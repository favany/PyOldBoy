# 1、作用：按位置存放多个值
# 2、定义
# l=[1,1.2,'a'] # l=list([1,1.2,'a'])
# print(type(l))

# 3、类型转换: 但凡能够被for循环遍历的类型都可以当做参数传给list()转成列表
# res=list('hello')
# print(res)
#
# res=list({'k1':111,'k2':222,'k3':3333})
# print(res)


# 4、内置方法
# 优先掌握的操作：
# 1、按索引存取值(正向存取+反向存取)：即可以取也可以改
# l=[111,'egon','hello']
# 正向取
# print(l[0])
# 反向取
# print(l[-1])
# 可以取也可以改：索引存在则修改对应的值
# l[0]=222
# print(l)

# 无论是取值操作还是赋值操作：索引不存在则报错
# l[3]=333


# 2、切片(顾头不顾尾，步长)
l = [111, 'egon', 'hello', 'a', 'b', 'c', 'd', [1, 2, 3]]
# print(l[0:3])
# print(l[0:5:2]) # 0 2 4

# print(l[0:len(l)])
# print(l[:])
# new_l=l[:] # 切片等同于拷贝行为，而且相当于浅copy
# print(id(l))
# print(id(new_l))

# l[-1][0]=1111111
# print(l)
# print(new_l)

# print(l[::-1])

# msg1='hello:egon:<>:18[]==123'
# msg2=msg1[:]
# print(msg1,id(msg1))
# print(msg2,id(msg2))
# 3、长度
# print(len([1, 2, 3]))
# 4、成员运算in和not in
# print('aaa' in ['aaa', 1, 2])
# print(1 in ['aaa', 1, 2])
# 5、往列表中添加值
# 5.1 追加
# l=[111,'egon','hello']
# l.append(3333)
# l.append(4444)
# print(l)

# 5.2、插入值
# l=[111,'egon','hello']
# l.insert(0,'alex')
# print(l)

# 5.3、extend添加值
# new_l=[1,2,3]
# l=[111,'egon','hello']
# l.append(new_l)
# print(l)

# 代码实现
# for item in new_l:
#     l.append(item)
# print(l)

# extend实现了上述代码
# l.extend(new_l)
# l.extend('abc')
# print(l)


# 7、删除
# 方式一：通用的删除方法，只是单纯的删除、没有返回值
# l = [111, 'egon', 'hello']
# del l[1]
# x =del l[1] # 抛出异常，不支持赋值语法
# print(l)

# 方式二：l.pop()根据索引删除，会返回删除的值
# l = [111, 'egon', 'hello']
# l.pop() # 不指定索引默认删除最后一个
# l.pop()
# print(l)

# res=l.pop(1)
# print(l)

# print(res)

# 方式三：l.remove()根据元素删除，返回None
# l = [111, 'egon', [1,2,3],'hello']
# l.remove([1,2,3])
# print(l)
# res=l.remove('egon')
# print(res) # None


# 8、循环
# l=[1,'aaa','bbb']
# for x in l:
#     l.pop(1)
#     print(x)

# 需要掌握操作
l = [1, 'aaa', 'bbb','aaa','aaa']
# 1、l.count()
# print(l.count('aaa'))

# 2、l.index()
# print(l.index('aaa'))
# print(l.index('aaaaaaaaa')) # 找不到报错

# 3、l.clear()
# l.clear()
# print(l)

# 4、l.reverse():不是排序，就是将列表倒过来
# l = [1, 'egon','alex','lxx']
# l.reverse()
# print(l)

# 5、l.sort(): 列表内元素必须是同种类型才可以排序
# l=[11,-3,9,2,3.1]
# l.sort() # 默认从小到大排，称之为升序
# l.sort(reverse=True) # 从大到小排，设置为降序
# print(l)

# l=[11,'a',12]
# l.sort()

# l=['c','e','a']
# l.sort()
# print(l)

# 了解：字符串可以比大小，按照对应的位置的字符依次pk
# 字符串的大小是按照ASCI码表的先后顺序加以区别，表中排在后面的字符大于前面的
# print('a'>'b')
# print('abz'>'abcdefg')

# 了解：列表也可以比大小,原理同字符串一样,但是对应位置的元素必须是同种类型
# l1=[1,'abc','zaa']
# l2=[1,'abc','zb']
#
# print(l1 < l2)


# 补充
# 1、队列：FIFO,先进先出
# l=[]
# # 入队操作
# l.append('first')
# l.append('second')
# l.append('third')
#
# print(l)
# # 出队操作
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))

# 2、堆栈：LIFO,后进先出
l=[]
# 入栈操作
l.append('first')
l.append('second')
l.append('third')

print(l)
# 出队操作
print(l.pop())
print(l.pop())
print(l.pop())