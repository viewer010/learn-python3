#!/usr/bin/env python3
#coding=utf8

#使用递归函数需要注意防止栈溢出
#python 默认递归深度为999
#python 6_recur.py 999  正常
#python 6_recur.py 1000  抛出异常
#sys.setrecursionlimit(100000) #可以设置为10000
#n!
from sys import argv
import sys
sys.setrecursionlimit(1000)
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
count=1
def add1(n):
    global count
    print('count=%d'%count)
    count+=1
    if n==1:
        return 1
    return 1+add1(n-1)

# print(fact(10))
print(argv)
print(add1(int(argv[1])))

#尾递归优化：
#尾递归是指，在函数返回的时候，调用函数本身，并且return语句不能包含表达式
#这样编译器或者解释器就可以把递归优化，使递归本身无论调用多少次，都只调用一个栈帧，不会出现栈溢出
# 循环可以看作一种特殊的尾递归函数
#python解释器没有做尾递归优化，所以仍然会栈溢出

def fact1(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num <= 1:
        return product
    return fact_iter(num-1,num*product)
print(fact1(990))

def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(4,'A','B','C')