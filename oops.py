from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


class Mainframe:
    
    def coustomcan(self,frameno,w,h,color,xc,yc):
        self.canvas=Canvas(frameno,width=w,height=h,bg=color,bd=0,highlightthickness=0)
        self.canvas.place(x=xc,y=yc)
        return self.canvas

    def image(self,path,x,y):
        self.img=PhotoImage(file=path)
        self.pic=self.canvas.create_image(x,y,image=self.img,anchor=NW)
        return self.pic

    def createtextoncanvas(self,x,y,name,fonts,*args):
        k=args
        if k==():
            self.canvas.create_text(x,y,text=name,font=fonts)
        else:
            self.canvas.create_text(x,y,text=name,font=fonts,fill=k)

    
    def coustomframe(self,frameno,w,h,color,xc,yc):
        self.f=Frame(frameno,width=w,height=h,bg=color)
        self.f.place(x=xc,y=yc)
        return self.f

    def packedframe(self,frameno,w,h,color,side,fill):
        self.f1=Frame(frameno,width=w,height=h,bg=color)
        self.f1.pack(side=side,fill=fill)
        return self.f1
 
    def combo(self,frameno,v,xc,yc):
        self.i=StringVar()
        self.coustomcombo=Combobox(frameno,values=v,textvariable=self.i)
        self.coustomcombo.place(x=xc,y=yc)

    def labels(self,frameno,name,w,h,color,xc,yc):
        self.l=Label(frameno,text=name,width=w,height=h,bg=color)
        self.l.place(x=xc,y=yc)

    def packedlabels(self,frameno,name,w,h,color,*args):
        k=args
        self.l1=Label(frameno,text=name,width=w,height=h,bg=color)
        if k==():
            self.l1.pack()
        else:
            side=k[0]
            fill=k[1]
            self.l1.pack(side=side,fill=fill)
        return self.l1
    
    def userentry(self,frameno,xc,yc,*args):
        k=args
        if k !=():
            self.en=Entry(frameno,width=k)
        else:
            self.en=Entry(frameno)
        self.en.place(x=xc,y=yc)


    def buttons_and_commands(self,frameno,name,task,xc,yc,*args):
        k=args
        if k==():
            self.b=Button(frameno,text=name,command=task)
        elif len(k)==1:
            w=k[0]
            self.b=Button(frameno,text=name,command=task,width=w)
        elif len(k)==2:
            w=k[0]
            h=k[1]
            self.b=Button(frameno,text=name,command=task,width=w,height=h)
        elif len(k)==3:
            w=k[0]
            h=k[1]
            color=k[2]
            self.b=Button(frameno,text=name,command=task,width=w,height=h,bg=color)
        elif len(k)==4:
            w=k[0]
            h=k[1]
            color=k[2]
            fg=k[3]
            self.b=Button(frameno,text=name,command=task,width=w,height=h,bg=color,fg=fg)
        else:
            w=k[0]
            h=k[1]
            color=k[2]
            fg=k[3]
            fonts=k[4]
            self.b=Button(frameno,text=name,command=task,width=w,height=h,bg=color,fg=fg,font=fonts)

        self.b.place(x=xc,y=yc)
        return self.b
    
    def passwordentry(self,frameno,xc,yc,*args):
        k=args
        if k==():
            self.enterpassword=Entry(frameno,show='*')
        else:
            w=k
            self.enterpassword=Entry(frameno,show='*',width=w)
        self.enterpassword.place(x=xc,y=yc) 
        return self.enterpassword.get()    


    # returning data entered by user
    
    def getentry(self):
        self.data1=self.en.get()
        return self.data1
    
    def getcombodata(self):
        self.data2=self.i.get()
        return self.data2

    def getpassworden(self):
        self.datapass=self.enterpassword.get()
        return self.datapass

    def clear(self):
        self.en.delete(0,END)
        # self.enterpassword.delete(0,END)

          
