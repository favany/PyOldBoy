"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

#            str  int   ('play','music')
# def register(name:str,age:int,hobbbies:tuple)->int:
#  print(name)
#  print(age)
#  print(hobbbies)
#  return 111
#
# # register(1,'aaa',[1,])
# res=register('egon',18,('play','music'))



# def register(name:str='egon',age:int=18,hobbbies:tuple=(1,2))->int:
#  print(name)
#  print(age)
#  print(hobbbies)
#  return 111
#
# # register(1,'aaa',[1,])
# # res=register('egon',18,('play','music'))
# res=register()


def register(name:"必须传入名字傻叉",age:1111111,hobbbies:"必须传入爱好元组")->"返回的是整型":
 print(name)
 print(age)
 print(hobbbies)
 return 111

# register(1,'aaa',[1,])
# res=register('egon',18,('play','music'))
# res=register('egon',19,(1,2,3))

print(register.__annotations__)



