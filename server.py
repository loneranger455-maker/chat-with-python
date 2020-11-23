import socket,threading
import csv
ip=socket.gethostname()
port=5151
addr=(ip,port)
socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket1.bind(addr)
list1=list()
def broadcast(encodedmsg,data):
    for i in list1:
        if i!=data:
            i.send(encodedmsg)
        
    
def clienthandle(data,addr,name):
    print("device connected: "+str(addr))
    connected=True
    while connected: 
         try:
             msg=data.recv(1024)
             msg.decode("utf-8")
         except:
             msg.decode("utf-8")=="##disconnect"
         if msg.decode("utf-8")=="##disconnect":
             connected=False
             list1.remove(data)
             print(str(addr)+" disconnected")
             return
         msg2=name+":"+msg.decode("utf-8")
         broadcast(msg2.encode("utf-8"),data)
    
   

print("server started...")
while True:
    socket1.listen()
    data,addr=socket1.accept()
    list1.append(data)
    msg=data.recv(1024)
    input1=msg.decode("utf-8")
    print(len(list1))
    try:
        thread1=threading.Thread(target=clienthandle,args=(data,addr,input1))
        thread1.start()
    except:
        continue

    

