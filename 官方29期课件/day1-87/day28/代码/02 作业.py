"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# 整合->解耦合->扩展性增强

class School:
    school_name = 'OLDBOY'

    def __init__(self, nickname, addr):
        self.nickname = nickname
        self.addr = addr
        self.classes = []

    def related_class(self, class_obj):
        # self.classes.append(班级名字)
        # self.classes.append(class_name)
        self.classes.append(class_obj)

    def tell_class(self): # 改
        # 打印的班级的名字
        print(self.nickname.center(60,'='))
        # 打印班级开设的课程信息
        for class_obj in self.classes:
            class_obj.tell_course()


# # 一：学校
# #1、创建校区
school_obj1=School('老男孩魔都校区','上海')
school_obj2=School('老男孩帝都校区','北京')
#
# #2、为学校开设班级
# # 上海校区开了:脱产14期，上海校区开了脱产15期
# school_obj1.related_class("脱产14期")
# school_obj1.related_class("脱产15期")
#
# # 北京校区开了:脱产29期
# school_obj2.related_class("脱产29期")
#
# #3、查看每个校区开设的班级
# school_obj1.tell_class()
# school_obj2.tell_class()


class Class:
    def __init__(self, name):
        self.name = name
        self.course = None

    def related_course(self, course_obj):
        # self.course = course_name
        self.course = course_obj

    def tell_course(self):
        print('%s' % self.name,end=" ")
        self.course.tell_info() # 打印课程的详细信息

# 二：班级
# 1、创建班级
class_obj1 = Class('脱产14期')
class_obj2 = Class('脱产15期')
class_obj3 = Class('脱产29期')

# 2、为班级关联一个课程
# class_obj1.related_course('python全栈开发')
# class_obj2.related_course('linux运维')
# class_obj3.related_course('python全栈开发')

# 3、查看班级开设的课程信息
# class_obj1.tell_course()
# class_obj2.tell_course()
# class_obj3.tell_course()

# 4、为学校开设班级
# 上海校区开了:脱产14期，上海校区开了脱产15期
school_obj1.related_class(class_obj1)
school_obj1.related_class(class_obj2)

# 北京校区开了:脱产29期
school_obj2.related_class(class_obj3)


# school_obj1.tell_class()
# school_obj2.tell_class()



class Course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price

    def tell_info(self):
        print('<课程名:%s 周期:%s 价钱:%s>' %(self.name,self.period,self.price))
# 三：课程
# 1、创建课程
course_obj1=Course('python全栈开发','6mons',20000)
course_obj2=Course('linux运维','5mons',18000)

# 2、查看课程的详细信息
# course_obj1.tell_info()
# course_obj2.tell_info()

# 3、为班级关联课程对象
class_obj1.related_course(course_obj1)
class_obj2.related_course(course_obj2)
class_obj3.related_course(course_obj1)

# class_obj1.tell_course()
# class_obj2.tell_course()
# class_obj3.tell_course()

school_obj1.tell_class()
school_obj2.tell_class()


class Student:
    pass




