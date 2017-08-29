#!/usr/bin/evn python3
#coding=utf8

#列表生成式
print(list(range(0,11)))
print([x*x for x in range(1,11)])

#加if判断
print([x*x for x in range(1,11) if x%2==0])

#两层
print([m+n for m in 'ABC' for n in "XYZ"])

d={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])
L=['Hello','World',"IBM",'Apple',18]
print([s.lower() for s in L if isinstance(s,str)])

#列出当前文件目录下所有的文件名和目录名
import os
print([d for d in os.listdir('.')])