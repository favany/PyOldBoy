import sys

# python3.8 run.py 1 2 3
# sys.argv获取的是解释器后参数值
# print(sys.argv)

# src_file=input('源文件路径: ').strip()
# dst_file=input('目标文件路径: ').strip()
#
# src_file=sys.argv[1]
# dst_file=sys.argv[2]
# # 判断
#
# with open(r'%s' %src_file,mode='rb') as read_f,\
#     open(r'%s' %dst_file,mode='wb') as write_f:
#     for line in read_f:
#         write_f.write(line)

# python3.8 run.py src_file dst_file


# print('[%-50s]' %'#')
# print('[%-50s]' %'##')
# print('[%-50s]' %'###')



# import time
#
# res=''
# for i in range(50):
#     res+='#'
#     time.sleep(0.5)
#     print('\r[%-50s]' % res,end='')


import time


def progress(percent):
    if percent > 1:
        percent = 1
    res = int(50 * percent) * '#'
    print('\r[%-50s] %d%%' % (res, int(100 * percent)), end='')

recv_size=0
total_size=1025011

while recv_size < total_size:
    time.sleep(0.01) # 下载了1024个字节的数据

    recv_size+=1024 # recv_size=2048

    # 打印进度条
    # print(recv_size)
    percent = recv_size / total_size  # 1024 / 333333
    progress(percent)













