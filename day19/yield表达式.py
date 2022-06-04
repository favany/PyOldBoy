# x = yield 返回值

def dog(name):
  print("道哥%s准备吃东西啦" % name)
  while True:
    # x 拿到的是 yield 接收到的值
    x = yield # x = "一根骨头"
    print("道哥%s吃了 %s"%(name, x))

g = dog("alex")
g.send("一根骨头")

vooce.net
