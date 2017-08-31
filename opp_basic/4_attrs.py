#!/usr/bin/env python3
#coding=utf8

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj,\'x\') =',hasattr(obj,'x'))#有属性x吗
print('hasattr(obj,\'y\') =',hasattr(obj,'y'))#有属性y吗
setattr(obj,'y',19)#设置一个属性'y'

print('hasattr(obj,\'y\') =',hasattr(obj,'y')) #有属性y吗
print('getattr(obj,\'y\') =',getattr(obj,'y')) #获取属性y
print('obj.y =',obj.y)#获取属性y

#获取属性’z',如果不存在，返回默认值404
print('getattr(obj,\'z\') =',getattr(obj,'z',404))

f=getattr(obj,'power') #获取属性‘power'
print(f)
print(f())