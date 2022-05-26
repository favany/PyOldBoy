# @File      : 06 __init__方法
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/5/26 5:54 PM
# @Info      :

# 解决方案二

# 调用类的过程又称为实例化，发生了三件事
# 1. 先生成一个空对象
# 2. python 会自动调用类中的 __init__ 方法，然后将调用类时括号内传入的参数，一同传给 __init__
# 3. 返回初始化完的对象

class Student:
    stu_school = 'old boy'

    def __init__(self, x, y):
        self.stu_name = x
        self.stu_age = y

    # 2. 功能的定义
    def tell_stu_info(self, stu_obj):
        print("学生信息：名字：%s 年龄：%s " % (
            stu_obj["stu_name"],
            stu_obj["age"],
        ))

    def set_info(self, stu_obj, x, y, z):
        pass

stu1 = Student("mophia", 18)

print(stu1.__dict__)

# 总结：__init__ 方法
# 1. 会在调用类时，自动触发执行，用来为对象初始化自己独有的数据
# 2. __init__ 内应该存放是为对象初始化属性的功能，是可以存放任意其他代码的，想要在类调用时立刻执行的代码，就可以放在该方法内。
# 3. __init__ 必须返回 None
