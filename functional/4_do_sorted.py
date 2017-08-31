#!/usr/bin/env python3
#coding=utf8

#python2.7
#sorted(iterable, cmp=None, key=None, reverse=False)

#python3
#sorted(iterable, key=None, reverse=False)

#通常规定，对于两个元素x和y，如果认为x<y,则返回－1,如果认为x==y,则返回0，如果认为x>y,则返回1，这样排序算法就不用关系具体的比较过程，而是根据比较结果直接进行排序

#python内置的sorted()函数就可以对list进行排序
print(sorted([36,5,9,21]))

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([36,5,-12,9,-21],key=abs))

print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
#反向排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))

#1
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    return t[0].lower()

L2=sorted(L,key=by_name)
print(L2)

#2
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_score(t):
    return t[1]

L2=sorted(L,key=by_score)
print(L2)

#operator.itemgetter函数的使用
#print(sorted(students,key=itemgetter(0,1)))
#进行多级排序，即先跟第二个域进行排序，再根据第一个域进行排序
from operator import itemgetter
L=['bob','about','Zoo','Credit']
print(sorted(L))
print(sorted(L,key=str.lower))

students = [('Bob',75),('Adam',92),('Adam',82),('Adam',62),('Bart',66),('Bart',88),('Lisa',88)]
print(sorted(students,key=itemgetter(0)))
print(sorted(students,key=lambda t:t[1]))
print(sorted(students,key=itemgetter(1),reverse=True))
print(sorted(students,key=itemgetter(0,1)))
