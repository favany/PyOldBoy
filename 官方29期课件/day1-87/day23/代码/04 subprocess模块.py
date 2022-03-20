"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

import subprocess

obj=subprocess.Popen('echo 123 ; ls / ; ls /root',shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 )

# print(obj)
# res=obj.stdout.read()
# print(res.decode('utf-8'))

err_res=obj.stderr.read()
print(err_res.decode('utf-8'))