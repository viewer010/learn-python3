#!/usr/bin/env python3
#coding=utf8
from multiprocessing import Process,Queue
import os,time,random

#写数据进程执行的代码
def write(q):
    print('Process to write: %s '% os.getpid())
    for value in range(10):
        print('Put %s to queue ...' % str(value))
        q.put(str(value))
        time.sleep(random.random())

#读数据进程的代码
def read(q):
    print('Process to read: %s'%(os.getpid()))
    while True:
        value = q.get(True)
        print('Get %s to queue ...' % value)
        time.sleep(random.random())

if __name__ == '__main__':
    #父进程常见Queue，并传给各个子进程
    q =  Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程，pw写入
    pw.start()
    #启动子进程,pr读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程是死循环，无法等待其结束，只能强行终止
    pr.terminate()

