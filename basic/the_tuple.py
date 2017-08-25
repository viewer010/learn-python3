#!/usr/bin/env python3
#coding=utf8

classmates = ('Michael','Bob','Tracy')
print('classmates =',classmates)
print("len(classmates) =",len(classmates))
print('classmates[0] =',classmates[0])
print('classmates[1] =',classmates[1])
print('classmates[2] =',classmates[2])
print('classmates[-1] =',classmates[-1])

#cannot modify tuple
# classmates[0] = 'Adam'


#避免与数学公式中小括号歧义，在只有1个元素的tuple定义时必须加一个逗号
t=(1,)

#tuple所谓的“不变”，是指tuple的每个元素，指向拥有不变
#"可变"的tuple
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

'''
>>> t = ('a','b',['A','B'])
>>> t[2][0] = 'X'
>>> t
('a', 'b', ['X', 'B'])
'''
