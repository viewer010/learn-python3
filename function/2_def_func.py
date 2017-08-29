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
    if (not isinstance(a,(int,float))) or (not isinstance(b,(int,float))) or (not isinstance(c,(int,float))):
        # raise TypeError("bad operand type")
        print("arg must be int or float")
        return None
    dat = b*b - 4*a*c
    if a == 0 or dat < 0:
        # raise TypeError("warnning:a is zero")
        print("a not zero,or b^2-4ac >=0")
        return None
    tmp = math.sqrt(dat)
    result1=(-b+tmp)/(2*a)
    result2=(-b-tmp)/(2*a)
    return result1,result2

if __name__ == "__main__":
    # question=input("please input the equation\n")
    print(quadratic(2,3,1))
    print(quadratic(1,3,-4))
    print(quadratic(1,3,4))
    print(quadratic(0,3,-4))
