#!/usr/bin/env python3
#coding=utf8

#函数参数类型，
    #位置参数
        #必选参数   def power(x)
        #默认参数   def power(x=2)

    #可变参数   def power(*x) x为一个list或者tuple|| def power(x) x为一个list或者tuple
    #关键字参数 def power(**kw)
    #命名关键字参数，def power(name,age,*,city,job) *后面的参数视为命名关键字参数
    #             def power(name,aget,*args,city='Beijing',job)
#参数组合顺序为：
    #必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def hello(greeting,*args):
    if(len(args)==0):
        print('%s!'%greeting)
    else:
        print('%s,%s!'%(greeting,', '.join(args)))

hello('Hi')
hello('Hi','Sarah')
hello('Hello','Michael','Bob','Adam')

names=('Bart','Lisa')
hello('hello',*names)