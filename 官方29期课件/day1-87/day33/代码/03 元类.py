"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
#一：引入：
# 一切都源自于一句话：一切皆为对象

#二：什么是元类？
# 元类就是用来实例化产生类的类
# 关系：元类---实例化---->类（People）---实例化---->对象（obj）
# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say(self):
#         print('%s:%s' %(self.name,self.name))
#
#
# print(People.__dict__)
# 如何得到对象
# obj=调用类()
# obj=People('egon',18)
# print(type(obj))
# 如果说类也是对象
# People=调用类(。。。)

# 查看内置的元类：
# 1、type是内置的元类
# 2、我们用class关键字定义的所有的类以及内置的类都是由元类type实例化产生
# print(type(People))
# print(type(int))

# 三：class关键字创造类People的步骤
# 类有三大特征：
# # 1、类名
# class_name="People"
# # 2、类的基类
# class_bases=(object,)
# # 3、执行类体代码拿到类的名称空间
# class_dic={}
# class_body="""
# def __init__(self,name,age):
#     self.name=name
#     self.age=age
#
# def say(self):
#     print('%s:%s' %(self.name,self.name))
# """
# exec(class_body,{},class_dic)
# # print(class_dic)
#
# # 4、调用元类
# People=type(class_name,class_bases,class_dic)

# 四：如何自定义元类来控制类的产生
# class Mymeta(type): # 只有继承了type类的类才是元类
#     #            空对象,"People",(),{...}
#     def __init__(self,x,y,z):
#         print('run22222222222....')
#         print(self)
#         # print(x)
#         # print(y)
#         # print(z)
#         # print(y)
#         # if not x.istitle():
#         #     raise NameError('类名的首字母必须大写啊！！！')
#
#     #          当前所在的类，调用类时所传入的参数
#     def __new__(cls, *args, **kwargs):
#         # 造Mymeta的对象
#         print('run1111111111.....')
#         # print(cls,args,kwargs)
#         # return super().__new__(cls,*args, **kwargs)
#         return type.__new__(cls,*args, **kwargs)
#
#
# # People=Mymeta("People",(object,),{...})
# # 调用Mymeta发生三件事，调用Mymeta就是type.__call__
# # 1、先造一个空对象=>People,调用Mymeta类内的__new__方法
# # 2、调用Mymeta这个类内的__init__方法，完成初始化对象的操作
# # 3、返回初始化好的对象
#
# class People(metaclass=Mymeta):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say(self):
#         print('%s:%s' %(self.name,self.name))
#
# # 强调：
# # 只要是调用类，那么会一次调用
# # 1、类内的__new__
# # 2、类内的__init__


# 五：__call__
# class Foo:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#     #            obj,1,2,3,a=4,b=5,c=6
#     def __call__(self,*args,**kwargs):
#         print('===>',args,kwargs)
#         return 123
#
# obj=Foo(111,222)
# # print(obj) # obj.__str__
# res=obj(1,2,3,a=4,b=5,c=6) # res=obj.__call__()
# print(res)

# 应用：如果想让一个对象可以加括号调用，需要在该对象的类中添加一个方法__call__
# 总结：
# 对象()->类内的__call__
# 类()->自定义元类内的__call__
# 自定义元类()->内置元类__call__


# 六：自定义元类控制类的调用=》类的对象的产生
class Mymeta(type): # 只有继承了type类的类才是元类
    def __call__(self, *args, **kwargs):
        # 1、Mymeta.__call__函数内会先调用People内的__new__
        people_obj=self.__new__(self)
        # 2、Mymeta.__call__函数内会调用People内的__init__
        self.__init__(people_obj,*args, **kwargs)

        # print('people对象的属性：',people_obj.__dict__)
        people_obj.__dict__['xxxxx']=11111
        # 3、Mymeta.__call__函数内会返回一个初始化好的对象
        return people_obj

# 类的产生
# People=Mymeta()=》type.__call__=>干了3件事
# 1、type.__call__函数内会先调用Mymeta内的__new__
# 2、type.__call__函数内会调用Mymeta内的__init__
# 3、type.__call__函数内会返回一个初始化好的对象

class People(metaclass=Mymeta):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('%s:%s' %(self.name,self.name))

    def __new__(cls, *args, **kwargs):
        # 产生真正的对象
        return object.__new__(cls)

# 类的调用
# obj=People('egon',18) =》Mymeta.__call__=》干了3件事
# 1、Mymeta.__call__函数内会先调用People内的__new__
# 2、Mymeta.__call__函数内会调用People内的__init__
# 3、Mymeta.__call__函数内会返回一个初始化好的对象

obj1=People('egon',18)
obj2=People('egon',18)
# print(obj)
print(obj1.__dict__)
print(obj2.__dict__)