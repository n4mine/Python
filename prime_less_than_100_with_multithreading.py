import threading

class p(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = [num]
    def run(self):
        global result
        temp = filter(lambda x:x if x == 2 else not [y for y in range(2,x) if x%y == 0], self.num)
        '''
        if len(temp) == 1:
            print "%s: prime %d" % (self.name,temp[0])
        else:
            print "%s: not prime" % self.name
        '''
        result += temp

result = []
threads = []

def test():
    for i in range(1,101):
        t = p(i)
        threads.append(t)
    for i in range(100):
        threads[i].start()
    for i in range(100):
        threads[i].join()

if __name__ == '__main__':
    test()
    print result 
