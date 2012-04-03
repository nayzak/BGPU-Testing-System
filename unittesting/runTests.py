#!/usr/bin/python
import subprocess
'''
  python runTest.py
  dump db, load db, run test

'''

subprocess.call(["python","dumpDB.py", "dump", "testing", "users", "groups"])
subprocess.call(["python","loadDB.py", "dump", "cur"])
subprocess.call(["python", "-m", "unittest", "discover", "../.", "-p", "*_test.py"])
