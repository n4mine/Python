"""
Usage:
python list.py path
"""

import os, sys

if len(sys.argv) != 2:
    print __doc__
    sys.exit(1)
path = sys.argv[1]

def tree(path, step, depth):
    if os.path.isdir(path):
        root,dirs,files = os.walk(path).next()
        if os.path.isdir(root):
            for file in files:
                print step * depth + file
            for dir in dirs:
                print step * depth + dir + '/'
                tree(os.path.join(root, dir), step, depth + 1)
    else:
        print r'%s is not a dir' % path


tree(path, '--', 1) 
