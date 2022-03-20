class Student:
    school = 'Oldboy'

    # 该方法会在对象产生之后自动执行，专门为对象进行初始化操作，可以有任意代码，但一定不能返回非None的值

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def choose(self):
        print('%s is choosing a course' % self.name)


stu1 = Student('李建刚', '男', 28)
stu2 = Student('王大力', '女', 18)

# 1、类中的数据属性
# print(id(Student.school))
# print(id(stu1.school))
# print(id(stu2.school))

# Student.school=1111111
# stu1.school=1111111
# print(stu1.school)
# print(stu2.school)

# 2、类中的函数属性
# print(Student.choose)
# Student.choose(stu1) # 类可以用，但就是一个普通函数
stu1.choose()
stu2.choose()

# print(Student.__dict__)
# print(stu1.__dict__)
# print(stu2.__dict__)

# Student.xxx=1
# print(Student.xxx)
# stu1.age=20
# stu1.yyy=30

# print(stu1.xxx)
# stu1.xxx=3333333333
# print(stu1.__dict__)
# print(stu1.xxx)
# print(stu2.xxx)

l=[] # l=list([])
print(type(l))

print(type(stu1))