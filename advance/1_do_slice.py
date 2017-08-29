#!/usr/bin/env python3
#coding=utf8
#L[0:3]表示，从索引0开始取，知道索引3为止，但不包括索引3。

print(list(range(100))[1::2])
print([x*2-1 for x in range(1,51)])
print([x for x in range(1,100) if x%2])

L=['Michael','Sarah','Tracy','Bob','Jack']
print('L[0:3] =',L[0:3])
print('L[:3] =',L[:3])
print('L[1:3] =',L[1:3])
print('L[-2:] =',L[-2:])

R=list(range(100))
print('R[:10] =',R[:10])
print('R[-10:] =',R[-10:])
print('R[10:20] =',R[10:20])
print('R[:10:2] =',R[:10:2])
print('R[::5] =',R[::5])
 