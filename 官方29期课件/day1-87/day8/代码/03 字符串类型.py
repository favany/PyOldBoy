# 1、作用
# 2、定义
# msg='hello' # msg=str('msg')
# print(type(msg))

# 3、类型转换
# str可以把任意其他类型都转成字符串
# res=str({'a':1})
# print(res,type(res))

# 4、使用：内置方法
# 4.1 优先掌握
# 4.1.1、按索引取值(正向取+反向取) ：只能取
msg='hello world'
# 正向取
# print(msg[0])
# print(msg[5])
# 反向取
# print(msg[-1])

# 只能取
# msg[0]='H'


# 4.1.2、切片:索引的拓展应用，从一个大字符串中拷贝出一个子字符串
msg='hello world'
# 顾头不顾尾
# res=msg[0:5] #x
# print(res)
# print(msg)

# 步长
# res=msg[0:5:2] # 0 2 4
# print(res) # hlo

# 反向步长(了解)
# res=msg[5:0:-1]
# print(res) #" olle"

msg='hello world'
# res=msg[:] # res=msg[0:11]
# print(res)

# res=msg[::-1] # 把字符串倒过来
# print(res)

# 4.1.3、长度len
# msg='hello world'
# print(len(msg))

# 4.1.4、成员运算in和not in
# 判断一个子字符串是否存在于一个大字符串中
# print("alex" in "alex is sb")
# print("alex" not in "alex is sb")
# print(not "alex" in "alex is sb") # 不推荐使用

# 4.1.5、移除字符串左右两侧的符号strip
# 默认去掉的空格
# msg='      egon      '
# res=msg.strip()
# print(msg) # 不会改变原值
# print(res) # 是产生了新值

# 默认去掉的空格
# msg='****egon****'
# print(msg.strip('*'))

# 了解：strip只取两边，不去中间
# msg='****e*****gon****'
# print(msg.strip('*'))

# msg='**/*=-**egon**-=()**'
# print(msg.strip('*/-=()'))

# 应用
# inp_user=input('your name>>: ').strip() # inp_user=" egon"
# inp_pwd=input('your password>>: ').strip()
# if inp_user == 'egon' and inp_pwd == '123':
#     print('登录成功')
# else:
#     print('账号密码错误')


# 4.1.6、切分split：把一个字符串按照某种分隔符进行切分，得到一个列表
# # 默认分隔符是空格
# info='egon 18 male'
# res=info.split()
# print(res)

# # 指定分隔符
# info='egon:18:male'
# res=info.split(':')
# print(res)

# 指定分隔次数(了解)
# info='egon:18:male'
# res=info.split(':',1)
# print(res)

# 4.1.7、循环
# info='egon:18:male'
# for x in info:
#     print(x)


# 4.2 需要掌握
#4.2.1、strip,lstrip,rstrip
# msg='***egon****'
# print(msg.strip('*'))
# print(msg.lstrip('*'))
# print(msg.rstrip('*'))

#4.2.2、lower,upper
# msg='AbbbCCCC'
# print(msg.lower())
# print(msg.upper())

#4.2.3、startswith,endswith
# print("alex is sb".startswith("alex"))
# print("alex is sb".endswith('sb'))

#4.2.4、format

#4.2.5、split,rsplit:将字符串切成列表
# info="egon:18:male"
# print(info.split(':',1)) # ["egon","18:male"]
# print(info.rsplit(':',1)) # ["egon:18","male"]

#4.2.6、join: 把列表拼接成字符串
# l=['egon', '18', 'male']
# res=l[0]+":"+l[1]+":"+l[2]
# res=":".join(l) # 按照某个分隔符号，把元素全为字符串的列表拼接成一个大字符串
# print(res)

# l=[1,"2",'aaa']
# ":".join(l)

#4.2.7、replace
# msg="you can you up no can no bb"
# print(msg.replace("you","YOU",))
# print(msg.replace("you","YOU",1))

#4.2.8、isdigit
# 判断字符串是否由纯数字组成
# print('123'.isdigit())
# print('12.3'.isdigit())

# age=input('请输入你的年龄：').strip()
# if age.isdigit():
#     age=int(age) # int("abbab")
#     if age > 18:
#         print('猜大了')
#     elif age < 18:
#         print('猜小了')
#     else:
#         print('才最了')
# else:
#     print('必须输入数字，傻子')

# 4.3了解
#4.3.1、find,rfind,index,rindex,count
msg='hello egon hahaha'
# 找到返回起始索引
# print(msg.find('e')) # 返回要查找的字符串在大字符串中的起始索引
# print(msg.find('egon'))
# print(msg.index('e'))
# print(msg.index('egon'))
# 找不到
# print(msg.find('xxx')) # 返回-1，代表找不到
# print(msg.index('xxx')) # 抛出异常

# msg='hello egon hahaha egon、 egon'
# print(msg.count('egon'))

#4.3.2、center,ljust,rjust,zfill
# print('egon'.center(50,'*'))
# print('egon'.ljust(50,'*'))
# print('egon'.rjust(50,'*'))
# print('egon'.zfill(10))

#4.3.3、expandtabs
# msg='hello\tworld'
# print(msg.expandtabs(2)) # 设置制表符代表的空格数为2

#4.3.4、captalize,swapcase,title
# print("hello world egon".capitalize())
# print("Hello WorLd EGon".swapcase())
# print("hello world egon".title())

#4.3.5、is数字系列
#4.3.6、is其他
# print('abc'.islower())
# print('ABC'.isupper())
# print('Hello World'.istitle())
# print('123123aadsf'.isalnum()) # 字符串由字母或数字组成结果为True
# print('ad'.isalpha()) # 字符串由由字母组成结果为True
# print('     '.isspace()) # 字符串由空格组成结果为True
# print('print'.isidentifier())
# print('age_of_egon'.isidentifier())
# print('1age_of_egon'.isidentifier())


num1=b'4' #bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3='四' #中文数字
num4='Ⅳ' #罗马数字

# isdigit只能识别：num1、num2
# print(num1.isdigit()) # True
# print(num2.isdigit()) # True
# print(num3.isdigit()) # False
# print(num4.isdigit()) # False



# isnumberic可以识别：num2、num3、num4
# print(num2.isnumeric()) # True
# print(num3.isnumeric()) # True
# print(num4.isnumeric()) # True

# isdecimal只能识别：num2
print(num2.isdecimal()) # True
print(num3.isdecimal()) # False
print(num4.isdecimal()) # False








