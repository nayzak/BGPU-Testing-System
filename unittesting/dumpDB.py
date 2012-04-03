#!/usr/bin/python
'''
python dumpDB.py file_name db_name collection1 collection2 ... collectionN

'''
from mongokit import *
import cPickle
import sys

try:
    file_name = sys.argv[1]
    db_name = sys.argv[2]
    collections = sys.argv[3:]
except:
    print('error: Not correct argv...')
    sys.exit(0)

connect = Connection()
db = connect[db_name]

toDump = list()
for collection in collections:
    toDump.append({collection: list(db[collection].find())})

cPickle.dump(toDump, open(file_name, 'wb'))
