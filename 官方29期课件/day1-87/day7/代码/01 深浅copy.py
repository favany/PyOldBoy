
list1=[
    'egon',
    'lxx',
    [1,2]
]

# 1、二者分隔不开，list改list2也跟着该，因为指向的就是同一个地址
# list2=list1 # 这不叫copy
# list1[0]='EGON'
# print(list2)

# 2、需求：
# 1、拷贝一下原列表产生一个新的列表
# 2、想让两个列表完全独立开，并且针对的是改操作的独立而不是读操作


# 3、如何copy列表
# 3.1 浅copy:是把原列表第一层的内存地址不加区分完全copy一份给新列表
list1=[
    'egon',
    'lxx',
    [1,2]
]

list3=list1.copy()
# print(list3)
# print(id(list1))
# print(id(list3))

# print(id(list1[0]),id(list1[1]),id(list1[2]))
# print(id(list3[0]),id(list3[1]),id(list3[2]))

# 实验1：对于不可变类型的赋值，都是产生了新值，让原列表的索引指向新的
# 内存地址，并不会影响新列表
list1[0]='EGON'
list1[1]='LXX'
# list1[2]=123

# 实验2：但对于可变类型，我们可以改变可变类型中包含的值，但内存地址不变
# 即原列表的索引指向仍然指向原来的内存地址，于是新列表也跟着一起受
# 影响，如下
# list1[2][0]=111
# list1[2][1]=222
# print(list1)
# print(list3)

# 综合实验1和实验2可以得出，要想copy得到的新列表与原列表的改操作完全独立开
# 必须有一种可以区分开可变类型与不可变类型的copy机制，这就是深copy

# 3.2 深copy
import copy
list1=[
    'egon',
    'lxx',
    [1,2]
]

list3=copy.deepcopy(list1)
# print(id(list1))
# print(id(list3))
# print(list3)

#          不可变        不可变        可变
# print(id(list1[0]),id(list1[1]),id(list1[2]))
# print(id(list3[0]),id(list3[1]),id(list3[2]))
'''
4497919088 4498367856 4498449216
4497919088 4498367856 4498595328
'''
# print(list3)
# print(id(list1[2][0]),id(list1[2][1]))
# print(id(list3[2][0]),id(list3[2][1]))

list1[0]='EGON'
list1[1]='LXX'

list1[2][0]=111
list1[2][1]=222
# print(list1)

print(list3)