#!/usr/bin/env python3
#coding=utf8
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print("%s: %s"%(self.name,self.score))
    def grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)

print('bart.name=',bart.name)
print('bart.score=',bart.score)
bart.print_score()

print('lisa.name',lisa.name)
print('lisa.score=',lisa.score)
lisa.print_score()

print('grade of Bart:',bart.grade())
print('grade of Lisa:',lisa.grade())

#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
bart.age=8
print(bart.age)

# print(lisa.age)#AttributeError

# 可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了
# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念