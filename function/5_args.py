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


def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

#通过tuple和dict调用上述函数
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)

args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)

args=[1,2,3]
kw={'d':88,'x':'#'}
f2(*args,**kw)

#func(*args,**kw) 对于任意函数，都可以通过类似func(*args,**kw)的形式调用它，无论它的参数是如何定义的