#!/usr/bin/env python
# encoding:utf-8

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import os

def getAPart(pos):
    '''get a part by send Range header'''

    startPos = pos[0]
    endPos = pos[1]

    f = urllib2.Request(url)
    f.add_header('Range' , 'bytes=' + str(startPos) + '-' + str(endPos))
    f.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')
    req = urllib2.urlopen(f)
    content = req.read()

    filename = "./part_"
    if os.path.exists(filename):
        fd = open('./part_', 'r+')
    else:
        fd = open('./part_', 'w+')

    fd.seek(startPos)
    fd.write(content)
    fd.close()

def genList(length):
    '''return a list which used by HTTP request header, start and end as a tuple'''

    length = int(length)

    startList = [x for x in xrange(0, length, rangeSize) ]
    endList = [y + rangeSize - 1 for y in startList ]

    '''
    THE FOLLOW CODE: `length -1`

    https://tools.ietf.org/html/rfc7233#section-2.1

    Examples of byte-ranges-specifier values:
    The first 500 bytes (byte offsets 0-499, inclusive):
        bytes=0-499
    '''
    if endList[-1] > length - 1:
        endList[-1] = length - 1

    return zip(startList, endList)

if __name__ == '__main__':
    url = 'http://dldir1.qq.com/qqfile/qq/QQ8.2/17720/QQ8.2.exe'
    length = urllib2.urlopen(url).headers['Content-Length'] # just get length

    # 分块大小
    rangeSize = 1024 * 1024 * 5

    rangeList = genList(length)

    pool = ThreadPool(8)
    pool.map(getAPart, rangeList)
    pool.close()
    pool.join()
