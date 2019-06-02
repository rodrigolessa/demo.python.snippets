import os, werkzeug, shutil, pickle, json
from PIL import Image
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
CORS(app, allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials", "Access-Control-Allow-Origin"],
    supports_credentials=True, intercept_exceptions=False)

class Image(Resource):
    
    def post(self, image_name):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.FileStorage, location='files')
        args = parser.parse_args()

        dest = 'master/images/tmp_{}/'.format(image_name)
        if not os.path.exists(dest):
            os.makedirs(dest)
        
        try:
            args["file"].save("{}{}.png".format(dest, image_name))
        except:
            return "Erro na imagem.", 400
        
        fit_query = """python src/fit.py -i "{}{}.png" -o "{}{}_clusters.potato" -l "master/datasetOutput/logs" -a "master/data/kme-clusters.clr" -t "master/data/trees_clustered_codebook.npz" -d "Master/data/apted_custom_dist.pickle"  -z "Master/data/dendogram.npy" """.format(dest, image_name, dest, image_name)

        os.system(fit_query)
        
        with open("{}{}_clusters.potato".format(dest, image_name), 'rb') as f:
            try:
                labels_dict = pickle.load(f)
            except EOFError:
                pass

        shutil.rmtree(dest, ignore_errors=True)

        response = jsonify(labels_dict)
        response.status_code = 200

        return response  


api.add_resource(Image, "/image/<string:image_name>")
    
    
if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=False, threaded=True)
