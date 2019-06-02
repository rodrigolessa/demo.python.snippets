import pyodbc, argparse, pickle

class Storage(object):
    """
    """

    def __init__(self, database):
        self.database = database
        self.cursor = None
    
    def connect(self):
        cnxn = pyodbc.connect(r'Driver={SQL Server Native Client 11.0};'
                    r'Server=dev;'
                    r'Database=figura;'
                    r'Trusted_Connection=yes;'
                    r'UID=sa;'
                    r'PWD=lilia;')

        self.cursor = cnxn.cursor()
    
    def store(self, query):
        self.cursor.execute(query)

    def lookup(self, query):
        self.cursor.execute(query)

        return self.cursor

    def commit(self):
        self.cursor.commit()
    