# @File      : 03 属性查找.py
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/5/27 9:24 AM
# @Info      :


class Student:
    stu_school = 'old boy'
    count = 0

    def __init__(self, x, y):
        self.count += 1
        self.stu_name = x
        self.stu_age = y

    # 2. 功能的定义
    def tell_stu_info(self):
        print("学生信息：名字：%s 年龄：%s 学校：%s" % (
            self.stu_name,
            self.stu_age,
            self.stu_school
        ))

    def set_info(self, stu_obj, x, y, z):
        pass

    def choose(self, x):
        print("正在选课...")
        self.course = x


stu = Student("mophia", 18)
stu2 = Student("jun", 19)

# 类中存放的是对象共有的数据与功能
# 一、类可以访问：
# 1、类的数据属性
print(Student.stu_school)  # old boy

# 2、类的函数属性
print(Student.tell_stu_info)  # <function Student.tell_stu_info at 0x10497fe20>
print(Student.set_info)  # <function Student.set_info at 0x1049a2f80>

# 二、类中的东西是给对象用的
# 1、类的数据属性是共享给所有对象用的，访问的内存地址一致
print(id(Student.stu_school), id(stu.stu_school), id(stu2.stu_school))  # 4340092400 4340092400 4340092400

# 修改对象的数据属性，不影响其他对象和类本身的数据属性
stu.stu_school = "OLDBOY"
print(Student.stu_school, stu.stu_school, stu2.stu_school)  # old boy OLDBOY old boy

# 2、类中定义的函数主要是给对象使用的，而且是绑定给对象的
# 所有对象指向的都是相同的功能，但是绑定到不同的对象是不同的绑定方法，内存地址各不相同.

print(id(Student.tell_stu_info), id(stu.tell_stu_info), id(stu2.tell_stu_info))

print(Student.tell_stu_info)  # <function Student.tell_stu_info at 0x101413e20>
print(stu.tell_stu_info)  # <bound method Student.tell_stu_info of <__main__.Student object at 0x101443ee0>>
print(stu2.tell_stu_info)  # <bound method Student.tell_stu_info of <__main__.Student object at 0x101443d90>>

stu.tell_stu_info()

stu.choose("Python 全栈开发")
print("stu 的课程是", stu.course)
stu2.choose("Linux 运维")
print("stu2 的课程是", stu2.course)
