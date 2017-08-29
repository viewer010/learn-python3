#!/usr/bin/env python3
#coding=utf8

def f(x):
    return x*x

print(list(map(f,[1,2,3,4,5,6,7,8,9])))
print(list(map(f,list(range(10)))))

#高阶函数map
#map函数接收2个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
list(map(str,[1,2,3,4,5,6,7,8,9]))

#高阶函数reduce
#reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接受2个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)

from functools import reduce
def add(x,y):
    return x+y
result=reduce(add,[1,3,5,7,9])
print(result)

def fn(x,y):
    return x*10+y
result=reduce(fn,[1,3,5,7,9])
print(result)

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
result=reduce(fn,map(char2num,'13579'))
print(result)

#简化为
def str2int1(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))

#进一步简化
def str2int(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(lambda x,y:x*10+y,map(char2num,s))

import time
def countTime(f,s):
    import time
    start=time.clock()
    print(f(s))
    end=time.clock()
    print(end-start)

print(str2int1('13579'))
print(str2int('13579'))
print(int('13579'))


print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))
#invaid
# ss=3
# pp=5
# print(ss=pp)


countTime(str2int1,'13579')
countTime(str2int,'13579')
countTime(int,'13579')
'''
0.0008680000000000077
13579
0.0007030000000000092
13579
0.0006009999999999904
#果然，还是自带的速度快
'''

#1
def normalize(name):
    return name[0].upper()+name[1:].lower() if len(name)>0 else name


L1=['adam','LISA','barT','a','']
L2=list(map(normalize,L1))
print(L2)

#2
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3*5*7*9 =',prod([3,5,7,9]))

#3
from functools import reduce
def str2float(s):
    point = 0
    def str2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}[s]
    def to_float(f,n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f*10+n
        else:
            point = point*10
            return f+n/point
    return reduce(to_float,map(str2num,s),0.0)
        
print('str2float(\'123.456\')=',str2float('123.456'))
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))