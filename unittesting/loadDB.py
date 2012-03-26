#!/usr/bin/python
'''
python dumpDB.py file_name db_name

'''
from mongokit import *
import cPickle
import sys

try:
    file_name = sys.argv[1]
    db_name = sys.argv[2]
except:
    print('error: Not correct argv...')
    sys.exit(0)

connect = Connection()
db = connect[db_name]

toLoad = cPickle.load(open(file_name, 'rb'))
for dump in toLoad:
    for collection, documents in dump.items():
        for document in documents:
            db[collection].insert(document)
