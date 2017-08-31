#!/usr/bin/env python3
#coding=utf8

# type()
#我们来判断对象类型，使用type()函数：
#基本类型,对象或者类
print('type(123) =',type(123))
print('type(\'123\') =',type('123'))
print('type(None) =',type(None))
print('type(abs) =',type(abs))

import types
print('type(\'abc\')==str?',type('abc')==str)

import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# 能用type()判断的基本类型也可以用isinstance()判断
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：