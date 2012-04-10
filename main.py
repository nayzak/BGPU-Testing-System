#!/usr/bin/env python
# coding: utf-8

# from whirlwind.core.bootstrap import Bootstrap
from application.bootstrap import Bootstrap
import os
import sys

#main app entry point
if __name__ == "__main__":
        try:
            Bootstrap.run(os.path.dirname(__file__), sys.argv[1])
        except:
            Bootstrap.run(os.path.dirname(__file__))
