#!/usr/bin/env python3
#coding=utf8

#返回函数
#函数作为返回值
#不立即求和，而是根据需要再计算
#每次调用返回函数，都会返回一个新的函数
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lazy_sum(1,2,4,5,7,8,9)
print(f)
print(f())
#闭包
#在函数lazy中又定义了函数sum，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回函数中，这种称为“闭包”的程序结构拥有极大的威力
#当一个函数返回一个函数后，其内部的局部变量还被新函数引用，所以闭包用起来简单，实现起来可不易
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
#如果一定要引用，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已经绑定的值不变：

#why f1(),f2(),f3() returns 9，9，9 ，other than 1，4，9？
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print('f1() =',f1())
print('f2() =',f2())
print('f3() =',f3())

#全部都是9，原因在于返回的函数引用变量i，但它并非立刻执行，等到2个函数都返回时，它们所引用的变量i 已经变成了3，因此最终结果为9
#如果一定要引用，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已经绑定的值不变：

#fix
def count():
    fs=[]
    def f(n):
        def j():
            return n*n
        return j
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count()
print('f1() =',f1())
print('f2() =',f2())
print('f3() =',f3())

#fix
def count():
    fs=[]
    for i in range(1,4):
        def f(n):
            return n*n
        fs.append(f(i))
    return fs

f1,f2,f3 = count()
print('f1 =',f1)
print('f2 =',f2)
print('f3 =',f3)
#这个就不是返回函数了
# TypeError: 'int' object is not callable
# print('f1() =',f1())
# print('f2() =',f2())
# print('f3() =',f3())