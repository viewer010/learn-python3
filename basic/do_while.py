#!/usr/bin/env python3
#coding=utf8

#计算1+2+3+...+100:
sum = 0
n=1
while n<=100:
    sum +=n
    n+=1
print(sum)

sum=0
for i in range(1,101):
    sum+=i
print(sum)


#计算1*2*3*...*100
acc=1
n=1
while n<=100:
    acc*=n
    n+=1
print(acc)

