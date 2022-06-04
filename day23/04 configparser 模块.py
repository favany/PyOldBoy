# @File      : 06 configparser 模块
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/2 10:40 AM
# @Info      :

# 加载某种特定格式的配置文件格式

import configparser

config = configparser.ConfigParser()
config.read('test.ini')

# 1. 获取 sections
print(config.sections())
# ['section1', 'section2']

# 2. 获取某一个 section 下的所有 options
print(config.options('section1'))
# ['k1', 'k2', 'user', 'age', 'is_admin', 'asalary']

# 3. 获取 items
print(config.items('section1'))

# 4. 获取指定 section 中的某个 option
re = config.get('section1', 'user')
print(re, type(re))

# 5. 获取 int
re = config.getint('section1', 'age')
print(re)

# 6. 获取 boolean
re = config.getboolean('section1', 'is')



