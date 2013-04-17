#coding:utf-8
'''
usage: getlink.py URL
ex: getlink.py [http://]www.baidu.com
'''

import urllib2
import re
import sys
   
def getlink(url):
    arg_url= str(url)
    if not re.compile(r'^http://').match(arg_url):
        arg_url = 'http://' + arg_url
    context = urllib2.urlopen(arg_url).read()
    result = re.compile(r'<a href="(http://.*?)"').finditer(context)
    return result

if len(sys.argv) != 2:
    print __doc__
    exit(1)
    
for url in getlink(sys.argv[1]):
    print url.group(1)
