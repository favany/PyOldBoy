"""
@File      : 02 yield 表达式
@Author    : 刘俊 mophia
@Email     : faaa@live.com
@Time      : 2022/6/30 12:18 AM
"""

# x = yield 返回值

def dog(name):
    food_list = []
    print('道哥 🐶 %s准备吃东西啦' % name)
    while True:
        # x 拿到的是 yield 接收到的值
        x = yield None # x = yield food_list
        print('道哥 🐶 %s 吃了 %s' % (name, x))


g = dog('alex')  # 道哥 🐶 alex准备吃东西啦
res = next(g)  # None
print(res)

g.send('一根🦴')  # 道哥 🐶 alex 吃了 一根🦴
g.send('肉包子')  # 道哥 🐶 alex 吃了 肉包子
g.send('一只老鼠🐭')  # 道哥 🐶 alex 吃了 一只老鼠🐭

g.close()

# g.send('111') # 关闭之后无法传值


