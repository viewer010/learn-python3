#!/usr/bin/env python3
#coding=utf8

#装饰器
#想要增强函数的功能，又不希望修改函数的定义，这种在代码运行期间动态增加功能的方式，称之为装饰器(Decorator)
# @log NameError: name 'log' is not defined 装饰器必须得写在前面
#装饰器在函数申明的时候就会被调用
def now():
    print('2015-3-25')

def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

# now1=log(now1)
@log

def now1():
    print('2015-3-25')

now1()
print(now1.__name__)
#???因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#@functools.wraps(func)
now()

#如果decorate本身需要传入参数，就需要编写一个返回decorator的高阶函数，写出来会更复杂
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

#now = log('execute')(now)
@log('execute')
def now2():
    print('2015-3-25')

now2()
print(now2.__name__)

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s():"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

#now = log('execute')(now)
@log('execute')
def now2():
    print('2015-3-25')
now2()
print(now2.__name__)

#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print("begain call %s"%func.__name__)
#         func(*args,**kw)
#         print("end call %s"%func.__name__)
#     return wrapper
# #TypeError: log() missing 1 required positional argument: 'func'
# @log
# def now3():
#     print('2015-3-25')
# now3()

#
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("begain call %s"%func.__name__)
        ret=func(*args,**kw)
        print("end call %s"%func.__name__)
        return ret
    return wrapper
#TypeError: log() missing 1 required positional argument: 'func'

@log
def now4():
    print('2015-3-25')

now4()

#2
import functools

def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print("%s %s"%(text,func.__name__))
                return func(*args,**kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print("%s %s"%('call',text.__name__))
            return text(*args,**kw)
        return wrapper
#f=log(f)
@log
def f():
    print('不带参数')
f()
print(f.__name__)

#f = log('execute')(f)
@log('execute')
def f():
    print('带参数')
f()
print(f.__name__)

#2_1
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    # return decorator
    if isinstance(text,str):
        return decorator
    else:
        f=text
        text=''
        return decorator(f)

@log
def f():
    print('不带参数1')
f()
print(f.__name__)

@log('execute')
def f():
    print('带参数1')
f()
print(f.__name__)