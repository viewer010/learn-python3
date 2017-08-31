#!/usr/bin/env python3
#coding=utf8
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

# now1=log(now)
@log

def now1():
    print('2015-3-25')

now1()
print(now1.__name__)


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
print(now4.__name__)

#重复调用
def log(times):
    print("run log")
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            for count in range(1,times+1):
                print("the %d time run %s "%(count,func.__name__))
                func(*args,**kw)
        return wrapper
    return decorator

@log(5)
def now5():
    print('2015-3-25')

now5()
print(now5.__name__)