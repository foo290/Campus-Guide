from tkinter import *
from tkinter.ttk import Combobox

class Mainframe2:

    def customcan(self,framename,w,h,color,xc,yc):
        self.c1=Canvas(framename,width=w,height=h,bg=color,bd=0,highlightthickness=0)
        self.c1.place(x=xc,y=yc)
        return self.c1

    def image(self,path,x,y):
        self.pic=PhotoImage(file=path)
        self.picofcan=self.c1.create_image(x,y,image=self.pic,anchor=NW)
        return self.picofcan

    def line(self,xs,ys,xf,yf,color,w):
        self.linesoncan=self.c1.create_line(xs,ys,xf,yf,fill=color,width=w)

    def text(self,x,y,name,fonts,color):
        self.c1.create_text(x,y,text=name,font=fonts,fill=color)

    def custombuttons(self,frameno,name,w,h,action,xc,yc,**kwargs):
        kdic=kwargs
        if kdic !={}:
            self.b=Button(frameno,text=name,width=w,height=h,command=action,bg=kdic['bg'],fg=kdic['fg'])
        else:
            self.b = Button(frameno, text=name, width=w, height=h,command=action)
        self.b.place(x=xc,y=yc)
        return self.b

    def customlabels(self,frameno,name,fonts,bgc,xc,yc,*args,**kwargs):
        style=kwargs
        if style=={}:
            wh=args
            if wh==():
                self.l1=Label(frameno,text=name,font=fonts,bg=bgc)
            else:
                w=wh[0]
                h=wh[1]
                self.l1 = Label(frameno, text=name,width=w,height=h, font=fonts, bg=bgc)
        else:
            wh = args
            if wh == ():
                self.l1 = Label(frameno, text=name, font=fonts, bg=bgc,fg=style['fg'])
            else:
                w = wh[0]
                h = wh[1]
                self.l1 = Label(frameno, text=name, width=w, height=h, font=fonts, bg=bgc,fg=style['fg'])
        self.l1.place(x=xc,y=yc)
        return self.l1

    def emailentry(self,frameno,xc,yc,*args):
        em=args
        self.emailvar=StringVar()
        if em !=():
            self.emen=Entry(frameno,width=em[0],textvariable=self.emailvar)
        else:
            self.emen = Entry(frameno, textvariable=self.emailvar)
        self.emen.place(x=xc,y=yc)

    def userEntry(self,frameno,xc,yc,*args):
        t=args
        self.valname=StringVar()
        if t != ():
            self.en1=Entry(frameno,width=t[0],textvariable=self.valname)
        else:
            self.en1 = Entry(frameno,textvariable=self.valname)
        self.en1.place(x=xc,y=yc)

    def userintentry(self,frameno,xc,yc,*args):
        t2=args
        self.intvalname=StringVar()
        if t2 != ():
            self.en23=Entry(frameno,width=t2[0],textvariable=self.intvalname)
        else:
            self.en23 = Entry(frameno,textvariable=self.intvalname)
        self.en23.place(x=xc,y=yc)


    def customframes(self,frameno,w,h,color,xc,yc):
        self.f1=Frame(frameno,width=w,height=h,bg=color)
        self.f1.place(x=xc,y=yc)
        return  self.f1


    def customcombobox(self,frameno,name,v,w,xc,yc):
        self.c1=Combobox(frameno,values=v,width=w,state='readonly')
        self.c1.set(name)
        self.c1.place(x=xc,y=yc)
        return self.c1

    def passwordentry(self,frameno,xc,yc,*args):
        t = args
        if t != ():
            self.en = Entry(frameno, show='*',width=t[0])
        else:
            self.en = Entry(frameno)
        self.en.place(x=xc, y=yc)

    def packedFrame(self,frameno,w,h,color,side,**kwargs):
        adic=kwargs
        self.f1 = Frame(frameno, width=w, height=h, bg=color)
        if  adic =={}:
            self.f1.pack(side=side)
        else:
            self.f1.pack(side=side,fill=adic['fill'])
        return self.f1

    def txtarea(self,frameno,w,h,xc,yc,**kwargs):
        state=kwargs
        self.t1=Text(frameno,width=w,height=h,wrap=WORD,padx=5,pady=5)
        if state == {}:
            pass
        else:
            self.t1.config(state=state['state'])
        self.t1.place(x=xc,y=yc)
        return self.t1

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

    def genralentry(self,frameno,xc,yc,*args):
        t3 = args
        self.em = StringVar()
        if t3 != ():
            self.enem = Entry(frameno, width=t3[0], textvariable=self.em)
        else:
            self.enem = Entry(frameno, textvariable=self.em)
        self.enem.place(x=xc, y=yc)


    # Getting values of entries

    def getuserentry(self):
        self.userdata=self.valname.get().title()
        return self.userdata

    def getpassword(self):
        self.passdata=self.en.get()
        return self.passdata

    def gettext(self):
        self.txtdata=self.t1.get(1.0,END)
        return self.txtdata

    def getcombodata(self):
        self.choice=self.c1.get()
        return self.choice

    def getint(self):
        self.intdat=self.intvalname.get()
        return self.intdat

    def getgenralentrydata(self):
        self.emmeta=self.em.get()
        return self.emmeta

    def getemail(self):
        self.emdat=self.emailvar.get().endswith('@gmail.com')
        if self.emdat==True:
            return self.emen.get()
        else:
            return False

    # clearing the data

    def clearuserentry(self):
        self.en1.delete(0,END)

    def clearpassword(self):
        self.en.delete(0,END)

    def cleartext(self):
        self.t1.delete(1.0,END)

    def clearcombo(self):
        self.c1.delete(0,END)

    def ex(self):
        meta=self.c1.get()
        self.c1.bind('<<ComboboxSelected>>')
        return meta

    def cleangenral(self):
        self.enem.delete(0,END)

    def clearinten(self):
        self.en23.delete(0,END)


# setting values
    def setuserentry(self,val):
        self.valname.set(val)

    def setintegerentry(self,valofint2):
        self.intvalname.set(valofint2)

    def setgenraluser(self, valofint):
        self.em.set(valofint)

    def setemail(self,emaildata):
        self.emailvar.set(emaildata)






