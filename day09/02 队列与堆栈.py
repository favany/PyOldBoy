# @File      : 02 队列与堆栈
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/7 3:36 PM
# @Info      :

# 队列： first in first out FIFO 先进先出
l = []

# 入队操作
l.append('first')
l.append('second')
l.append('third')

# 出队操作
print(l.pop(0))
print(l.pop(0))
print(l.pop(0))

# 堆栈： LIFO，后进先出
l = []

# 入栈操作
l.append('first')
l.append('second')
l.append('third')

# 出栈操作
print(l.pop())
print(l.pop())
print(l.pop())
