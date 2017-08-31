#!/usr/bin/env python3
#coding=utf8

#在Python中，一个.py文件就称之为一个模块(Module)
#大大提高了代码的可维护性
#方便其他地方使用
#避免函数名和变量名冲突

#为避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（package）
#引入包之后，只要顶层的模块名不与别人冲突，那所有模块都不会与别人冲突
#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则Python就把这个目录当成普通目录
#__init__.py可以是一个空文件，也可以有Python代码，__init__.py本身就是一个模块，而它的模块名就是mycompany

# import company
# company
# print(dir(company))
# company.abc

import company
#company/__init__.py中的内容是可以使用的，但xyz和其他模块不能使用
# company.xyz.xyz()

#xyz模块可用
import company.xyz
#abc模块可用
from company import abc

company.xyz.xyz()
company.abc.abc()

print('main',__name__)