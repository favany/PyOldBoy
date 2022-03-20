print('模块foo==>')

x=1

def get():
    print(x)

def change():
    global x
    x=0

