"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

class Student:
    # 1、变量的定义
    stu_school='oldboy'
    count=0

    # 空对象,'egon',18,'male'
    def __init__(self,x,y,z):
        Student.count += 1

        self.stu_name=x # 空对象.stu_name='egon'
        self.stu_age=y  # 空对象.stu_age=18
        self.stu_gender=z # 空对象.stu_gender='male'
        # return None

    # 2、功能的定义
    def tell_stu_info(self):
        print('学生信息：名字：%s 年龄：%s 性别：%s' %(
            self.stu_name,
            self.stu_age,
            self.stu_gender
        ))

    def set_info(self,x,y,z):
        self.stu_name=x
        self.stu_age=y
        self.stu_gender=z

    def choose(self,x):
        print('正在选课')
        self.course=x

stu1_obj=Student('egon',18,'male') # Student.__init__(空对象,'egon',18,'male')
stu2_obj=Student('lili',19,'female')
stu3_obj=Student('jack',20,'male')

# print(stu1_obj.count)
# print(stu2_obj.count)
# print(stu3_obj.count)

# 类中存放的是对象共有的数据与功能
# 一：类可以访问：
# 1、类的数据属性
# print(Student.stu_school)
# 2、类的函数属性
# print(Student.tell_stu_info)
# print(Student.set_info)

# 二：但其实类中的东西是给对象用的
# 1、类的数据属性是共享给所有对象用的，大家访问的地址都一样
# print(id(Student.stu_school))

# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))
# print(id(stu3_obj.stu_school))

# Student.stu_school='OLDBOY'
# stu1_obj.stu_school='OLDBOY'
# print(stu1_obj.stu_school)

# print(Student.stu_school)
# print(stu2_obj.stu_school)
# print(stu3_obj.stu_school)

# 2、类中定义的函数主要是给对象使用的，而且是绑定给对象的，虽然所有对象指向的都是相同的功能，但是绑定到不同的对象就是不同的绑定方法，内存地址各不相同

# 类调用自己的函数属性必须严格按照函数的用法来
# print(Student.tell_stu_info)
# print(Student.set_info)

# Student.tell_stu_info(stu1_obj)
# Student.tell_stu_info(stu2_obj)
# Student.tell_stu_info(stu3_obj)

# Student.set_info(stu1_obj,'EGON',19,'MALE')
# Student.tell_stu_info(stu1_obj)

# 绑定方法的特殊之处在于：谁来调用绑定方法就会将谁当做第一个参数自动传入
# print(Student.tell_stu_info)
# print(stu1_obj.tell_stu_info)
# print(stu2_obj.tell_stu_info)
# print(stu3_obj.tell_stu_info)

# stu1_obj.tell_stu_info() #tell_stu_info(stu1_obj)
# stu2_obj.tell_stu_info() #tell_stu_info(stu2_obj)
# stu3_obj.tell_stu_info() #tell_stu_info(stu3_obj)

#
# stu1_obj.choose('python全栈开发')
# print(stu1_obj.course)
#
# stu2_obj.choose('linux运维')
# print(stu2_obj.course)
#
# stu3_obj.choose('高级架构师')
# print(stu3_obj.course)



l1=['aa','bb','cc'] # l=list([1,2,3])
l2=[111,222,333] # l=list([1,2,3])
# print(l1.append)
# print(list.append)

# l1.append('dd')
# l2.append('dd')
# print(l1)
# print(l2)

# list.append(l1,'dd')
# list.append(l2,'dd')
# print(l1)
# print(l2)
