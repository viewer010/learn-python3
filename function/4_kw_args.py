#!/usr/bin/env python3
#coding=utf8

#函数参数类型，
    #位置参数
        #必选参数   def power(x)
        #默认参数   def power(x=2)

    #可变参数   def power(*x) x为一个list或者tuple|| def power(x) x为一个list或者tuple
    #关键字参数 def power(**kw)
    #命名关键字参数，def power(name,age,*,city,job) *后面的参数视为命名关键字参数
    #             def power(name,aget,*args,city='Beijing',job)

# def power(x):
#     return x*x

def power(x,n=2):
    #1
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(4))
print(power(4,4))


#python 函数怎么做重载？
#python 参数比较灵活，是否可以通过调配参数达到重载的目的？

#为什么默认参数不能放在必选参数的前面？
#因为调用函数会产生歧义，例如下面调用foo(1,2)，函数该解释为foo(1,6,2)还是foo(1,6)，搞不清
#如果有默认值的参数在前，则调用函数必须使用key＝value的形式，或者进行特殊的规定，而不能使用直接送入Value的形式
#为了调用函数时更方便
'''
def foo(p1,p2=6,p3):
    return 0
print(foo(1,2,3))
print(foo(1,2))

  File "/Users/viewer/MyGit/learn-python3/function/kw_args.py", line 26
    def foo(p1,p2=6,p3):
           ^
SyntaxError: non-default argument follows default argument

'''


#使用默认参数必须指向不变对象
#python中，万物皆是对象
#pytohn中不存在所谓的传值调用，一切传递的都是对象的引用，也可以认为是传址
#坑 def add_end(L=[])
#不变对象有哪些？
    #str,int,float,number,tuple
    #None
    #undefined

'''
>>> i=37
>>> y=i
>>> i=i+1
>>> y
37
>>> i
38
>>> y is i
False
#整数不可变，范围[-5,256]
>>> x=1000
>>> y=1000
>>> x is y
False
>>> x=100
>>> y=100
>>> x is y
True
'''
#关键字参数
def print_scores(**kw):
    print('     Name score')
    print('---------------')
    for name,score in kw.items():
        print('%10s %d'%(name,score))

print_scores(Adam=99,Lisa=88,Bart=77)
data={
    'Adam Lee':99,
    'Lisa S':88,
    'F.Bart':77
}
print_scores(**data)

#命名关键字参数
def print_info(name,*,gender,city='Beijing',age):
    print('Personal Info')
    print('-------------')
    print('  Name: %s'%name)
    print('Gender: %s'%gender)
    print('  City: %s'%city)
    print('   Age: %s'%age)
    print()
print_info('Bob',gender='male',age=20)
print_info('Lisa',gender='female',city='Shanghai',age=18)
print_info('Lisa',gender='female',city='Shanghai',age=18,count=1)
'''
Traceback (most recent call last):
  File "/Users/viewer/MyGit/learn-python3/function/4_kw_args.py", line 104, in <module>
    print_info('Lisa',gender='female',city='Shanghai',age=18,count=1)
TypeError: print_info() got an unexpected keyword argument 'count'
'''
