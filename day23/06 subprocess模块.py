# @File      : 06 subprocess模块
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/4 11:04 AM
# @Info      : 子进程

import subprocess

obj = subprocess.Popen('echo 123; ls /; ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

res = obj.stdout.read()
print(res.decode('utf-8'))  # 系统的编码

err_res = obj.stderr.read()
print(err_res.decode('utf-8'))  # 系统的编码
