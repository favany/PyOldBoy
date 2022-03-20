# 学生的数据
stu_name='egon'
stu_age=18
stu_gender='male'

# 学生的功能
def tell_stu_info():
    print('学生信息：名字：%s 年龄：%s 性别：%s' %(stu_name,stu_age,stu_gender))

def set_info(x,y,z):
    stu_name=x
    stu_age=y
    stu_gender=z