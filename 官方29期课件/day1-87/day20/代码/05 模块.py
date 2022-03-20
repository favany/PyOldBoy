"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

'''
1、什么是模块？
    模块就是一系列功能的集合体,分为三大类
        I：内置的模块
        II：第三方的模块
        III：自定义的模块
            一个python文件本身就一个模块，文件名m.py，模块名叫m

            ps：模块有四种形式
            　　1 使用python编写的.py文件

            　　2 已被编译为共享库或DLL的C或C++扩展
            
            　　3 把一系列模块组织到一起的文件夹（注：文件夹下有一个__init__.py文件，该文件夹称之为包）
            
            　　4 使用C编写并链接到python解释器的内置模块
                        
2、为何有用模块
    I:内置与第三的模块拿来就用，无需定义，这种拿来主义，可以极大地提升自己的开发效率
    II:自定义的模块
        可以将程序的各部分功能提取出来放到一模块中为大家共享使用
        好处是减少了代码冗余，程序组织结构更加清晰
        

3、如何用模块
'''

y=333
z=444
import foo
# 1、首次导入模块会发生3件事
# 1、执行foo.py
# 2、产生foo.py的名称空间，将foo.py运行过程中产生的名字都丢到foo的名称空间中
# 3、在当前文件中产生的有一个名字foo，该名字指向2中产生的名称空间

# 之后的导入，都是直接引用首次导入产生的foo.py名称空间,不会重复执行代码
# import foo
# import foo
# import foo
# import foo


# 2、引用：
# print(foo.x)
# print(foo.get)
# print(foo.change)
# 强调1：模块名.名字，是指名道姓地问某一个模块要名字对应的值，不会与当前名称空间中的名字发生冲突
# x=1111111111111
# print(x)
# print(foo.x)

# 强调2：无论是查看还是修改操作的都是模块本身，与调用位置无关
# import foo
#
# x=3333333333
# # foo.get()
#
# foo.change()
# print(x)
#
# print(foo.x)
# foo.get()




# 3、可以以逗号为分隔符在一行导入多个模块
# 建议如下所示导入多个模块
# import time
# import foo
# import m

# 不建议在一行同时导入多个模块
import time,foo,m


# 4、导入模块的规范
#I. python内置模块
#II. 第三方模块
#III. 程序员自定义模块

# import time
# import sys
#
# import 第三方1
# import 第三方2
#
# import 自定义模块1
# import 自定义模块2
# import 自定义模块3


# 5、import 。。。 as 。。。
# import foo as f # f=foo
# f.get()


# import abcdefgadfadfas
# #
# # abcdefgadfadfas.f1
# # abcdefgadfadfas.f2
# # abcdefgadfadfas.f3


# import abcdefgadfadfas as mmm
#
# mmm.f1
# mmm.f2
# mmm.f3


#6、模块是第一类对象
import foo

#7、自定义模块的命名应该采用纯小写+下划线的风格


#8、可以在函数内导入模块
def func():
    import foo

