#!/usr/bin/env python3
#coding=utf8

#filter()函数用于过滤序列
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filte()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10,15])))

def not_empty(s):
    return s and s.strip()

print(not_empty(' '))
print(not_empty(None))
print(list(filter(not_empty,['A','','B',None,'C','   '])))

def isTrue(x):
    if x:
        return True
    else:
        return False
    #return True if x else False
print(list(map(isTrue,['A','','B',None,'C','   '])))

#filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

#用filter求素数
#埃氏筛选法

#1，先构造一个从3开始的奇数序列
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#2.定义一个筛选函数

def _not_divisible(n):
    print('_not_divisible',n)
    return lambda x:x % n >0

#3.定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
for n in primes():
    if n<1000:
        print(n)
    else:
        break

#next()调用为循环调用，先加的先计算

#练习1
#me...
# def is_palindrome(n):
#     u=int(str(n)[::-1])
#     print(n,u)
#     return n==u
#others
def is_palindrome(n):
    return str(n)==str(n)[::-1]

output=filter(is_palindrome,range(1,1000))
print(list(output))