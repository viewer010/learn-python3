#!/usr/bin/env python3
#coding=utf8

x = abs(100)
y = abs(-20)
print(x,y)
print('max(1,2,3) =',max(1,2,3))
print('main(1,2,3) =',min(1,2,3))
print('sum([1,2,3]) =',sum([1,2,3]))


# help(abs)

x=10
print(hex(10))

#函数名其实就是指向一个函数对象的引用，完全可以把函数名复制给一个变量，相当于给这个函数起了一个别名
a=abs
print(a(-1))

#当然，已有的函数名可以指向新的对象，这会导致当前环境下该内置函数名功能的改变,得关闭当前程序，重启才行
abs=hex
print(abs(-1))