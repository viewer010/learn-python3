#!/usr/bin/env python3
#coding=utf8
#filename 7_decorator_2.py
#question
#
#写一个装饰器，限制函数没10秒之行一次

import time
from functools import wraps

def decorator(func):
    '''
    cache for function result,which is immutable with fixed arguments
    '''
    print("initial cache for %s"%func.__name__)
    cache={}
    
    @wraps(func)
    def decorated_func(*args,**kw):
        #函数名作为key
        key=func.__name__
        result=None
        #判断是否存在缓存
        print('cache',cache)
        if key in cache.keys():
            (result,updateTime)=cache[key]
            #过期时间固定为10秒
            if time.time()-updateTime < 10:
                print("limit call 10S",key,"also have %s's"%str(time.time()-updateTime))
                result = updateTime
            else:
                print("cache expired !!! can call")
                result=None
        else:
            print("no cache for",key)
        
        if result is None:
            result = func(*args,**kw)
            cache[key] = (result,time.time())
        return result
    return decorated_func

@decorator
def func(x):
    print("call func",x)

@decorator
def func1(x):
    print("call func1",x)

func(1)
func1(1)
func(1)
func1(1)

# time.sleep(10)
func(2)

#吊吊的装饰器
def Before(*args,**kw):
    print('before')
def After(*args,**k2):
    print('after')
def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(*args,**kw):
            before_result=before_func(*args,**kw)
            if(before_result != None):
                return before_result
            main_result = main_func(*args,**kw)
            if(main_result != None):
                return main_result
            after_result = after_func(*args,**kw)
            if(after_result != None):
                return after_result
        return wrapper
    return outer

@Filter(Before,After)
def Index(request,kargs):
    print('index',request,kargs)

Index('hello','world!')