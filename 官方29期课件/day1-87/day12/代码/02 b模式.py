"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128


控制文件读写内容的模式
t：
    1、读写都是以字符串（unicode）为单位
    2、只能针对文本文件
    3、必须指定字符编码，即必须指定encoding参数
b：binary模式
    1、读写都是以bytes为单位
    2、可以针对所有文件
    3、一定不能指定字符编码，即一定不能指定encoding参数

总结：
1、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要手动编码与解码，所以此时t模式更为方便
2、针对非文本文件（如图片、视频、音频等）只能使用b模式
"""

# 错误演示：t模式只能读文本文件
# with open(r'爱nmlgb的爱情.mp4',mode='rt') as f:
#     f.read() # 硬盘的二进制读入内存-》t模式会将读入内存的内容进行decode解码操作


#
# with open(r'test.jpg',mode='rb',encoding='utf-8') as f:
#     res=f.read() # 硬盘的二进制读入内存—>b模式下，不做任何转换，直接读入内存
#     print(res) # bytes类型—》当成二进制
#     print(type(res))

# with open(r'd.txt',mode='rb') as f:
#     res=f.read() # utf-8的二进制
#     print(res,type(res))
#
#     print(res.decode('utf-8'))

# with open(r'd.txt',mode='rt',encoding='utf-8') as f:
#     res=f.read() # utf-8的二进制->unicode
#     print(res)


# with open(r'e.txt',mode='wb') as f:
#     f.write('你好hello'.encode('gbk'))

# with open(r'f.txt',mode='wb') as f:
#     f.write('你好hello'.encode('utf-8'))
#     f.write('哈哈哈'.encode('gbk'))


# 文件拷贝工具
src_file=input('源文件路径>>: ').strip()
dst_file=input('源文件路径>>: ').strip()
with open(r'{}'.format(src_file),mode='rb') as f1,\
    open(r'{}'.format(dst_file),mode='wb') as f2:
    # res=f1.read() # 内存占用过大
    # f2.write(res)

    for line in f1:
        f2.write(line)




# 循环读取文件
# 方式一：自己控制每次读取的数据的数据量
# with open(r'test.jpg',mode='rb') as f:
#     while True:
#         res=f.read(1024) # 1024
#         if len(res) == 0:
#             break
#         print(len(res))


# 方式二：以行为单位读，当一行内容过长时会导致一次性读入内容的数据量过大
# with open(r'g.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         print(len(line),line)

# with open(r'g.txt',mode='rb') as f:
#     for line in f:
#         print(line)

# with open(r'test.jpg',mode='rb') as f:
#     for line in f:
#         print(line)







