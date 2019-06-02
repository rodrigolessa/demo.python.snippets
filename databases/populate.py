import argparse, pickle, re, sys
from storage import Storage
sys.path.insert(0,'src/')
from image import Image

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="visual trees object's file")
    return parser.parse_args()

def read_data(vt_path):
    vts = []
    with open(vt_path, 'rb') as f:
        while True:
            try:
                vts.append(pickle.load(f))
            except EOFError:
                break
    
    return vts

def main():
    args = init_args()

    visual_trees = read_data(args.f)
    
    storage = Storage('VisualTrees')

    storage.connect()

    for visual_tree in visual_trees:
        name = re.sub('.*\/', '', visual_tree.path)
        name = re.sub('\..*', '', name)

        query = "INSERT INTO VisualTrees(Name, Label) VALUES('{}', {})"\
            .format(name, visual_tree.tree.label)
        storage.store(query)

    storage.commit()
main()