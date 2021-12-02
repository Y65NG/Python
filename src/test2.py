def receiveMessage():
    global s

    while True:
        global addr
        data,addr=s.recvfrom(1024)
        data=data.decode('utf-8')
        a=data.split("|")
        if not data:
            print("client has exited!")
            break
        elif a[0]=='join': #连接服务器请求
            print('client 连接服务器!')
            label1["text"]='client连接服务器成功,请你走棋!'
        elif a[0]=='exit':
            print('client 对方退出!')
            label1["text"]='client对方退出,游戏结束!'
        elif a[0]=='over':
            print('对方赢信息!')
            label1["text"]=data.split("|")[0]
            showinfo(title="提示",message=data.split("|")[1])
        elif a[0]=='move':
            print('received:',data,'from',addr)
            p=a[1].split(",")
            x=int(p[0])
            y=int(p[1])
            print(p[0],p[1])
            label1["text"]="客户端走的位置"+p[0]+p[1]
            drawOtherChess(x,y)
        s.close()


def receiveMessage(): #接受消息

global s

while True:

data = s.recv(1024).decode('utf-8')

a = data.split("|")

if not data:

print('server has exited!')

break

elif a[0] == 'exit':

print('对方退出!')

lanel1["text"] = '对方退出!游戏结束!'

elif a[0] == 'over':

print('对方赢信息!')

label1["text"] = data.split("|")[0]

showinfo(title="提示", message=data.split("|")[1])

elif a[0] == 'move':

print('received:', data)

p = a[1].split(",")

x = int(p[0])

y = int(p[1])

print(p[0], p[1])

label1["text"] = "服务器走的位置" + p[0] + p[1]

drawOtherChess(x,y)

s.close()