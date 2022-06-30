"""
@Time    : 2022/6/30 10:30
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 00 复习.py
"""

def add():
    count = 0
    while True:
        count += 1
        yield count

g = add()

# list(g)