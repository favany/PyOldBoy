"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# x=yield 返回值

# 一：
# def dog(name):
#     print('道哥%s准备吃东西啦...' %name)
#     while True:
#         # x拿到的是yield接收到的值
#         x = yield # x = '肉包子'
#         print('道哥%s吃了 %s' %(name,x))
#
#
# g=dog('alex')
# g.send(None) # 等同于next(g)
#
# g.send(['一根骨头','aaa'])
# # g.send('肉包子')
# # g.send('一同泔水')
# # g.close()
# # g.send('1111') # 关闭之后无法传值


# 二：
def dog(name):
    food_list=[]
    print('道哥%s准备吃东西啦...' %name)
    while True:
        # x拿到的是yield接收到的值
        x = yield food_list # x = '肉包子'
        print('道哥%s吃了 %s' %(name,x))
        food_list.append(x) # ['一根骨头','肉包子']
#
# g=dog('alex')
# res=g.send(None)  # next(g)
# print(res)
#
# res=g.send('一根骨头')
# print(res)
#
# res=g.send('肉包子')
# print(res)
# # g.send('一同泔水')




def func():
    print('start.....')
    x=yield 1111  # x='xxxxx'
    print('哈哈哈啊哈')
    print('哈哈哈啊哈')
    print('哈哈哈啊哈')
    print('哈哈哈啊哈')
    yield 22222

g=func()
res=next(g)
print(res)

res=g.send('xxxxx')
print(res)





