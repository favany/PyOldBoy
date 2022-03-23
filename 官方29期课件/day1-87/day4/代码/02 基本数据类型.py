# 1、数字类型
# 1.1 整型int
# 作用：记录年龄、身份证号、个数等等
# 定义：
age = 18
# print(type(age))

# 浮点型float
# 作用：记录薪资、身高、体重
# 定义
salary = 3.3
height = 1.87
weight = 70.3
# print(type(height))

# 数字类型的其他使用
# level = 1
# level=level + 1
# print(level)
# print(10 *3)

# print(10 + 3.3) # int与float之间可以相加
# age = 19
# print(age > 18)


# 2、字符串类型str
# 作用：记录描述性质的状态，名字、一段话
# 定义：用引号（''，""，''' '''，""" """，）包含的一串字符
info = '''
天下只有两种人。比如一串葡萄到手，一种人挑最好的先吃，
另一种人把最好的留到最后吃。
照例第一种人应该乐观，因为他每吃一颗都是吃剩的葡萄里最好的；
第二种人应该悲观，因为他每吃一颗都是吃剩的葡萄里最坏的。
不过事实却适得其反，缘故是第二种人还有希望，第一种人只有回忆。
'''
# print(type(info))
# name="egon"
# print(name)

# x=18
# print(type(x))
# x='18' # 由数字组成的字符串，是字符串类型，不是int类型
# print(type(x))

# 'name'='egon' # 语法错误，等号左边是变量名，变量名的命名不能有引号

# xxx # 代表访问变量名字
'xxx'  # 代表的是值

# x=10
# y=x

# 其他使用：
# 字符串的嵌套，注意：外层用单引号，内存应该用双引号，反之亦然
# print("my name is 'egon'")
# print('my name is \'egon\'')

# 字符串之间可以相加，但仅限于str与str之间进行，
# 代表字符串的拼接，了解即可，不推荐使用，因为str之间的
# 相加效率极低
# print('my name is '+'egon')
# print('='*20)
# print('hello world')
# print('='*20)


# 3、列表：索引对应值，索引从0开始，0代表第一个
# 作用：按位置记录多个值（同一个人的多个爱好、同一个班级的所有学校姓名、同一个人12个月的薪资），并且可以按照索引取指定位置的值

# 定义：在[]内用逗号分隔开多个任意类型的值,一个值称之为一个元素
#  0   1    2        3          4
l = [10, 3.1, 'aaa', ['bbb', 'ccc'], 'ddd']
# print(l)
# print(l[1])
# print(l[2])
# print(l[3][1])

# print(l[4])
# print(l[-1])

# hobbies='read music play'
# print(hobbies)
# hobbies = ['read', 'music', 'play']
# print(hobbies[1])

# 其他的用途：
# students_info=[
#     ['tony',18,['jack',]],
#     ['jason',18,['play','sleep']]
# ]
# 取出第一个学生的第一个爱好
# print(students_info[0][2][0])


# 4、
# 索引反映的是顺序、位置，对值没有描述性的功能
#      0      1   2     3
info=['egon',18,'male',19]
# print(type(info))
# print(info[0])
# print(info[1])
# print(info[2])

# 字典类型：key对应值，其中key通常为字符串类型，所以key对值可以有描述性的功能
# 作用：用来存多个值，每个值都有唯一一个key与其对应，key对值有描述性功能
# 定义：在{}内用逗号分开各多个key：value
# d={'a':1,'b':2}
# print(type(d))
# print(d['a'])

# info={
#     "name":'egon',
#     "age":18,
#     "gender":'male',
#     "salary":19
# }
# print(info["salary"])

# 其他用途：
# students_info=[
#     第1个信息,
#     第2个信息,
#     第3个信息,
# ]

students_info=[
    {"name":'egon1','age1':19,'gender':'male'},
    {"name":'egon2','age1':19,'gender':'male'},
    {"name":'egon3','age1':19,'gender':'male'},
]

print(students_info[1]['gender'])


# 5 布尔bool
# 6.1 作用
# 用来记录真假这两种状态
#
# 6.2 定义
# is_ok = True
# is_ok = False
# print(type(is_ok))

# x=1
# y=0

# students=[
#     {'name':'egon','gender':'male'},
#     {'name':'alex','gender':'female'},
# ]

# students=[
#     {'name':'egon','gender':True},
#     {'name':'alex','gender':False},
# ]

students=[
    {'name':'egon','gender':1},
    {'name':'alex','gender':0},
]

# 6.3 其他使用
# 通常用来当作判断的条件，我们将在if判断中用到它



# 总结：如何选择合适的类型来记录状态
# 1、选取的类型是否可以明确标识事物的状态
# 2、存不是目的，存的目的是为了日后取出来用，并且方便的用
# 3、把自己想象成一台计算机，如果我是计算机，
#    我会如何以何种形式把事物的状态记到脑子里
#    然后再去python中找相应的数据类型来让计算机像自己一样去记下事物的状态