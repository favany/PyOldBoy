"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 什么是反射？
# 指的是在程序运行过程中可以"动态（不见棺材不掉泪）"获取对象的信息

# 为何要用反射？

# 如何实现反射？
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('<%s:%s>' %(self.name,self.age))

obj=People('辣白菜同学',18)



# 实现反射机制的步骤
# 1、先通过多dir：查看出某一个对象下可以.出哪些属性来
# print(dir(obj))

# 2、可以通过字符串反射到真正的属性上，得到属性值
# print(obj.__dict__[dir(obj)[-2]])

# 四个内置函数的使用:通过字符串来操作属性值
# 1、hasattr()
# print(hasattr(obj,'name'))
# print(hasattr(obj,'x'))

# 2、getattr()
# print(getattr(obj,'name'))

# 3、setattr()
# setattr(obj,'name','EGON') # obj.name='EGON'
# print(obj.name)

# 4、delattr()
# delattr(obj,'name') # del obj.name
# print(obj.__dict__)


# res1=getattr(obj,'say') # obj.say
# res2=getattr(People,'say') # People.say
# print(res1)
# print(res2)


# obj=10
# if hasattr(obj,'x'):
#     print(getattr(10,'x'))
# else:
#     pass

# print(getattr(obj,'x',None))


# if hasattr(obj,'x'):
#     setattr(obj,'x',111111111) # 10.x=11111
# else:
#     pass


class Ftp:
    def put(self):
        print('正在执行上传功能')

    def get(self):
        print('正在执行下载功能')

    def interactive(self):
        method=input(">>>: ").strip() # method='put'

        if hasattr(self,method):
            getattr(self,method)()
        else:
            print('输入的指令不存在')


# obj=Ftp()
# obj.interactive()









