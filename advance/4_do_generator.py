#!/usr/bin/env python3
#coding=utf8

#生成器：generator
#在python中一边循环一遍计算的机制称为生成器
#优点是节省空间，到用到的时候才计算

# 创建生成器有2个方法
# 一、把一个列表生成式的［］换成（）
# 二、函数定义中包涵yield关键字

#打印generator里的函数
#一、使用next函数： next(g)
#二、使用for循环，
#               使用for循环拿不到生成器的返回值,要想拿到返回值，得使用next()必须捕获生成器停止时的StopIteration错误才行,e.value为return返回值

s=(x*x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
f=fib(10)
print('fib(10):',f)
for x in f:
    print(x)

#call generator manually:
g=fib(5)
while 1:
    try:
        #python为g.next()
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

g=fib(6)
try:
    for x in g:
        print('g:',x)
except StopIteration as e:
    print('Generator return value:',e.value)

#myself
# def triangles():
#     tmp=[0,1,]
#     tmp1=[]
#     while True:
#         yield tmp[1:]
#         tmp1=[0,]
#         for i,value in enumerate(tmp[:-1]):
#             tmp1.append(tmp[i]+tmp[i+1])
#         tmp1.append(1)
#         tmp=tmp1

#others 1
# def triangles():
#     L=[1]
#     while 1:
#         yield L
#         L=[L[i-1]+L[i] for i in range(1,len(L))]
#         L.insert(0,1)
#         L.append(1)
#others 2
def triangles():
    n,l1=0,[1]
    while n<max:
        yield l1
        l1=[x+y for x,y in zip([0]+l1,l1+[0])]
        n=n+1

n=0
for t in triangles():
    print(t)
    n=n+1
    if n==10:
        break

