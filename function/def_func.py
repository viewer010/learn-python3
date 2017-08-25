#!/usr/bin/env python3
#coding=utf8

import math

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#函数返回值为一个tuple
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = x + step * math.sin(angle)
    return nx,ny

n = my_abs(-20)
print(n)

x,y = move(100,100,60,math.pi/6)
print(x,y)

#TypeError: bad operand type:
# my_abs('123')

def quadratic(a,b,c):
    if not isinstance(a,(int,float))