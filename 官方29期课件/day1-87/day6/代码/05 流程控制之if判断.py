# print(1)
# print(2)
# print(3)
# if 条件:
#     代码1
#     代码2
#     代码3
# print(4)
# print(5)
'''
语法1:
if 条件:
    代码1
    代码2
    代码3

'''
# age = 60
# is_beautiful = True
# star = '水平座'
#
# if age > 16 and age < 20 and is_beautiful and star == '水平座':
#     print('我喜欢，我们在一起吧。。。')
#
# print('其他代码.............')


'''
语法2:
if 条件:
    代码1
    代码2
    代码3
else:
    代码1
    代码2
    代码3
'''

# age = 60
# is_beautiful = True
# star = '水平座'
#
# if age > 16 and age < 20 and is_beautiful and star == '水平座':
#     print('我喜欢，我们在一起吧。。。')
# else:
#     print('阿姨好，我逗你玩呢，深藏功与名')
#
# print('其他代码.............')


'''
语法3:
if 条件1:
    代码1
    代码2
    代码3
elif 条件2:
    代码1
    代码2
    代码3
elif 条件2:
    代码1
    代码2
    代码3
'''
# score=73
# if score >= 90:
#     print('优秀')
# elif score >= 80 and score < 90:
#     print('良好')
# elif score >= 70 and score < 80:
#     print('普通')

# 改进
# score = input('请输入您的成绩：') # score="18"
# score=int(score)
#
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 70:
#     print('普通')


'''
语法3:
if 条件1:
    代码1
    代码2
    代码3
elif 条件2:
    代码1
    代码2
    代码3
elif 条件2:
    代码1
    代码2
    代码3
...
else:
    代码1
    代码2
    代码3
'''
# score = input('请输入您的成绩：') # score="18"
# score=int(score)
#
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 70:
#     print('普通')
# else:
#     print('很差，小垃圾')
#
# print('=====>')


'''
if嵌套if
'''
age = 17
is_beautiful = True
star = '水平座'

if 16 < age < 20 and is_beautiful and star == '水平座':
    print('开始表白。。。。。')
    is_successful = True
    if is_successful:
        print('两个从此过上没羞没臊的生活。。。')
else:
    print('阿姨好，我逗你玩呢，深藏功与名')

print('其他代码.............')
