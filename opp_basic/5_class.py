#!/usr/bin/env python3
#coding=utf8

#实例属性
#类属性，类本身的属性
#直接在class中定义属性，这种属性就是类属性
#类属性归类所有，类的所有实例都可以访问到

#给实例绑定属性的方法是通过实例变量，或者通过self变量

class Student(object):
    name='Student'
#创建实例s
s=Student()
#打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name)
print(Student.name)
#给实例绑定name属性
s.name='Michael'

#由于实例优先级比类属性高，因此，它会屏蔽掉类的name属性
print(s.name)
print(Student.name)
del s.name
print(s.name)

s1=Student()
print(s1.name)
Student.name='change'

print(s1.name)
print(s.name)