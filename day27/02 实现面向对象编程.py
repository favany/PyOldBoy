# @File      : 02 实现面向对象编程.py
# @Author    : 刘俊 mophia
# @Website   : mophia.com
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/5/26 4:19 PM
# @Info      : www.zhihu.com/p/109292504

# 先定义类
# 类体代码是在类定义阶段就会立即执行，会产生类的名称空间
class Student:  # 大驼峰
    # 1. 变量的定义
    stu_school = 'old boy'

    # 2. 功能的定义
    def tell_stu_info(self, stu_obj):
        print("学生信息：名字：%s 年龄：%s " % (
            stu_obj["stu_name"],
            stu_obj["age"],
        ))

    def set_info(self, stu_obj, x, y, z):
        pass

    print("=======>")


# print(Student.__dict__)

# 属性访问的语法
# 1. 访问数据属性
# print(Student.stu_school) # Student.__dict__['stu_school']
# 2. 访问函数属性
# print(Student.set_info) # Student.__dict__['set_info']

# 二、再调用类产生对象
stu1_obj = Student()


# stu1_obj.name = 'mophia'  # stu1_obj.__dict__['name'] = 'mophia'
# stu1_obj.stu_age = 18  # stu1_obj.__dict__['stu_age'] = 18
# print("stu1_obj", stu1_obj.__dict__)
# 
# stu2_obj = Student()
# stu2_obj.name = 'bfy'
# stu2_obj.stu_age = 18
# print("stu2_obj", stu2_obj.__dict__)

def init(obj, x, y):
    obj.stu_name = x
    obj.stu_age = y


init(stu1_obj, "mophia", 18)
print("stu1_obj", stu1_obj.__dict__)
