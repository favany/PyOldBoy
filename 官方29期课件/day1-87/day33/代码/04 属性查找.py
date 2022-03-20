"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 属性查找的原则：对象-》类-》父类
# 切记：父类 不是 元类

class Mymeta(type):
    n=444

    def __call__(self, *args, **kwargs): #self=<class '__main__.StanfordTeacher'>
        obj=self.__new__(self) # StanfordTeacher.__new__
        # obj=object.__new__(self)
        print(self.__new__ is object.__new__) #True
        self.__init__(obj,*args,**kwargs)
        return obj

class Bar(object):
    # n=333

    # def __new__(cls, *args, **kwargs):
    #     print('Bar.__new__')
    pass

class Foo(Bar):
    # n=222

    # def __new__(cls, *args, **kwargs):
    #     print('Foo.__new__')
    pass

class StanfordTeacher(Foo,metaclass=Mymeta):
    # n=111

    def __init__(self,name,age):
        self.name=name
        self.age=age


obj=StanfordTeacher('lili',18)
print(obj.__dict__)
# print(obj.n)
# print(StanfordTeacher.n)

