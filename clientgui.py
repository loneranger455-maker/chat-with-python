import socket,threading
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x500")
ip=socket.gethostname()
port=5151
addr=(ip,port)
listmsg=list()
socket1=" "


class client():
    def pujan(self):
        self.check=True
        self.frame1=Frame(root,height=300,width=500,bg="pink")
        self.frame1.pack(pady=80)
        Label(self.frame1,text="Enter your name to be displayed:",font=("Georgia",20,"bold")).pack(pady=20)
        self.en=Entry(self.frame1,width=20,font=("Georgia",18,"bold"))
        self.en.pack(pady=20)
        Button(self.frame1,text="connect",width=30,command=lambda:self.message()).pack(pady=50)
       
    
    def message(self):
        global socket1
        if len(self.en.get())==0:
            messagebox.showerror("error","please enter your name first")
            self.frame1.destroy()
            self.pujan()
        else:
            try:
               socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
               socket1.connect(addr)
               self.message1()
            except:
                 self.check=True
                 messagebox.showerror("Error","Cannot connect to the server!! \nmake sure the server is running")
                 self.frame1.destroy()
                 self.pujan()
                 
    def send(self):
        inputmsg=self.en1.get()
        self.en1.delete(0,'end')
        socket1.send(inputmsg.encode("utf-8"))
        self.scroll.insert(END,"you:"+inputmsg)
    def th1(self):
        while self.check:
           msg=socket1.recv(1024)
           self.scroll.insert(END,msg.decode("utf-8"))                                                                                             
    def disconnect(self):
        global socket1
        socket1.send("##disconnect".encode("utf-8"))
        self.frame2.destroy()
        self.check=False
        socket1.close()

        self.pujan()

    def close(self):
        global socket1
        socket1.send("##disconnect".encode("utf-8"))
        quit()
    def th2(self):
        while self.check:
             self.scroll.yview_moveto('1.0')
       
    def message1(self):
        socket1.send(self.en.get().encode("utf-8"))
        self.frame1.destroy()
        self.frame2=Frame(root,height=300,width=500,bg="pink")
        self.frame2.pack(pady=80)
        self.scroll=Listbox(self.frame2,width=30,fg="blue",height=10,font=("Georgia",15,"bold"))
        self.scroll.pack()
        self.scroll.insert(0,"            Hello everyone Enjoy chatting  ")
        
        scr=Scrollbar(self.frame2)
        scr.pack(side=RIGHT, fill=Y)
        self.scroll.config(yscrollcommand = scr.set) 
        scr.config(command = self.scroll.yview) 
        th2=threading.Thread(target=self.th2)
        th2.start()
        self.en1=Entry(self.frame2,width=20,font=("Georgia",18,"bold"))
        self.en1.pack(pady=10)
        Button(self.frame2,text="Send",width=5,command=lambda:self.send()).pack(side=LEFT)
        Button(self.frame2,text="Disconnect",width=5,command=lambda:self.disconnect()).pack(side=LEFT,padx=30)
        Button(self.frame2,text="Exit",width=5,command=lambda:self.close()).pack(side=LEFT,padx=30)
        self.thread1=threading.Thread(target=self.th1)
        self.thread1.start()
    def __init__(self):
        self.pujan()
ak=client()
root.mainloop()