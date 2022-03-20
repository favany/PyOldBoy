"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# 1、什么是继承
# I:继承是一种创建新类的方式，新建的类可称为子类或派生类，父类又可称为基类或超类,子类会遗传父类的属性
# II:需要注意的是：python支持多继承
#          在Python中，新建的类可以继承一个或多个父类

# class Parent1(object):
#     x=1111
#
# class Parent2(object):
#     pass
#
# class Sub1(Parent1): # 单继承
#     pass
#
# class Sub2(Parent1,Parent2): # 多继承
#     pass

# print(Sub1.__bases__)
# print(Sub2.__bases__)

# print(Sub1.x)

# ps1: 在python2中有经典类与新式类之分
# 新式类：继承了object类的子类，以及该子类的子类子子类。。。
# 经典：没有继承object类的子类，以及该子类的子类子子类。。。

# ps2:在python3中没有继承任何类，那么会默认继承object类，所以python3中所有的类都是新式类
# print(Parent1.__bases__)
# print(Parent2.__bases__)
#

# III:python的多继承
#     优点：子类可以同时遗传多个父类的属性，最大限度地重用代码
#     缺点：
#         1、违背人的思维习惯：继承表达的是一种什么"是"什么的关系
#         2、代码可读性会变差
#         3、不建议使用多继承，有可能会引发可恶的菱形问题，扩展性变差，
#         如果真的涉及到一个子类不可避免地要重用多个父类的属性，应该使用Mixins

# 2、为何要用继承：用来解决类与类之间代码冗余问题


# 3、如何实现继承
# # 示范1：类与类之间存在冗余问题
# class Student:
#     school='OLDBOY'
#
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def choose_course(self):
#         print('学生%s 正在选课' %self.name)
#
#
# class Teacher:
#     school='OLDBOY'
#
#     def __init__(self,name,age,sex,salary,level):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.salary=salary
#         self.level=level
#
#     def score(self):
#         print('老师 %s 正在给学生打分' %self.name)
#


# 示范2：基于继承解决类与类之间的冗余问题
class OldboyPeople:
    school = 'OLDBOY'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(OldboyPeople):
    def choose_course(self):
        print('学生%s 正在选课' % self.name)
# stu_obj = Student('lili', 18, 'female')
# print(stu_obj.__dict__)
# print(stu_obj.school)
# stu_obj.choose_course()


class Teacher(OldboyPeople):
    #           老师的空对象，'egon',18,'male',3000,10
    def __init__(self, name, age, sex, salary, level):
        # 指名道姓地跟父类OldboyPeople去要__init__
        OldboyPeople.__init__(self,name,age, sex)
        self.salary = salary
        self.level = level

    def score(self):
        print('老师 %s 正在给学生打分' % self.name)

tea_obj=Teacher('egon',18,'male',3000,10)
# print(tea_obj.__dict__)
# print(tea_obj.school)

tea_obj.score()