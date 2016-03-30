#!/usr/bin/env python
# coding: utf-8

f = open('data', 'r')

sum = 0
buffer_size=20
while True:
    current_part = f.readline(buffer_size)
    
#    print '--debug, before current_part:', current_part
    if current_part.endswith(' ') or current_part.endswith('\n'):
#        print '--debug, Ends with space or newline'
        sum += len(current_part.split())
    elif not current_part: # EOF
#        print '--debug, EOF'
        break
    else: # 刚好截到单词中间
        next = f.read(1)
        while next and next != ' ' and next != '\n':
#            print '--debug, next:', next
            current_part += next
            next = f.read(1)
        sum += len(current_part.split())

#    print '--debug, after current_part:', current_part

print 'total num:', sum

f.close()
