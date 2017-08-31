#!/var/bin/env python2
#coding=utf8

#偏函数
#当函数参数个数太多，需要简化时，使用functools.partial可以创建新的函数，这个新的函数可以固定住原函数的部分参数，从而使调用简单

import functools

int2=functools.partial(int,base=2)

print('100000 =',int2('100000'))
print('1010101 =',int2('1010101'))