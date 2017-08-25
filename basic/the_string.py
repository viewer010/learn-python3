#!/usr/bin/env python3
#coding=utf8
s='Python 中文'
print(s)
b=s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

#python 数据类型有
'''
int     整数      没有大小限制
float   浮点数     没有大小限制，但是超出一定范围就直接表示为 inf(无限大)
str     字符串
bool    布尔值     (True|False)
None    空值

python内置数据类型
list    列表      有序集合；索引从0开始，-1表示最后一个元素,超出会越界
tuple   元组      有序列表；一旦初始化就不能更改
dict    字典      类比于其他语言中的map，使用键-值(key-value)存储

'''

