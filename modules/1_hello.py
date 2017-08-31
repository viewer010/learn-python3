#!/usr/bin/env python3
#coding=utf8
#1，2行为标注注释，
#第一行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
#第二行注释表示py文件本身使用标准UTF－8编码

'a test module'
#这是一个字符串,表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Michael Liao'
#使用__author__变量把作者写进去

#后面为真正的代码
import sys
#导入入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
#
def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world!')
    elif len(args)==2:
        print('hello, %s!'%args[1])
    else:
        print("Too many arguments!")

#当在命令行运行python3 hello.py something 时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方
#导入该hello模块时，if判断将失败，因此这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试

if __name__=='__main__':
    test()

#作用域
#正常的函数和变量名是公开的（public），可以被直接引用
##__doc__,__author__,__name__ 特殊变量，有特殊用途，可以被直接引用
#_xx 和__xx这样的函数和变量就是非公开的(private)，不应该被直接引用，
###python没有完全限制访问private函数或者变量，只是从编程习惯上不应该引用private函数或者变量
#private函数或变量是一种非常有用的代码封装和抽象的方法，不需要关心其细节