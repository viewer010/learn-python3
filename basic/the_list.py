#!/usr/bin/env python3
#coding=utf8
classmates=['Michael','Bob','Tracy']
print('classmates =',classmates)
print('len(classmates) =',len(classmates))
print('classmates[0] =',classmates[0])
print('classmates[1] =',classmates[1])
print('classmates[2] =',classmates[2])
print('classmates[-1] =',classmates[-1])
classmates.pop()
print('classmates =',classmates)

#修改
classmates[0]='Adam'
print('classmates =',classmates)

classmates.append('Lucy')
print('classmates =',classmates)

for i,value in enumerate(classmates):
    print(i,value)
