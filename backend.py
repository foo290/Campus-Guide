from oops2 import Mainframe2
from tkinter import *
from tkinter import messagebox,filedialog
from database import *
from info import *
import os
from PIL import Image
from tkcalendar import Calendar


dp_max_size=(150,150)

logged_user=['root']
validationstudent={}
validationfaculty={}
validateadmin={}
existing_user=[]

def rectanglefade(root,time,name,xnc,ync,**kwargs):

    width = 300
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = 250
    globalobj=Mainframe2()
    cd=kwargs
    if cd=={}:
        holdercan=globalobj.customcan(root,300,200,'white',x,y)

    else:
        x1=cd['x']
        y1=cd['y']
        holdercan=globalobj.customcan(root,300,200,'white',x1,y1)
    holdercan.config(highlightbackground='black',highlightthickness=0)

    # globalobj.customlabels(holdercan, 'Loading...', 'none 7', 'white', 105, 95)
    holdercan.create_text(xnc,ync,text=name)


    c1=holdercan.create_rectangle(100,90,200,110,width=5,outline='red')
    c2=holdercan.create_rectangle(90,80,210,120,width=5,outline='green')
    c3=holdercan.create_rectangle(80,70,220,130,width=5,outline='steelblue')
    c4=holdercan.create_rectangle(70,60,230,140,width=5,outline='black')

    def fadered():
        c1 = holdercan.create_rectangle(100, 90, 200, 110, width=5, outline='white')
    def fadegreen():
        c2 = holdercan.create_rectangle(90, 80, 210, 120, width=5, outline='white')
    def fadesteelblue():
        c3 = holdercan.create_rectangle(80, 70, 220, 130, width=5, outline='white')
    def fadeblack():
        c4 = holdercan.create_rectangle(70, 60, 230, 140, width=5, outline='white')


    def createred():
        c1 = holdercan.create_rectangle(100, 90, 200, 110, width=5, outline='red')
    def creategreen():
        c2 = holdercan.create_rectangle(90, 80, 210, 120, width=5, outline='green')
    def createsteelblue():
        c3 = holdercan.create_rectangle(80, 70, 220, 130, width=5, outline='steelblue')
    def createblack():
        c4 = holdercan.create_rectangle(70, 60, 230, 140, width=5, outline='black')


    def changefade():
        holdercan.after(100,fadered)
        holdercan.after(250,fadegreen)
        holdercan.after(350,fadesteelblue)
        holdercan.after(450,fadeblack)
        holdercan.after(450,createfade)
    def createfade():
        holdercan.after(450,createred)
        holdercan.after(550,creategreen)
        holdercan.after(650,createsteelblue)
        holdercan.after(750,createblack)
        holdercan.after(850,changefade)


    changefade()

    holdercan.after(time,holdercan.destroy)

def can_but(frno,name,clr,hlclr,fg,xc,yc,fun,w,h,txtalignX):
    fonttxt='Ebrima'

    globalobj=Mainframe2()
    projectbut = globalobj.customcan(frno, w, h,clr, xc, yc)
    projectbut.config(highlightthickness=0, highlightbackground=hlclr, cursor='hand2')
    projectbut.create_text(txtalignX, 15, text=name, font=f'{fonttxt} 12', fill=fg)

    projectbut.bind('<Enter>', lambda event: projectbut.config(highlightthickness=1))
    projectbut.bind('<Leave>', lambda event: projectbut.config(highlightthickness=0))
    projectbut.bind('<Button-1>', lambda event:fun())



#=================================================================== ANIMATION SCRIPT ================================================================

def barcollision(root,time,name,xnc,ync,**kwargs):
    width = 300
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = 250
    globalobj=Mainframe2()
    cddic=kwargs
    if cddic=={}:
        holdercan = globalobj.customcan(root, 300, 200, 'white', x, y)
    else:
        holdercan = globalobj.customcan(root, 300, 200, 'white', cddic['x'],cddic['y'] )

    block=holdercan.create_rectangle(135,140,165,150,fill='red',outline='red')
    line=holdercan.create_line(50,150,255,150,fill='red',width=5)
    label=globalobj.customlabels(holdercan,name,'none','white',xnc,ync)


    global s
    s=2

    def move():
        global s
        holdercan.move(block,0,s)

        stoper=holdercan.coords(block)
        if stoper[3]>=151.0:
            s=s*-1
            holdercan.itemconfig(block,fill='red',outline='red')
            holdercan.itemconfig(line,fill='green')
            label.config(fg='red')
        elif stoper[1]<=67.0:
            s=s*-1
            holdercan.itemconfig(block,fill='green',outline='green')
            holdercan.itemconfig(line,fill='red')
            label.config(fg='green')

        holdercan.update()
        holdercan.after(10,move)
    move()
    holdercan.after(time,holdercan.destroy)


def circleloading(root,time,name,xmc,ymc,**kwargs):

    width = 300
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = 250
    globalobj=Mainframe2()
    cd=kwargs
    if cd=={}:
        holdercan=globalobj.customcan(root,300,200,'white',x,y)

    else:
        x1=cd['x']
        y1=cd['y']
        holdercan=globalobj.customcan(root,300,200,'white',x1,y1)
    holdercan.config(highlightthickness=1,highlightbackground='black')


    globalobj.customlabels(holdercan,name,'none','white',xmc,ymc)

    holdercan.create_oval(95,100,115,120,fill='red',outline='red')
    holdercan.create_oval(125,100,145,120,fill='green',outline='green')
    holdercan.create_oval(155,100,175,120,fill='steelblue',outline='steelblue')
    holdercan.create_oval(185,100,205,120,fill='#ebcf1a',outline='yellow')

    def tw1():
        holdercan.create_oval(95, 100, 115, 120, fill='white', outline='white')

    def tw2():
        holdercan.create_oval(125, 100, 145, 120, fill='white', outline='white')

    def tw3():
        holdercan.create_oval(155, 100, 175, 120, fill='white', outline='white')

    def tw4():
        holdercan.create_oval(185, 100, 205, 120, fill='white', outline='white')


    def tr():
        holdercan.create_oval(95, 100, 115, 120, fill='red', outline='red')

    def tg():
        holdercan.create_oval(125, 100, 145, 120, fill='green', outline='green')

    def tsb():
        holdercan.create_oval(155, 100, 175, 120, fill='steelblue', outline='steelblue')

    def tb():
        holdercan.create_oval(185, 100, 205, 120, fill='#ebcf1a', outline='yellow')

    def whitescale():
        holdercan.after(200,tw1)
        holdercan.after(400,tw2)
        holdercan.after(600,tw3)
        holdercan.after(800,tw4)
        holdercan.after(800,changer)


    def changer():
        holdercan.after(200,tr)
        holdercan.after(400,tg)
        holdercan.after(600,tsb)
        holdercan.after(800,tb)
        holdercan.after(800,coordination)


    def coordination():
        whitescale()

    holdercan.after(100,coordination)

    holdercan.after(time,holdercan.destroy)

def login_load(name):
    ab_root = Toplevel()
    ab_root.state('zoom')
    ab_root.attributes('-alpha', 1)
    ab_root.wm_attributes('-topmost', True)
    ab_root.overrideredirect(True)
    rootCanvas = Canvas(ab_root, bg='white', )
    rootCanvas.pack(fill=BOTH, expand=1, anchor=CENTER)
    rootCanvas.create_text(700, 250, text=name, font=f'Ebrima 40', fill='black')

    def squarecircle(root, **kwargs):
        width = 300
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = 300

        globalobj = Mainframe2()
        coordinatesdic = kwargs

        if coordinatesdic == {}:
            holdercan = globalobj.customcan(root, 300, 100, 'white', x, y)
        else:
            x1 = coordinatesdic['x']
            y1 = coordinatesdic['y']
            holdercan = globalobj.customcan(root, 300, 100, 'white', x1, y1)

        r = globalobj.customframes(holdercan, 20, 20, 'red', 135, 10)
        g = globalobj.customframes(holdercan, 20, 20, 'green', 160, 10)
        sb = globalobj.customframes(holdercan, 20, 20, 'steelblue', 135, 35)
        b = globalobj.customframes(holdercan, 20, 20, 'black', 160, 35)

        def tr():
            r.config(bg='white')
            sb.config(bg='steelblue')

        def tg():
            g.config(bg='white')
            r.config(bg='red')

        def tb():
            b.config(bg='white')
            g.config(bg='green')

        def tsb():
            sb.config(bg='white')
            b.config(bg='black')

        def changer():
            r.after(200, tr)
            g.after(400, tg)
            b.after(600, tb)
            sb.after(800, tsb)
            holdercan.after(800, changer)

        changer()

    squarecircle(ab_root)
    ab_root.after(2100,lambda :ab_root.attributes('-alpha',0.6))
    ab_root.after(2150,lambda :ab_root.attributes('-alpha',0.5))
    ab_root.after(2220,lambda :ab_root.attributes('-alpha',0.4))
    ab_root.after(2250,lambda :ab_root.attributes('-alpha',0.3))
    ab_root.after(2300,lambda :ab_root.attributes('-alpha',0.2))
    ab_root.after(2350,lambda :ab_root.attributes('-alpha',0.1))
    ab_root.after(2400,lambda :ab_root.destroy())
    ab_root.mainloop()


#-----------------------------------------------------------------------------------------------------------------------------------------------------

class Verification:

    def authenticate(self,usernameen,passworden,uniqueid):

#---------------ADMIN----------------------------------
        self.adminname=adminusername()
        self.adminpw=adminpassword()
        self.adminid=adminuniqueid()

        for an,ap in zip(self.adminname,self.adminpw):
            validateadmin[an]=ap
        self.admkeys=validateadmin.keys()
        self.admvalues=validateadmin.values()

#-----------------FACULTY--------------------------------
        self.facultyuser=facultyusername()
        self.facultypw=facultypassword()
        self.empid=facultyempid()

        for fn,fp in zip(self.facultyuser,self.facultypw):
            validationfaculty[fn]=fp
        self.fkeylist=list(validationfaculty.keys())
        self.fvaluelist=list(validationfaculty.values())

#------------------STUDENT--------------------------------
        self.name = studentusername()
        self.password = studentpassword()
        self.sturol =studentrollno()
        for n,p in zip(self.name,self.password):
            validationstudent[n]=p
        self.keyslist=list(validationstudent.keys())
        self.valuelist=list(validationstudent.values())

        if uniqueid in self.sturol:

            if usernameen in self.keyslist:
                if validationstudent[usernameen]==passworden:
                        from studentPannel import students_panel               #-----------------------student login successfull-------------------
                        certain_student=fulldataofstudent(uniqueid)
                        #-------------display pic------------
                        dp_rol=fetch_rol2()
                        if uniqueid in dp_rol:
                            dp_pic=fetch_image(uniqueid)
                            if certain_student==1:
                                messagebox.showerror('Not Found','This is an invalid user!')
                            else:
                                if dp_pic!=[None]:
                                    students_panel('student',certain_student,dp_pic[0],usernameen,passworden,students_tabs)
                                else:
                                    students_panel('student',certain_student, 'defaultuser.png',usernameen,passworden,students_tabs)
                        else:
                            students_panel('student',certain_student,'defaultuser.png',usernameen,passworden,students_tabs)
                        #-------------------------------------
                else:
                    messagebox.showerror('Access Denied','Password is wrong!')
            else:
                messagebox.showwarning('User not found', "Looks like we don't know you\n You have to sign up first")

#-------------------------------FACULTY-----------------------authenticate---------------------------=======================---------------------------------------------

        else:
            if uniqueid in self.empid:
                if usernameen in self.fkeylist:
                    if validationfaculty[usernameen]==passworden:
                            from studentPannel import students_panel #-----------------------faculty login successfull-------------------
                            certain_faculty=fulldataoffaculty(uniqueid)
                            #---------display pic----------
                            dp_id=fetchfacid()
                            if uniqueid in dp_id:
                                dp_offac=fetchfacimg(uniqueid)
                                if certain_faculty==1:
                                    messagebox.showerror('Not Found','This is an invalid user')
                                else:
                                    if dp_offac !=[None]:
                                        students_panel('faculty', certain_faculty, dp_offac[0], usernameen, passworden,
                                                       faculty_tabs)
                                    else:
                                        students_panel('faculty', certain_faculty, 'defaultuser.png', usernameen, passworden,faculty_tabs)
                            else:
                                students_panel('faculty', certain_faculty, 'defaultuser.png', usernameen, passworden, faculty_tabs)
                    else:
                        messagebox.showerror('Access Denied', 'Password is wrong !')
                else:
                    messagebox.showwarning('User not found',"Looks like we don't know you\n You have to sign up first.")
            else:
                if uniqueid in self.adminid:
                    if usernameen in self.admkeys:
                        if validateadmin[usernameen]==passworden:
                                from mainpage import mainpageon
                                mainpageon(usernameen)

                        else:
                            messagebox.showerror('Access Denied', 'Password is wrong!')
                    else:
                         messagebox.showwarning('User not found',"Looks like we don't know you\n You have to sign up first.")
                else:
                    messagebox.showerror('Invalid','The ID/Roll No. you have entered is not valid')

#---------------------------------------------------------------------------------------------------------------------------------------------------------
def custompanelfun(identity,root,w,h,topmar,bxc,bxy):
    op2global=Mainframe2()
    op2ob1=Mainframe2()

    width = w
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = topmar
    helpdesk = op2ob1.customcan(root, w, h, 'white', x, y)
    helpdesk.config(highlightthickness=2, bd=2, highlightbackground='black')
    if identity=='feestruct':                             #850 700
        op2global.customlabels(helpdesk, 'Fee Structure', 'none 12 bold', 'white', 400, 10)
        op2ob1.line(350,40,550,40,'black',2)

    def closepage():
        helpdesk.destroy()

    op2global.custombuttons(helpdesk, 'Close', 5, 1, closepage, bxc, bxy)

#========================================================================= MAIN UPDATE OPERATIONS FUNCTION =========================================================================
class Fee:

    def fee_pannel(self,frameno,intro,windowname):
        #---------objects--------
        self.globalobj=Mainframe2()
        self.obj1=Mainframe2()
        self.obj2=Mainframe2()
        self.obj3=Mainframe2()
        self.obj4=Mainframe2()
        self.obj5=Mainframe2()
        self.obj6=Mainframe2()
        self.obj7=Mainframe2()
        self.obj8=Mainframe2()

        #===========================================    scrollable area and tree view   ====================================================

        from tkinter.ttk import Treeview

        self.infoframe = Frame(frameno, width=500, height=500, bg='white')
        self.infocan = self.globalobj.packedFrame(frameno, 200, 200, '#f2dd22', LEFT, fill=Y)

        self.xscrollbar = Scrollbar(self.infoframe, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)

        self.yscrollbar = Scrollbar(self.infoframe, orient=VERTICAL)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.table = Treeview(self.infoframe,
                              columns=('1', '2', '3', '4', '5', '6', '7','8','9','10'), xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)

        self.table.heading('1', text='NAME')
        self.table.heading('2', text='SURNAME')
        self.table.heading('3', text="ROLL NO")
        self.table.heading('4', text="FATHER'S NAME")
        self.table.heading('5', text='COURSE')
        self.table.heading('6', text='BRANCH')
        self.table.heading('7', text='YEAR')
        self.table.heading('8', text='SEMESTER')
        self.table.heading('9', text='FEE')
        self.table.heading('10', text='FEE STATUS')

        self.table['show']='headings'

        self.table.pack(side=TOP, fill=BOTH, expand=1)

        self.xscrollbar.config(command=self.table.xview)
        self.yscrollbar.config(command=self.table.yview)
        self.infoframe.pack(side=RIGHT, fill=BOTH, expand=1)



        #=============================================================================================================
        self.datainputframe1 = self.globalobj.customframes(self.infocan, 200, 720, '#f2dd22', 0, 28)

        self.globalobj.customlabels(self.datainputframe1, windowname, 'none', 'black', 0, 10,22,1,fg='white')

        self.roll=self.globalobj.customlabels(self.datainputframe1, 'Roll No. :', 'none', '#f2dd22', 10, 40)
        self.obj2.genralentry(self.datainputframe1, 10, 70, 28)

        # ==============================================================================================================

        def fillStatusofstu(event):
            rowinfo = self.table.focus()
            valinfo = self.table.item(rowinfo)
            stumetadata = valinfo['values']
            print(stumetadata)
            width = 400
            x = (frameno.winfo_screenwidth() // 2) - (width // 2)
            y = 250
            feestat = self.globalobj.customcan(frameno, width, 300, 'white', x, y)
            feestat.config(highlightthickness=2, bd=2, highlightbackground='black')

            self.globalobj.customlabels(feestat, 'Fill Status :', 'none 12 bold', 'white', 10, 10)
            self.globalobj.customlabels(feestat, f'Name         :   {stumetadata[0]+" "+stumetadata[1]}', None, 'white', 25, 40)
            self.globalobj.customlabels(feestat, f'Roll No.     :   {stumetadata[2]}', None, 'white', 25, 70)
            self.globalobj.customlabels(feestat, f'Total Fee    :   {stumetadata[-2]}', None, 'white', 25, 100)
            pf=self.globalobj.customlabels(feestat, f'Pending Fee  :   {stumetadata[-1]}', None, 'white', 25, 130,fg='red')
            if stumetadata[-1]==0:
                pf.config(fg='green')
            else:
                pass
            am=self.globalobj.customlabels(feestat, 'Fill ammount   :', None, 'white', 25, 160)

            self.obj5.userintentry(feestat,120,160,25)

            def fillingfee():
                fillingammount1 = self.obj5.getint()
                if fillingammount1 != '':
                    try:
                            fillingammount=int(self.obj5.getint())
                            if fillingammount >stumetadata[-1]:
                                messagebox.showerror('Ammount Error','Ammount can not be greater than Pending ammount.',parent=frameno)
                            elif stumetadata[-1]==0:
                                # pf.config(fg='green')
                                messagebox.showerror('No Dues','There is no pending ammount to fill',parent=frameno)
                            else:

                                dueammount=stumetadata[-1]-fillingammount
                                updateFee(dueammount,stumetadata[2])
                                messagebox.showinfo('Success!','Ammount is filled Successfully!',parent=frameno)
                                feestat.destroy()
                                fetchfeeinfo()

                    except ValueError:
                                messagebox.showerror('Value Error', 'Please enter a valid ammount in digits', parent=frameno)
                else:
                     am.config(fg='red')

            def closepage():
                feestat.destroy()



            self.globalobj.custombuttons(feestat, 'Close', 5, 1, closepage, 360, 2)
            self.globalobj.custombuttons(feestat, 'Fill', 15, 1, fillingfee, 20, 260)
            # self.globalobj.custombuttons(feestat, 'Close', 5, 1, closepage, 360, 2)
        def exit():
            self.infocan.destroy()
            self.infoframe.destroy()
            self.datainputframe1.destroy()
            buthlp.destroy()
            butback.destroy()

        # -----------------------------------------------------------------------------

        butback = self.globalobj.custombuttons(intro, 'Back ', 10, 1, exit, 1130, 13)
        buthlp = self.globalobj.custombuttons(intro, 'Help ', 10, 1, None, 1230, 13)

        butback.bind('<Enter>', lambda event, bc=butback: bc.config(bg="red", fg='white'))
        butback.bind('<Leave>', lambda event, bc=butback: bc.config(bg="white", fg='black'))

        buthlp.bind('<Enter>', lambda event, bc=buthlp: bc.config(bg="green", fg='white'))
        buthlp.bind('<Leave>', lambda event, bc=buthlp: bc.config(bg="white", fg='black'))

        # -----------------------------------------------------------------------------



        def fetchfeeinfo():
            rol=self.obj2.getgenralentrydata()
            d,rolfe=fetch_feeStatus(rol)
            self.table.delete(*self.table.get_children())

            if rol=='':
                for valfee1 in d:
                    self.table.insert('',END,values=valfee1)
            else:
                if d != [] and rolfe != []:
                    self.table.delete(*self.table.get_children())
                    for valfee2 in rolfe:
                        self.table.insert('',END,values=valfee2)
                else:
                    messagebox.showwarning('Invalid Rollno','No data found for this roll no.',parent=frameno)

        self.table.bind('<ButtonRelease-1>',fillStatusofstu)

        self.butfetch=self.globalobj.custombuttons(self.datainputframe1, 'Fetch', 10, 1, fetchfeeinfo, 100, 500)
        self.butcancel=self.globalobj.custombuttons(self.datainputframe1, 'Cancel', 10, 1, exit, 10, 500)

#===========================================================================================================================================================================

def newstudent():
    from oops2 import Mainframe2
    win=Toplevel()
    width=850
    win.resizable(False,False)
    center=' '*110
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y=20
    win.geometry(f'{width}x700+{x}+{y}')
    win.iconbitmap(cg_logo)
    win.title(center+'Student Registration Pannel')
    win.iconbitmap(win,cg_logo)
    win.focus()

    def errorinfo(tag,xc,xy):
        wobjGlobal.customlabels(scrollablecan, tag, None, None, xc, xy, 2, 1, fg='red')

    # Objects of Mainframe
    wobjGlobal = Mainframe2()

    wobj1 = Mainframe2()
    wobj2 = Mainframe2()
    wobj3 = Mainframe2()
    wobj4 = Mainframe2()
    wobj5 = Mainframe2()
    wobj6 = Mainframe2()
    wobj7 = Mainframe2()
    wobj8 = Mainframe2()
    wobj9 = Mainframe2()
    wobj10 = Mainframe2()
    wobj13 = Mainframe2()
    wobj14 = Mainframe2()
    wobj15 = Mainframe2()
    wobj16 = Mainframe2()
    wobj17 = Mainframe2()
    wobj18 = Mainframe2()
    wobj19 = Mainframe2()
    wobj20 = Mainframe2()
    wobj23 = Mainframe2()
    wobj24 = Mainframe2()
    wobj25 = Mainframe2()
    wobj26 = Mainframe2()
    wobj27 = Mainframe2()
    wobj28 = Mainframe2()
    wobj29 = Mainframe2()
    wobj30 = Mainframe2()

    #---------------------------------DIVIDERS----------------------

    holderframe=wobjGlobal.customframes(win,850,720,'green',0,0)
    scrollablecan=Canvas(holderframe,width=1355,height=720)
    scrollablecan.pack(side=LEFT,expand=True,fill=BOTH)

    divider1=scrollablecan.create_line(25,190,800,190,fill='black',width=1)
    divider2=scrollablecan.create_line(25,280,800,280,fill='black',width=1)
    divider3=scrollablecan.create_line(610,300,610,600,fill='black',width=1)

    #--------Display Pic-----------------------------------
    dp=wobj30.customcan(scrollablecan,150,150,'white',30,20)
    #------------------------------Personal details-------------------------------
    stufirstname=wobjGlobal.customlabels(scrollablecan,'First Name : ','none',None,200,30)
    wobj1.userEntry(scrollablecan,325,35,25)

    stulastname = wobjGlobal.customlabels(scrollablecan, 'Last Name: ', 'none', None, 510, 30)
    wobj2.userEntry(scrollablecan, 640, 35, 25)

    stufathername=wobjGlobal.customlabels(scrollablecan,"Father's Name: ",'none',None,200,80)
    wobj3.userEntry(scrollablecan,325,85,25)

    stumothername=wobjGlobal.customlabels(scrollablecan,"Mother's Name :",'none',None,510,80)
    wobj5.userEntry(scrollablecan,640,85,25)

    stuparentcontact=wobjGlobal.customlabels(scrollablecan,'Parents Contact : ','none',None,200,130)
    wobj4.userintentry(scrollablecan,325,135,25)

    stuphoneno=wobjGlobal.customlabels(scrollablecan,'Phone no.: ','none',None,510,130)
    wobj6.userintentry(scrollablecan,640,135,25)
    #----------------------------------------------------------------------------

    #---------------------------Year branch course-----------------------
    stucourse=wobjGlobal.customlabels(scrollablecan,'Course :','none',None,25,200)
    c=wobj7.customcombobox(scrollablecan,'-Select Course-',courses,20,100,200)

    stubranch=wobjGlobal.customlabels(scrollablecan,'Branch :','none',None,290,200)
    brn=wobj8.customcombobox(scrollablecan,'-Select Branch-',None,20,370,200)

    stuyear=wobjGlobal.customlabels(scrollablecan,'Year :','none',None,550,200)
    yo=wobj9.customcombobox(scrollablecan,'-Select Year-',None,20,610,200)

    #-------------------------------------------------------------------
    def example1(event):
        def print_sel():
            print(cal.selection_get())
            month.set(cal.selection_get())
            top.destroy()

        top = Toplevel(win)

        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand2",year=1999)
        cal.pack(fill="both", expand=True)
        Button(top, text="Submit",width=15,height=1, command=print_sel,bg='green',fg='white').pack()

    studob=wobjGlobal.customlabels(scrollablecan,'D.O.B :','none',None,25,240)
    month=wobj10.customcombobox(scrollablecan,'select',None,20,100,240)

    month.bind("<ButtonRelease-1>",example1)

    stusem=wobjGlobal.customlabels(scrollablecan,'SEM :','none',None,290,240)
    semrol=wobj14.customcombobox(scrollablecan,'-Semester-','',20,370,240)

    sturollno=wobjGlobal.customlabels(scrollablecan,'Roll No :','none',None,550,240)
    wobj13.genralentry(scrollablecan,615,240,23)


    stucountry=wobjGlobal.customlabels(scrollablecan,'Country :','none',None,25,300)
    wobj15.userEntry(scrollablecan,130,300,25)

    stucity=wobjGlobal.customlabels(scrollablecan,'City :','none',None,25,340)
    wobj16.userEntry(scrollablecan,130,340,25)

    stupin=wobjGlobal.customlabels(scrollablecan,'PIN Code :','none',None,25,380)
    wobj17.userintentry(scrollablecan,130,380,25)

    stuemail=wobjGlobal.customlabels(scrollablecan,'E-mail :','none',None,25,420)
    wobj18.emailentry(scrollablecan,130,420,25)
    #------------------------------------------------------------------------------------- LEFT...
    stuadhaar=wobjGlobal.customlabels(scrollablecan,'Adhaar No.:','none',None,320,300)
    wobj19.userintentry(scrollablecan,430,300,25)

    def example2(event):
        def print_sel():
            # print(cal.selection_get())
            regmonth.set(cal2.selection_get())
            top.destroy()

        top = Toplevel(win)

        cal2 = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand2")
        cal2.pack(fill="both", expand=True)
        Button(top, text="Submit", width=15, height=1, command=print_sel, bg='green', fg='white').pack()

    stureg=wobjGlobal.customlabels(scrollablecan,'Date of Reg. :','none',None,320,340)
    regmonth=wobj20.customcombobox(scrollablecan,'',None,20,430,340)

    regmonth.bind('<ButtonRelease-1>',example2)

    stubatch=wobjGlobal.customlabels(scrollablecan,'Batch :','none',None,320,380)
    batchstart=wobj23.customcombobox(scrollablecan,'Year',yearofdob,5,430,380)
    wobjGlobal.customlabels(scrollablecan,'To','none',None,495,380)
    wobj24.customcombobox(scrollablecan,'Year',['select from'],5,530,380)

    stugender=wobjGlobal.customlabels(scrollablecan,'Gender :','none',None,320,420)
    wobj26.customcombobox(scrollablecan,'Select Gender',['Male','Female','Others'],20,430,420)

    stuaddress=wobjGlobal.customlabels(scrollablecan,'Address :','none',None,25,460)
    wobj25.txtarea(scrollablecan,56,2,130,460)

    wobjGlobal.customlabels(scrollablecan,'Fee :','none',None,25,530)
    feeentry=wobj27.userintentry(scrollablecan,130,530,25)
    wobj27.setintegerentry(0)

    wobjGlobal.customlabels(scrollablecan,'Transport Service :','none',None,300,530)
    trans=wobj28.customcombobox(scrollablecan,'select',None,15,450,534)

    #------------------------------LIST BOX------------------
    wobjGlobal.customlabels(scrollablecan,'Documents Provided','none',None,638,290)
    allingmigration=' '*6
    doclist=Listbox(scrollablecan,width=20,height=14,font='none 12',selectmode=MULTIPLE)
    doclist.place(x=620,y=320)
    doclist.insert(0,allingmigration+'12th Marksheet')
    doclist.insert(1,allingmigration+'Migration Certificate')
    doclist.insert(2,allingmigration+'10th Marksheet')
    doclist.insert(3,allingmigration+'Charecter Certificate')
    doclist.insert(4,allingmigration+'Adhaar Card')
    doclist.insert(5,allingmigration+'PAN Card')
    doclist.insert(6,allingmigration+'Driving Licence')
    doclist.insert(7,allingmigration+'Medical Certificate')
    #--------------------------------------------------------

    #---------------------------SUGGESTION EVENT BINDINGS---------------------------------
    def tranfeeconfig(transincluded):
        wobj27.setintegerentry(transincluded)

    def hover_transport(event):
        selected_choice=wobj28.getcombodata()
        if selected_choice=='Yes':
            rawfee = int(wobj27.getint())
            transincluded = rawfee + 20000
            tranfeeconfig(transincluded)
        elif selected_choice=='No':
            accord_branch=wobj7.getcombodata()
            if accord_branch=='B.Tech':
                tranfeeconfig(btech_fee[0])
            elif accord_branch=='BSc':
                tranfeeconfig(35000)
    trans.bind('<<ComboboxSelected>>',hover_transport)

#--------------------branch year semester events------------------------------------------

    def branch_config(brlist):
        # wobj8.customcombobox(scrollablecan, '-Select Branch-', brlist, 20, 370, 200)
        brn.set('-Select Branch-')
        brn.config(values=brlist)
    def year_config(yearl):
        # wobj9.customcombobox(scrollablecan, '-Select Year-', yearl, 20, 610, 200)
        yo.set('-Select Year-')
        yo.config(values=yearl)
    def rol_to_branch(event):
        rolb=wobj8.getcombodata()
        yo.set('-Select Year-')
        wobj13.setgenraluser('')

        semrol.set('-Semester-')
        if rolb==btech_fileld[1]:
            btechrol11.insert(1,'C')
        elif rolb==btech_fileld[2]:
            btechrol11.insert(1,'M')
        elif rolb==btech_fileld[3]:
            btechrol11.insert(1,'E')
        elif rolb==btech_fileld[4]:
            btechrol11.insert(1,'C')

        elif rolb==bsc_fields[1]:
            btechrol11.insert(1,'G')
        elif rolb==bsc_fields[2]:
            btechrol11.insert(1,'P')
        elif rolb==bsc_fields[3]:
            btechrol11.insert(1,'M')
        elif rolb==bsc_fields[4]:
            btechrol11.insert(1,'C')
        elif rolb==bsc_fields[5]:
            btechrol11.insert(1,'L')
        elif rolb == bsc_fields[6]:
            btechrol11.insert(1, 'CO')
        elif rolb==bsc_fields[4]:
            btechrol11.insert(1,'BB')
        elif rolb==bsc_fields[8]:
            btechrol11.insert(1,'BC')

    brn.bind('<<ComboboxSelected>>',rol_to_branch)

    def hover_select(event):
        yo.set('-Select Year-')
        semrol.set('-Semester-')
        wobj13.setgenraluser('')
        selected_course_for_branch = wobj7.getcombodata()

        if selected_course_for_branch == 'B.Tech':
            branch_config(btech_fileld)
            year_config(btech_years)
            btechrol11.insert(0, 'A')
            # wobj13.setgenraluser(btechrol11[0])
            # ------transport-----------
            wobj27.setintegerentry(btech_fee[0])
            trans.config(values=choice_list)

        elif selected_course_for_branch == 'BSc/UG':
            branch_config(bsc_fields)
            year_config(ug_years)
            btechrol11.insert(0, 'B')
            # -----transport-----------
            wobj27.setintegerentry(bsc_fee[0])
            trans.set('select')
            trans.config(values=choice_list)

        elif selected_course_for_branch == 'M.Tech':
            branch_config(btech_fileld)
            year_config(btech_years)
            btechrol11.insert(0, 'MT')
            # --------transport-----------
            wobj27.setintegerentry(mtech_fee[0])
            trans.set('select')
            trans.config(values=choice_list)

        elif selected_course_for_branch == 'MSc':
            branch_config(bsc_fields)
            year_config(ug_years)
            btechrol11.insert(0, 'MUG')
            # --------transport----------
            wobj27.setintegerentry(msc_fee[0])
            trans.set('select')
            trans.config(values=choice_list)

        elif selected_course_for_branch == 'B.Com':
            branch_config(['B.Com'])
            year_config(ug_years)
            btechrol11.insert(0, 'C')
            # -------transport---------
            wobj27.setintegerentry(bsc_fee)
            trans.set('select')
            trans.config(values=choice_list)

        elif selected_course_for_branch == 'BBA':
            branch_config(['BBA'])
            year_config(ug_years)
            btechrol11.insert(0, 'D')
            # ---------transport----------
            wobj27.setintegerentry(bsc_fee)
            trans.set('select')
            trans.config(values=choice_list)

        elif selected_course_for_branch == 'BCA':
            branch_config(['BCA'])
            year_config(ug_years)
            btechrol11.insert(0, 'E')
            # --------transport-------
            wobj27.setintegerentry(bsc_fee)
            trans.set('select')
            trans.config(values=choice_list)

        else:
            branch_config(['No Information'])
            year_config(['No Information'])
            trans.config(values=['No information'])
            # sem_config('No Data')

    c.bind('<<ComboboxSelected>>',hover_select)
    #---------------semester suggestion------------
    def sem_config(semdata):
        semrol.set('-Semester-')
        semrol.config(values=semdata)


    def accord_year_sem(event):
        semrol.set('-Semester-')
        sel_year=wobj9.getcombodata()
        if sel_year=='1st year':
            sem_config(['1st semester','2nd semester'])
        elif sel_year=='2nd year':
            sem_config(['3rd semester','4th semester'])
        elif sel_year=='3rd year':
            sem_config(['5th semester','6th semester'])
        elif sel_year=='4th year':
            sem_config(['7th semester','8th semester'])
        else:
            sem_config(['select year first'])
    yo.bind('<<ComboboxSelected>>',accord_year_sem)

    def semroladjustment(event):
        semsel=wobj14.getcombodata()
        print(semsel)
        if semsel=='1st semester':
            btechrol11.insert(2,'103170')
            wobj13.setgenraluser(btechrol11[0]+btechrol11[1]+btechrol11[2])
            print(btechrol11[0]+btechrol11[1])

        elif semsel=='2nd semester':
            btechrol11.insert(2,'203170')
            wobj13.setgenraluser(btechrol11[0]+btechrol11[1]+btechrol11[2])

        elif semsel=='3rd semester':
            btechrol11.insert(2,'303170')
            wobj13.setgenraluser(btechrol11[0]+btechrol11[1]+btechrol11[2])

        elif semsel=='4th semester':
            btechrol11.insert(2,'403170')
            wobj13.setgenraluser(btechrol11[0]+btechrol11[1]+btechrol11[2])

        elif semsel=='5th semester':
            btechrol11.insert(2,'503170')
            wobj13.setgenraluser(btechrol11[0]+btechrol11[1]+btechrol11[2])

        elif semsel=='6th semester':
            btechrol11.insert(2,'603170')
            wobj13.setgenraluser(btechrol11[0]+btechrol11[1]+btechrol11[2])

        elif semsel=='7th semester':
            btechrol11.insert(2,'703170')
            wobj13.setgenraluser(btechrol11[0]+btechrol11[1]+btechrol11[2])

        elif semsel=='8th semester':
            btechrol11.insert(2,'803170')
            wobj13.setgenraluser(btechrol11[0]+btechrol11[1]+btechrol11[2])

    semrol.bind('<<ComboboxSelected>>',semroladjustment)

    #---------------BATCH-------------------
    def endbatchconfig(dataofendbatch):
        wobj24.customcombobox(scrollablecan, 'Year', dataofendbatch, 5, 530, 380)

    def batchhover(event):
        startdate=int(wobj23.getcombodata())
        onindex=yearofdob.index(startdate)

        endbatchconfig(yearofdob[onindex:])

    batchstart.bind('<<ComboboxSelected>>',batchhover)
#------------------------------------------------------------------------------------------------------

    #-----------------------------FOOTER FRAME----------------------------
    footer=wobjGlobal.customframes(scrollablecan,9000,50,'steelblue',0,650)

    def errorhandleing(message):
        messagebox.showerror('Invalid Entry',message,parent=win)

    def getting_values():

        #-----------getting selected documents-----
        listof_doc=[]
        selected_documents=doclist.curselection()
        if selected_documents==():
            listof_doc.append('No Documents')
        else:
            for docselected in selected_documents:
                listof_doc.append(str((doclist.get(docselected))).split('  ')[3])

        final_listofdoc=str(listof_doc).split('$%')
        #------------------------------------------
        first_name = wobj1.getuserentry()
        last_name = wobj2.getuserentry()
        father_name = wobj3.getuserentry()
        mother_name = wobj5.getuserentry()
        # ----------COMBODATA-------------------
        course_name = wobj7.getcombodata()
        branch_name = wobj8.getcombodata()
        sem = wobj14.getcombodata()
        year_name = wobj9.getcombodata()
        #--------checking validity of roll no-----------

        rollno = wobj13.getgenralentrydata()
        invalid_roll_no=existing_rollno(course_name,branch_name,year_name,sem)
        if rollno in invalid_roll_no:
            messagebox.showerror('Already Exixt','This roll no. is already been assigned in this course to this branch and year',parent=win)
        else:

            #--------------dates-------------------------------
            monthofdob = wobj10.getcombodata()

            monthofreg = wobj20.getcombodata()

            finaldob = str(monthofdob)
            finaldateofreg = str(monthofreg)

            batchstarting = wobj23.getcombodata()
            batchending = wobj24.getcombodata()
            batch_duration=batchstarting+'-'+batchending
            #-----------------------------------------------------
            genderdata = wobj26.getcombodata()
            email=wobj18.getemail()

            transport_service=wobj28.getcombodata()
            # --------------------------------------
            country_name = wobj15.getuserentry()
            city_name = wobj16.getuserentry()
            addressofstu = wobj25.gettext()

            pcontact = list(wobj4.getint())
            phno = list(wobj6.getint())
            pinno = list(wobj17.getint())
            adhaarcardno = list(wobj19.getint())
            #----------EXCEPTION HANDELING----------------------
            print(monthofdob,monthofreg)

            if first_name=='':
                errorhandleing('Please enter Name')

            elif last_name=='':
                errorhandleing('Please enter surname')

            elif father_name=='':

                errorhandleing("Please enter Father's Name")

            elif mother_name=='':
                errorhandleing("Please enter Mother's Name")

            elif pcontact==[]:
                errorhandleing('Enter Parents Contact')

            elif phno==[]:
                errorhandleing('Enter your Phone No.')

            elif course_name =='-Select Course-' or course_name=='':
                errorhandleing('Please select a course to proceed.')

            elif branch_name=='-Select Branch-' or branch_name=='':
                errorhandleing('Please select the Branch associated with that course')

            elif year_name=='-Select Year-' or year_name=='':
                errorhandleing('Select the year')

            elif monthofdob=='select' or monthofdob=='':
                errorhandleing('Select Month For D.O.B')

            elif rollno=='':
                errorhandleing('Enter the new Roll No. of Student')

            elif sem == '-Semester-' or sem == '':
                errorhandleing('select the Semester')

            elif country_name=='':
                errorhandleing('Enter the country name')

            elif city_name=='':
                errorhandleing('Enter the name of city')

            elif pinno==[]:
                errorhandleing('Enter the PIN no.')

            elif email==False:
                errorhandleing('Please enter a valid email in "@gmail.com" format.')

            elif adhaarcardno=='':
                errorhandleing('Please enter a valid Adhaar card no.')

            elif monthofreg=='select' or monthofreg=='':
                errorhandleing('Selct the month of registration')

            elif batchstarting=='Year' or batchstarting=='':
                errorhandleing('Select batch starting year')
            elif batchending=='Year' or batchending=='':
                errorhandleing('Select batch ending year')

            elif genderdata=='Select Gender' or genderdata=='':
                errorhandleing('Please select Gender')

            elif addressofstu=='':
                errorhandleing('Enter your address')

            elif transport_service=='select' or transport_service=='':
                errorhandleing('Please select transport services')

            else:
                if len(pcontact)==10:
                    errorinfo('', 500, 135)
                    stuparentcontact.config(fg='black')
                    wobjGlobal.customlabels(scrollablecan, '', None, None, 500, 135, 2, 1)

                    if len(phno) == 10:
                            errorinfo('',800,135)
                            stuphoneno.config(fg='black')
                            wobjGlobal.customlabels(scrollablecan, '', None, None, 800, 135, 2, 1)

                            if len(pinno) == 6:
                                errorinfo('',290,382)
                                stupin.config(fg='black')

                                if len(adhaarcardno) == 12:
                                    errorinfo('',582,300)
                                    stuadhaar.config(fg='black')

                                    try:
                                        parentscontact = int(wobj4.getint())
                                        phoneno = int(wobj6.getint())
                                        pincode = int(wobj17.getint())
                                        adhaar = int(wobj19.getint())
                                        feeofstu = int(wobj27.getint())
                                    except ValueError:
                                        messagebox.showerror('Invalid', 'Some of the information you entered is invalid',parent=win)
                                    else:

                                        responce=messagebox.askyesno('Confirmation','The entered data will be stored in database.\nConfirm with yes/no',parent=win)
                                        if responce==True:
                                            data_warehouse(first_name, last_name, rollno, course_name, branch_name,
                                                           year_name, sem, father_name, mother_name, parentscontact, finaldob,
                                                           phoneno, email, country_name, city_name, pincode, adhaar,
                                                           finaldateofreg,
                                                           batch_duration, genderdata, feeofstu, transport_service,
                                                           addressofstu, *final_listofdoc)
                                            #-------------- FEE STATUS DATABASE INSERTION ----------------------------
                                            studentFeestatus(first_name,last_name,rollno,father_name,course_name,branch_name,year_name,sem,feeofstu,feeofstu)
                                            messagebox.showinfo('Success!','Data saved sucessfully!',parent=win)
                                            win.destroy()
                                        else:
                                            pass
                                else:
                                    errorinfo('',582,300)
                                    stuadhaar.config(fg='red')
                                    messagebox.showerror('Invalid Value', 'Please enter a valid 12-digit Adhaar Card Number.',parent=win)
                            else:
                                errorinfo('',290,382)
                                stupin.config(fg='red')
                                messagebox.showerror('Inavalid Value', 'Please enter a valid 6-digit PIN Code.',parent=win)
                    else:
                            errorinfo('',800,135)
                            stuphoneno.config(fg='red')
                            messagebox.showerror('Invalid','Please enter a valid 10-digit phone no.',parent=win)
                else:
                    errorinfo('', 470, 135)
                    stuparentcontact.config(fg='red')
                    messagebox.showerror('Invalid', 'Please enter a valid 10-digit phone no.',parent=win)

    def exit():
        torem=fetch_image(wobj13.getgenralentrydata())
        if torem !=[]:
            os.remove(f"{studir_path}//{torem[0]}")
            deleting_image_onaccount(wobj13.getgenralentrydata())
        else:
            pass
        win.destroy()

    def loadin_dp():
        rol = wobj13.getgenralentrydata()

        if rol not in valid_rollno():
            from tkinter import filedialog
            if rol=='':
                messagebox.showerror('Fatal Error',"Can't assign the pic withot full information.\nFill the form completely first.",parent=win)
            else:
                path=filedialog.askopenfile(title='Choose Image',parent=win,filetype=[('png Files','*.png'),('jpeg Files','*.jpeg'),
                                                                                      ('jpg Files','*.jpg')])
                renamed_path=str(path.name).split('/')[-1]
                if list(renamed_path).count('.') ==1:
                    image_name_splitted=str(renamed_path).split('.')

                    print(image_name_splitted[0]+'.png')

                    imgfile_dp=Image.open(path.name)
                    imgfile_dp.thumbnail(dp_max_size)
                    imgfile_dp.save(f'{studir_path}//{image_name_splitted[0]}.png')
                    try:
                        image_insert(rol,f'{image_name_splitted[0]}.png')
                        wobj30.image(f'{studir_path}//{image_name_splitted[0]}.png', 0, 0)
                        but.destroy()
                    except:
                        messagebox.showerror('Already Exist','Image with this name already exist in database.\n\nTry changing the Image name or Roll no.',parent=win)

                else:
                    messagebox.showwarning("Parsing Error!","Your imahe file contains too many  '. DOTS'  in name. Please rename the file and try again.",parent=win)
        else:
            messagebox.showerror('Already Exist',
                             'This Roll no. already exist in database.',
                             parent=win)


    #-----------------------------BUTTONS---------------------------------
    wobjGlobal.custombuttons(footer,'Submit',10,1,getting_values,50,10)
    wobjGlobal.custombuttons(footer,'Cancel',10,1,exit,170,10)
    but=wobj29.custombuttons(dp,'upload img.',10,1,loadin_dp,35,60)

    win.mainloop()


#====================================================================================================================================================================================

#========================================================================= MAIN FETCH OPERATIONS FUNCTION FOR STUDENTS==============================================================

def fetch(selected_course,selected_year,selected_branch,given_roll,frameno,selected_sem,table,maindata):
           narrowfetch, cbys, cbyr, cby, cbsr, cbs, cbr, cb, cs, onlyc, cys, cy, bysr, bys, byr, by, bsr, bs, onlyb, ys, onlyyear, onlysem, defaultinfo=maindata
           def errorh(mess):
               messagebox.showerror('Invalid Attempt!',mess,parent=frameno)

           if selected_course !='select' and selected_course !='':
               if selected_branch !='select' and selected_branch !='':
                   if selected_year !='select' and selected_year !='':
                       if selected_sem !='select' and selected_sem !='':
                           if given_roll !='':
                               if narrowfetch==[]:
                                   errorh('No data found for given info')
                               else:
                                   table.delete(*table.get_children())

                                   for vals1 in narrowfetch:
                                       table.insert('',END,values=vals1)
                           else:
                               if cbys==[]:
                                   errorh('Rare case.\nNo information found for given information')
                               else:
                                   table.delete(*table.get_children())

                                   for vals2 in cbys:
                                       table.insert('',END,values=vals2)
                       else:
                           if given_roll !='':
                               if cbyr==[]:
                                   errorh('No data Found')
                               else:
                                   table.delete(*table.get_children())

                                   for vals3 in cbyr:
                                       table.insert('',END,values=vals3)
                           else:
                               if cby==[]:
                                   errorh('no data')
                               else:
                                   table.delete(*table.get_children())

                                   for vals4 in cby:
                                       table.insert('',END,values=vals4)
                   else:
                       if selected_sem !='select' and selected_sem !='':
                           if given_roll !='':
                               if cbsr==[]:
                                   errorh('no data found cbsr')
                               else:
                                   table.delete(*table.get_children())

                                   for vals5 in cbsr:
                                       table.insert('',END,values=vals5)
                           else:
                               if cbs==[]:
                                   errorh('nodatafound cbs')
                               else:
                                   table.delete(*table.get_children())

                                   for vals6 in cbs:
                                       table.insert('',END,values=vals6)
                       else:
                           if given_roll !='':
                               if cbr==[]:
                                   errorh('no data found cbr')
                               else:
                                   table.delete(*table.get_children())

                                   for vals7 in cbr:
                                       table.insert('', END, values=vals7)
                           else:
                               if cb==[]:
                                   errorh('no data cb')
                               else:
                                   table.delete(*table.get_children())

                                   for vals23 in cb:
                                       table.insert('', END, values=vals23)
               else:
                   if selected_year !='select' and selected_year !='':
                       if selected_sem !='select' and selected_sem !='':
                           if given_roll !='':
                               errorh('Please select branch ysr')
                           else:
                               if cys==[]:
                                   errorh('nodata found cys')
                               else:
                                   table.delete(*table.get_children())

                                   for vals8 in cys:
                                       table.insert('',END,values=vals8)
                       else:
                           if given_roll !='':
                               errorh('please select branch to search with roll no')
                           else:
                               if cy==[]:
                                   errorh('no data found cy')
                               else:
                                   table.delete(*table.get_children())

                                   for vals9 in cy:
                                       table.insert('',END,values=vals9)
                   else:
                       if selected_sem !='select' and selected_sem !='':
                           if given_roll !='':
                               errorh('Sufficiant information not provided')
                           else:
                               if cs==[]:
                                   errorh('no data found cy')
                               else:
                                   table.delete(*table.get_children())

                                   for vals10 in cs:
                                       table.insert('',END,values=vals10)
                       else:
                           if given_roll !="":
                               errorh('no quite sufficient information provided')
                           else:
                               if onlyc ==[]:
                                   errorh('No one has applied for this course yet')
                               else:
                                   table.delete(*table.get_children())

                                   for vals11 in onlyc:
                                       table.insert('',END,values=vals11)
           else:
               if selected_branch !='select' and selected_branch !='':
                   if selected_year !='select' and selected_year !='':
                       if selected_sem !='select' and selected_sem !='':
                           if given_roll !='':
                               if bysr==[]:
                                   errorh('no data found bysy')
                               else:
                                   table.delete(*table.get_children())

                                   for vals12 in bysr:
                                       table.insert('',END,values=vals12)
                           else:
                               if bys==[]:
                                   errorh(' no data found byy')
                               else:
                                   table.delete(*table.get_children())

                                   for vals13 in bys:
                                       table.insert('',END,values=vals13)
                       else:
                           if given_roll !='':
                               if byr==[]:
                                   errorh('no data found byy')
                               else:
                                   table.delete(*table.get_children())

                                   for vals14 in byr:
                                       table.insert('',END,values=vals14)
                           else:
                               if by ==[]:
                                   errorh('no data found by')
                               else:
                                   table.delete(*table.get_children())

                                   for vals15 in by:
                                       table.insert('',END,values=vals15)
                   else:
                       if selected_sem !='select' and selected_sem !='':
                           if given_roll !='':
                               if bsr==[]:
                                   errorh('no data found so far bsy')
                               else:
                                   table.delete(*table.get_children())

                                   for vals16 in bsr:
                                       table.insert('',END,values=vals16)
                           else:
                               if bs==[]:
                                   errorh('no data found by')
                               else:
                                   table.delete(*table.get_children())

                                   for vals17 in bs:
                                       table.insert('',END,values=vals17)
                       else:
                           if given_roll !='':
                               errorh('Not sufficient information provided')
                           else:
                               if onlyb==[]:
                                   errorh('Rare case.\nNo one is in this branch')
                               else:
                                   table.delete(*table.get_children())

                                   for vals18 in onlyb:
                                       table.insert('',END,values=vals18)
               else:
                   if selected_year !='select' and selected_year !='':
                       if selected_sem !='select' and selected_sem !='':
                           if given_roll !='':
                               errorh('select branch to serch with rollno')
                           else:
                               if ys==[]:
                                   errorh('no data found yy')
                               else:
                                   table.delete(*table.get_children())

                                   for vals19 in ys:
                                       table.insert('',END,values=vals19)
                       else:
                           if given_roll !='':
                               errorh('Please selct branch to search with rollno')
                           else:
                               if onlyyear==[]:
                                   errorh('Rare case, No one is in this year')
                               else:
                                   table.delete(*table.get_children())

                                   for vals20 in onlyyear:
                                       table.insert('',END,values=vals20)

                   else:
                       if selected_sem !='select' and selected_sem !='':
                           if given_roll !='':
                               errorh('Rare case, No one is in this year')
                           else:
                               if onlysem==[]:
                                   errorh('rare case , no one is in this semester')
                               else:
                                   table.delete(*table.get_children())

                                   for vals21 in onlysem:
                                       table.insert('',END,values=vals21)

                       else:
                           if given_roll !='':
                               meta_stack=fetch_on_rol(given_roll)
                               if meta_stack==[]:
                                   errorh('No student found with this Roll no.')
                               else:
                                   table.delete(*table.get_children())
                                   for stack in meta_stack:
                                       table.insert('',END,values=stack)
                           else:
                               table.delete(*table.get_children())

                               for vals22 in defaultinfo:
                                   table.insert('', END, values=vals22)

#===================================================================================================================================================================================

#===================================================================    FACULTY REGISTRATION    ===================================================================================

def newemployee():
    win=Toplevel()
    win.geometry('850x700+0+0')
    win.resizable(False,False)
    center=' '*110
    win.title(center+'Faculty Registration Pannel')
    win.iconbitmap(win,cg_logo)
    win.focus()

    def errorinfo(tag,xc,xy):
        wobjGlobal.customlabels(scrollablecan, tag, None, None, xc, xy, 2, 1, fg='red')

    # Objects of Mainframe
    wobjGlobal = Mainframe2()
    wfobj1 = Mainframe2()
    wfobj2 = Mainframe2()
    wfobj3 = Mainframe2()
    wfobj4 = Mainframe2()
    wfobj5 = Mainframe2()
    wfobj6 = Mainframe2()
    wfobj7 = Mainframe2()
    wfobj10 = Mainframe2()
    wfobj11 = Mainframe2()
    wfobj12 = Mainframe2()
    wfobj13 = Mainframe2()
    wfobj14 = Mainframe2()
    wfobj15 = Mainframe2()
    wfobj16 = Mainframe2()
    wfobj17 = Mainframe2()
    wfobj18 = Mainframe2()
    wfobj19 = Mainframe2()

    #---------------------------------DIVIDERS----------------------

    holderframe=wobjGlobal.customframes(win,850,720,'green',0,0)
    scrollablecan=Canvas(holderframe,width=1355,height=720)
    scrollablecan.pack(side=LEFT,expand=True,fill=BOTH)

    divider1=scrollablecan.create_line(25,190,800,190,fill='black',width=1)

    #--------Display Pic-----------------------------------
    dpfac=wfobj19.customcan(scrollablecan,150,150,'white',30,20)
    #------------------------------Personal details-------------------------------
    #-----title combobox--------

    wobjGlobal.customlabels(scrollablecan,'Title : ','none',None,200,30)
    stafftitle=wfobj1.customcombobox(scrollablecan,'Select',staff_title,22,325,30)

    wobjGlobal.customlabels(scrollablecan,'Department : ','none',None,510,30)
    wfobj2.customcombobox(scrollablecan,'Select',departments,22,640,30)

    wobjGlobal.customlabels(scrollablecan,"First Name : ",'none',None,200,80)#                LEFT SIDE FIELDS
    wfobj3.userEntry(scrollablecan,325,85,25)

    wobjGlobal.customlabels(scrollablecan,"Last Name :",'none',None,510,80)#                 RIGHT SIDE FIELDS
    wfobj4.userEntry(scrollablecan,640,85,25)

    fphno=wobjGlobal.customlabels(scrollablecan,'Phone No. : ','none',None,200,130)
    wfobj5.userintentry(scrollablecan,325,135,25)

    fphno2=wobjGlobal.customlabels(scrollablecan,'Phone No. 2 : ','none',None,510,130)
    wfobj6.userintentry(scrollablecan,640,135,25)
    #========---------=========----------=========--------------==========--------

    studob=wobjGlobal.customlabels(scrollablecan,'D.O.B :','none',None,25,240)
    month=wfobj7.customcombobox(scrollablecan,'select',None,20,100,240)

    wobjGlobal.customlabels(scrollablecan,'Emp ID :','none',None,280,240)
    wfobj10.genralentry(scrollablecan,360,240,25)

    empadhar=wobjGlobal.customlabels(scrollablecan,'Adhaar No. :','none',None,540,235)
    wfobj11.userintentry(scrollablecan,640,240,25)

    stucountry=wobjGlobal.customlabels(scrollablecan,'Country :','none',None,25,300)
    wfobj12.userEntry(scrollablecan,100,300,25)

    stucity=wobjGlobal.customlabels(scrollablecan,'City :','none',None,280,300)
    wfobj13.userEntry(scrollablecan,360,300,25)

    stupin=wobjGlobal.customlabels(scrollablecan,'PIN Code :','none',None,540,290)
    wfobj14.userintentry(scrollablecan,640,290,25)

    stuemail=wobjGlobal.customlabels(scrollablecan,'E-mail :','none',None,25,360)
    wfobj15.emailentry(scrollablecan,100,360,25)

    stugender=wobjGlobal.customlabels(scrollablecan,'Gender :','none',None,280,360)
    wfobj16.customcombobox(scrollablecan,'Select Gender',['Male','Female','Others'],20,360,360)

    wobjGlobal.customlabels(scrollablecan,'Stipend :','none',None,540,360)
    feeentry=wfobj17.userintentry(scrollablecan,640,360,25)
    wfobj17.setintegerentry(0)

    wobjGlobal.customlabels(scrollablecan,'Address :','none',None,25,430)
    wfobj18.txtarea(scrollablecan,82,2,130,420)

    wobjGlobal.customlabels(scrollablecan,'Resume :','none',None,25,500)

    #---------------------------- EMP ID -------------------------------
    def allocatingempid(event):
        titlesel=wfobj1.getcombodata()
        if titlesel==staff_title[3]:
            staff_empidlist.insert(0,'Empas')
            wfobj10.setgenraluser(staff_empidlist[0])

        elif titlesel==staff_title[2]:
            staff_empidlist.insert(0,'Emppr')
            wfobj10.setgenraluser(staff_empidlist[0])

        elif titlesel==staff_title[1]:
            staff_empidlist.insert(0,'Emphod')
            wfobj10.setgenraluser(staff_empidlist[0])

        elif titlesel==staff_title[0]:
            staff_empidlist.insert(0,'Empd')
            wfobj10.setgenraluser(staff_empidlist[0])

        else:
            staff_empidlist.insert(0,'Lib')
            wfobj10.setgenraluser(staff_empidlist[0])

    stafftitle.bind('<<ComboboxSelected>>',allocatingempid)

    #----------------DATES------------------
    def example3(event):
        def print_sel():
            print(cal.selection_get())
            month.set(cal.selection_get())
            top.destroy()

        top = Toplevel(win)

        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand2",year=1999)
        cal.pack(fill="both", expand=True)
        Button(top, text="Submit",width=15,height=1, command=print_sel,bg='green',fg='white').pack()

    month.bind('<ButtonRelease-1>',example3)


    #-----------------------------FOOTER FRAME----------------------------
    footer=wobjGlobal.customframes(scrollablecan,9000,50,'steelblue',0,650)

    def errorhandleing(message):
        messagebox.showerror('Invalid Entry',message,parent=win)

    def getting_values():

        #------------------------------------------
        faculty_title = wfobj1.getcombodata()
        depart = wfobj2.getcombodata()
        first_name = wfobj3.getuserentry()
        last_name = wfobj4.getuserentry()
        emp_phone=wfobj5.getint()
        emp_phone2=wfobj6.getint()
        emp_id=wfobj10.getgenralentrydata()
        #--------------dates-------------------------------
        monthofdob = wfobj7.getcombodata()

        finaldob = str(monthofdob)
        #-----------------------------------------------------
        genderdata = wfobj16.getcombodata()
        email=wfobj15.getemail()
        # --------------------------------------
        country_name = wfobj12.getuserentry()
        city_name = wfobj13.getuserentry()
        addressofstu = wfobj18.gettext()

        phno = list(wfobj5.getint())
        phno2 = list(wfobj6.getint())
        pinno = list(wfobj14.getint())
        adhaarcardno = list(wfobj11.getint())
        #----------EXCEPTION HANDELING----------------------



        if faculty_title=='Select' or faculty_title=='':

            errorhandleing("Please select title of employee.")

        elif depart=='Select' or depart=='':
            errorhandleing("Please select department for employee.")

        elif first_name=='':
            errorhandleing('Please enter Name')

        elif last_name=='':
            errorhandleing('Please enter surname')

        elif phno==[]:
            errorhandleing('Enter Phone No.')

        elif phno2==[]:
            errorhandleing('Enter second Phone No.')

        elif monthofdob=='select' or monthofdob=='':
            errorhandleing('Select Month For D.O.B')

        elif emp_id=='':
            errorhandleing('Enter the new Employee ID for Employee.')

        elif country_name=='':
            errorhandleing('Enter the country name')

        elif city_name=='':
            errorhandleing('Enter the name of city')

        elif pinno==[]:
            errorhandleing('Enter the PIN no.')

        elif email==False:
            errorhandleing('Please enter a valid email in "@gmail.com" format.')

        elif adhaarcardno=='':
            errorhandleing('Please enter a valid Adhaar card no.')


        elif genderdata=='Select Gender' or genderdata=='':
            errorhandleing('Please select Gender')

        elif addressofstu=='\n':
            errorhandleing('Enter your address')

        else:
            idclash = existing_empid()
            if emp_id in idclash:
                messagebox.showerror('Already Exist','This employee id is already been assigned to someone with this title in this department.',parent=win)
            else:
                if len(phno) == 10:
                        fphno.config(fg='black')

                        if len(phno2)==10:
                            if len(pinno) == 6:
                                stupin.config(fg='black')

                                if len(adhaarcardno) == 12:
                                    # errorinfo('',582,300)
                                    empadhar.config(fg='black')
                                    try:
                                        eph = int(wfobj5.getint())
                                        eph2 = int(wfobj6.getint())
                                        pincode = int(wfobj14.getint())
                                        adhaar = int(wfobj11.getint())
                                        stipend = wfobj17.getint()
                                    except ValueError:
                                        fphno.config(fg='red')
                                        fphno2.config(fg='red')
                                        stupin.config(fg='red')

                                        messagebox.showerror('Invalid', 'Some of the information you entered is invalid',parent=win)
                                    else:
                                        resp=messagebox.askokcancel('Confirmation!','The entered data will be saved in database.',parent=win)
                                        if resp==True:
                                            faculty_data_warehouse(first_name,last_name,emp_id,faculty_title,depart,eph,eph2,finaldob,genderdata,
                                                  email,stipend,country_name,city_name,
                                                  pincode,adhaar,addressofstu)
                                            messagebox.showinfo('Saved!','Your data is saved sucessfully!',parent=win)
                                            win.destroy()

                                        else:
                                            pass
                                else:
                                    empadhar.config(fg='red')
                                    messagebox.showerror('Invalid Value', 'Please enter a valid 12-digit Adhaar Card Number.',parent=win)
                            else:
                                stupin.config(fg='red')
                                messagebox.showerror('Inavalid Value', 'Please enter a valid 6-digit PIN Code.',parent=win)
                        else:
                            messagebox.showerror('Invalid', 'Please enter a valid 10-digit phone no.',parent=win)

                else:
                        errorinfo('',800,135)
                        fphno.config(fg='red')
                        messagebox.showerror('Invalid','Please enter a valid 10-digit phone no.',parent=win)


    def fac_img():
        if wfobj10.getgenralentrydata()=='':
            messagebox.showerror('Invalid Attempt','Please fill the form completely first.',parent=win)
        else:
            idclash = existing_empid()
            if wfobj10.getgenralentrydata() in idclash:
                messagebox.showerror('Already Exist!','This employee ID already Exist',parent=win)
            else:
                imgpath=filedialog.askopenfile(parent=win,title='Choose Image',filetype=[('png Files','*.png')])
                if imgpath !=None:
                    renamedimg=str(imgpath.name).split("/")[-1]
                    image_name_splitted = str(renamedimg).split('.')

                    print(image_name_splitted[0] + '.png')

                    imgfile_dp = Image.open(imgpath.name)
                    imgfile_dp.thumbnail(dp_max_size)
                    imgfile_dp.save(f'{facdir_path}//{image_name_splitted[0]}.png')

                    insert_facultyimg(wfobj10.getgenralentrydata(),f'{image_name_splitted[0]}.png')
                    wfobj19.image(f'{facdir_path}//{image_name_splitted[0]}.png',0,0)
                    but.destroy()

                else:
                    pass


    def cv():
        if wfobj10.getgenralentrydata()=='':
            messagebox.showerror('Invalid Attempt','First fill complete form.',parent=win)
        else:
            import shutil
            filepath=filedialog.askopenfile(parent=win,title='Select Resume PDF',filetypes=[('pdf Files','*.pdf')])
            if filepath !=None:
                filenameouttapath=str(filepath.name).split('/')[-1]
                print(filenameouttapath)
                upload_resume(wfobj10.getgenralentrydata(),filenameouttapath)
                shutil.copy2(filepath.name,fac_cv_file_path)
                wobjGlobal.customlabels(scrollablecan,'','none 20 bold',None,300,498,fg='green')

                def openresume():
                    os.startfile(f'{fac_cv_file_path}//{filenameouttapath}')

                wobjGlobal.custombuttons(scrollablecan,'See Resume',20,1,openresume,350,500,fg='white',bg='#323b38')
            else:
                pass

    def exit():
        toremove=fetchfacimg(wfobj10.getgenralentrydata())
        cvtorem=resume_files(wfobj10.getgenralentrydata())
        if cvtorem !=[]:
            removecv(wfobj10.getgenralentrydata())
            os.remove(f'{fac_cv_file_path}//{cvtorem[0]}')
        else:
            pass
        if toremove !=[]:
            os.remove(f'{fac_displaypic_path}//{toremove[0]}')
            deletingfacimg_onaccount(wfobj10.getgenralentrydata())
        else:
            pass
        win.destroy()
    #-----------------------------BUTTONS---------------------------------
    wobjGlobal.custombuttons(footer,'Submit',10,1,getting_values,50,10)
    wobjGlobal.custombuttons(footer,'Cancel',10,1,exit,170,10)
    wobjGlobal.custombuttons(scrollablecan,'Choose file',20,1,cv,130,500,fg='white',bg='#323b38')
    but = wobjGlobal.custombuttons(dpfac, 'upload img.', 10, 1, fac_img, 35, 60)

    win.mainloop()

#======================================================================= MAIN UPDATE OPERATIONS FUNCTION FOR FACULTY =============================================================

def showdataoffaculty(table):
    #-----------------------------------------------information out of table------------------------

    rowinfo=table.focus()

    contentinfo=table.item(rowinfo)
    metafacdata=contentinfo['values']
    print(metafacdata)
    if metafacdata =='':
        return
    else:


        win = Toplevel()
        win.geometry('850x700+0+0')
        win.resizable(False, False)
        center = ' ' * 110
        win.title(center + 'Faculty Update Pannel')

        def errorinfo(tag, xc, xy):
            wobjGlobal.customlabels(scrollablecan1, tag, None, None, xc, xy, 2, 1, fg='red')


        # Objects of Mainframe
        wobjGlobal = Mainframe2()
        wfobju1 = Mainframe2()
        wfobju2 = Mainframe2()
        wfobju3 = Mainframe2()
        wfobju4 = Mainframe2()
        wfobju5 = Mainframe2()
        wfobju6 = Mainframe2()
        wfobju7 = Mainframe2()
        wfobju10 = Mainframe2()
        wfobju11 = Mainframe2()
        wfobju12 = Mainframe2()
        wfobju13 = Mainframe2()
        wfobju14 = Mainframe2()
        wfobju15 = Mainframe2()
        wfobju16 = Mainframe2()
        wfobju17 = Mainframe2()
        wfobju18 = Mainframe2()
        wfobju19 = Mainframe2()

        # ---------------------------------DIVIDERS----------------------

        holderframe1 = wobjGlobal.customframes(win, 850, 720, 'green', 0, 0)
        scrollablecan1 = Canvas(holderframe1, width=1355, height=720)
        scrollablecan1.pack(side=LEFT, expand=True, fill=BOTH)

        divider1 = scrollablecan1.create_line(25, 190, 800, 190, fill='black', width=1)

        # --------Display Pic-----------------------------------
        dpoffac = wfobju19.customcan(scrollablecan1, 150, 150, 'white', 30, 20)

        #---------------------   IMAGE PROCESSING SCRIPT------------------

        idwithdp=fetchfacid()
        print(idwithdp)

        if metafacdata[2] in idwithdp:
            print(metafacdata[2])
            imgnamefac=fetchfacimg(metafacdata[2])
            if imgnamefac[0] !=None:
                print(imgnamefac)
                wfobju19.image(f'{fac_displaypic_path}//{imgnamefac[0]}',0,0)
                print('i was here')
            else:
                print('one level down')
                wfobju19.image(f'{fac_displaypic_path}//defaultdp.png',0,0)
        else:
            print('more')
            wfobju19.image(f'{fac_displaypic_path}//defaultdp.png', 0, 0)

        #-------------------------------------------------------------------
        #------------------   PDF CV PROCESSING SCRIPT    ------------------

        idwithcv=resume_empid()

        if metafacdata[2] in idwithcv:
            print(metafacdata[2])
            cvfilename=resume_files(metafacdata[2])
            print(cvfilename)
            if cvfilename[0] !=None:
                wobjGlobal.customlabels(scrollablecan1, '', 'none 20 bold', None, 130, 498, fg='green')
                def openresume():
                    os.startfile(f'{fac_cv_file_path}//{cvfilename[0]}')
                    print(f'{fac_cv_file_path}//{cvfilename[0]}')
                wobjGlobal.custombuttons(scrollablecan1,'Open Resume',20,1,openresume,200,500,fg='white',bg='#323b38')

            else:
                wobjGlobal.customlabels(scrollablecan1, '', 'none 20 bold', None, 130, 498, fg='red')
        else:
            wobjGlobal.customlabels(scrollablecan1, '', 'none 20 bold', None, 130, 498, fg='red')

        # ------------------------------Personal details-------------------------------
        # -----title combobox--------
        wobjGlobal.customlabels(scrollablecan1, 'Title : ', 'none', None, 200, 30)
        stafftitle = wfobju1.customcombobox(scrollablecan1, 'Select', staff_title, 22, 325, 30)

        wobjGlobal.customlabels(scrollablecan1, 'Department : ', 'none', None, 510, 30)
        staff_depart=wfobju2.customcombobox(scrollablecan1, 'Select', departments, 22, 640, 30)

        wobjGlobal.customlabels(scrollablecan1, "First Name : ", 'none', None, 200, 80)  # LEFT SIDE FIELDS
        wfobju3.userEntry(scrollablecan1, 325, 85, 25)

        wobjGlobal.customlabels(scrollablecan1, "Last Name :", 'none', None, 510, 80)  # RIGHT SIDE FIELDS
        wfobju4.userEntry(scrollablecan1, 640, 85, 25)

        fphno = wobjGlobal.customlabels(scrollablecan1, 'Phone No. : ', 'none', None, 200, 130)
        wfobju5.userintentry(scrollablecan1, 325, 135, 25)

        fphno2 = wobjGlobal.customlabels(scrollablecan1, 'Phone No. 2 : ', 'none', None, 510, 130)
        wfobju6.userintentry(scrollablecan1, 640, 135, 25)
        # ========---------=========----------=========--------------==========--------

        studob = wobjGlobal.customlabels(scrollablecan1, 'D.O.B :', 'none', None, 25, 240)
        month = wfobju7.customcombobox(scrollablecan1, '', None, 20, 100, 240)

        wobjGlobal.customlabels(scrollablecan1, 'Emp ID :', 'none', None, 280, 240)
        wfobju10.genralentry(scrollablecan1, 360, 240, 25)

        empadhar = wobjGlobal.customlabels(scrollablecan1, 'Adhaar No. :', 'none', None, 540, 235)
        wfobju11.userintentry(scrollablecan1, 640, 240, 25)

        stucountry = wobjGlobal.customlabels(scrollablecan1, 'Country :', 'none', None, 25, 300)
        wfobju12.userEntry(scrollablecan1, 100, 300, 25)

        stucity = wobjGlobal.customlabels(scrollablecan1, 'City :', 'none', None, 280, 300)
        wfobju13.userEntry(scrollablecan1, 360, 300, 25)

        stupin = wobjGlobal.customlabels(scrollablecan1, 'PIN Code :', 'none', None, 540, 290)
        wfobju14.userintentry(scrollablecan1, 640, 290, 25)

        stuemail = wobjGlobal.customlabels(scrollablecan1, 'E-mail :', 'none', None, 25, 360)
        wfobju15.emailentry(scrollablecan1, 100, 360, 25)

        stugender = wobjGlobal.customlabels(scrollablecan1, 'Gender :', 'none', None, 280, 360)
        genderdat=wfobju16.customcombobox(scrollablecan1, 'Select Gender', ['Male', 'Female', 'Others'], 20, 360, 360)

        wobjGlobal.customlabels(scrollablecan1, 'Stipend :', 'none', None, 540, 360)
        feeentry = wfobju17.userintentry(scrollablecan1, 640, 360, 25)
        wfobju17.setintegerentry(0)

        wobjGlobal.customlabels(scrollablecan1, 'Address :', 'none', None, 25, 430)
        addr=wfobju18.txtarea(scrollablecan1, 82, 2, 130, 420)

        wobjGlobal.customlabels(scrollablecan1, 'Resume :', 'none', None, 25, 500)

        #=================================================  SETTING DATA    ============================================================================

        title=stafftitle.set(metafacdata[3])
        deparment = staff_depart.set(metafacdata[4])
        firstname=wfobju3.setuserentry(metafacdata[0])
        lastname=wfobju4.setuserentry(metafacdata[1])
        phone1=wfobju5.setintegerentry(metafacdata[5])
        phone2=wfobju6.setintegerentry(metafacdata[6])

        dobm=month.set(metafacdata[7])

        empid=wfobju10.setgenraluser(metafacdata[2])
        adaahar=wfobju11.setintegerentry(metafacdata[14])
        countryoffac=wfobju12.setuserentry(metafacdata[11])
        cityoffac=wfobju13.setuserentry(metafacdata[12])
        pinno=wfobju14.setintegerentry(metafacdata[13])
        emailen=wfobju15.setemail(metafacdata[9])
        genderoffac=genderdat.set(metafacdata[8])
        salary=wfobju17.setintegerentry(metafacdata[10])
        wfobju18.cleartext()
        address=addr.insert('end',metafacdata[15])


        #===============================================================================================================================================

        # ----------------DATES------------------
        def dobempupdate(event):
            def print_sel():
                print(cal.selection_get())
                month.set(cal.selection_get())
                top.destroy()

            top = Toplevel(win)

            cal = Calendar(top,
                           font="Arial 14", selectmode='day',
                           cursor="hand2", year=1999)
            cal.pack(fill="both", expand=True)
            Button(top, text="Submit", width=15, height=1, command=print_sel, bg='green', fg='white').pack()

        month.bind('<ButtonRelease-1>', dobempupdate)

        # -----------------------------FOOTER FRAME----------------------------
        footer = wobjGlobal.customframes(scrollablecan1, 9000, 50, 'steelblue', 0, 650)

        def errorhandleing(message):
            messagebox.showerror('Invalid Entry', message, parent=win)

        def getting_values():

            # ------------------------------------------
            faculty_title = wfobju1.getcombodata()
            depart = wfobju2.getcombodata()
            first_name = wfobju3.getuserentry()
            last_name = wfobju4.getuserentry()
            emp_phone = wfobju5.getint()
            emp_phone2 = wfobju6.getint()
            emp_id = wfobju10.getgenralentrydata()
            # --------------dates-------------------------------
            monthofdob = wfobju7.getcombodata()

            finaldob = str(monthofdob)
            # -----------------------------------------------------
            genderdata = wfobju16.getcombodata()
            email = wfobju15.getemail()
            # --------------------------------------
            country_name = wfobju12.getuserentry()
            city_name = wfobju13.getuserentry()
            addressofstu = wfobju18.gettext()

            phno = list(wfobju5.getint())
            phno2 = list(wfobju6.getint())
            pinno = list(wfobju14.getint())
            adhaarcardno = list(wfobju11.getint())
            # ----------EXCEPTION HANDELING----------------------

            if faculty_title == 'Select' or faculty_title == '':

                errorhandleing("Please select title of employee.")

            elif depart == 'Select' or depart == '':
                errorhandleing("Please select department for employee.")

            elif first_name == '':
                errorhandleing('Please enter Name')

            elif last_name == '':
                errorhandleing('Please enter surname')

            elif phno == []:
                errorhandleing('Enter Phone No.')

            elif phno2 == []:
                errorhandleing('Enter second Phone No.')

            elif monthofdob == 'select' or monthofdob == '':
                errorhandleing('Select Month For D.O.B')

            elif emp_id == '':
                errorhandleing('Enter the new Employee ID for Employee.')

            elif country_name == '':
                errorhandleing('Enter the country name')

            elif city_name == '':
                errorhandleing('Enter the name of city')

            elif pinno == []:
                errorhandleing('Enter the PIN no.')

            elif email == False:
                errorhandleing('Please enter a valid email in "@gmail.com" format.')

            elif adhaarcardno == '':
                errorhandleing('Please enter a valid Adhaar card no.')


            elif genderdata == 'Select Gender' or genderdata == '':
                errorhandleing('Please select Gender')

            elif addressofstu == '\n':
                errorhandleing('Enter your address')

            else:
                idclash = existing_empid()
                if emp_id!=metafacdata[2] and  emp_id in idclash:

                        messagebox.showerror('Already Exist',
                                             'This employee id is already been assigned to someone with this title in this department.',
                                             parent=win)

                else:
                    if len(phno) == 10:
                        fphno.config(fg='black')

                        if len(phno2) == 10:
                            if len(pinno) == 6:
                                stupin.config(fg='black')

                                if len(adhaarcardno) == 12:
                                    # errorinfo('',582,300)
                                    empadhar.config(fg='black')
                                    try:
                                        eph = int(wfobju5.getint())
                                        eph2 = int(wfobju6.getint())
                                        pincode = int(wfobju14.getint())
                                        adhaar = int(wfobju11.getint())
                                        stipend = wfobju17.getint()
                                    except ValueError:
                                        fphno.config(fg='red')
                                        fphno2.config(fg='red')
                                        stupin.config(fg='red')

                                        messagebox.showerror('Invalid', 'Some of the information you entered is invalid',
                                                             parent=win)
                                    else:
                                        resp = messagebox.askokcancel('Confirmation!',
                                                                      'The entered data will be saved in database.',
                                                                      parent=win)
                                        if resp == True:
                                            updatefacultydata(first_name, last_name, emp_id, faculty_title, depart,
                                                                   eph, eph2, finaldob, genderdata,
                                                                   email, stipend, country_name, city_name,
                                                                   pincode, adhaar, addressofstu,metafacdata[2])
                                            messagebox.showinfo('Saved!', 'Your data is saved sucessfully!', parent=win)
                                            win.destroy()
                                        else:
                                            pass
                                else:
                                    empadhar.config(fg='red')
                                    messagebox.showerror('Invalid Value',
                                                         'Please enter a valid 12-digit Adhaar Card Number.', parent=win)
                            else:
                                stupin.config(fg='red')
                                messagebox.showerror('Inavalid Value', 'Please enter a valid 6-digit PIN Code.', parent=win)
                        else:
                            messagebox.showerror('Invalid', 'Please enter a valid 10-digit phone no.', parent=win)

                    else:
                        errorinfo('', 800, 135)
                        fphno.config(fg='red')
                        messagebox.showerror('Invalid', 'Please enter a valid 10-digit phone no.', parent=win)

        def fac_img():
            if wfobju10.getgenralentrydata()=="":
                messagebox.showerror('Fatal Error','An Error occured, Please check all the details are filled properly.',parent=win)
            else:
                existingfacidwithdp=fetchfacid()
                pathtofacimg=filedialog.askopenfile(parent=win,title='Choose to update',filetype=[('png Files', '*.png'), ('jpeg Files', '*.jpeg'),
                                                                    ('jpg Files', '*.jpg')])
                imgnameouttadir=str(pathtofacimg.name).split('/')[-1]

                if list(imgnameouttadir).count('.') == 1:
                    image_name_splitted = str(imgnameouttadir).split('.')

                    print(image_name_splitted[0] + '.png')

                    imgfile_dp = Image.open(pathtofacimg.name)
                    imgfile_dp.thumbnail(dp_max_size)
                    imgfile_dp.save(f'{facdir_path}//{image_name_splitted[0]}.png')

                    if metafacdata[2] in existingfacidwithdp:
                        updatefacimg(metafacdata[2],f'{image_name_splitted[0]}.png')
                        wfobju19.image(f'{facdir_path}//{image_name_splitted[0]}.png',0,0)
                    else:
                        insert_facultyimg(metafacdata[2],f'{image_name_splitted[0]}.png')
                        wfobju19.image(f'{facdir_path}//{image_name_splitted[0]}.png',0,0)

        def cv():
            if wfobju10.getgenralentrydata()=='':
                messagebox.showerror('Invalid Attempt','First fill complete form.',parent=win)
            else:
                existingempidofcv=resume_empid()

                import shutil
                filepath=filedialog.askopenfile(parent=win,title='Select Resume PDF',filetypes=[('pdf Files','*.pdf')])
                if filepath !=None:
                    filenameouttapath=str(filepath.name).split('/')[-1]
                    print(filenameouttapath)
                    files = os.walk(fac_cv_file_path)
                    processed_files = next(files)[2]
                    if filenameouttapath not in processed_files:
                        if metafacdata[2] in existingempidofcv:
                            update_resume(filenameouttapath,wfobju10.getgenralentrydata())
                            shutil.copy2(filepath.name,fac_cv_file_path)
                            wobjGlobal.customlabels(scrollablecan1,'','none 20 bold',None,510,498,fg='green')
                        else:
                            upload_resume(wfobju10.getgenralentrydata(),filenameouttapath)
                            shutil.copy2(filepath.name,fac_cv_file_path)
                            wobjGlobal.customlabels(scrollablecan1,'','none 20 bold',None,510,498,fg='green')
                    else:
                        respforcv=messagebox.askyesno('Already Exist','A file withs name already exist. Do you want to remove that file and proceed upload?',parent=win)
                        if respforcv==True:
                            os.remove(f'{fac_cv_file_path}//{filenameouttapath}')
                            update_resume(filenameouttapath,wfobju10.getgenralentrydata())
                            shutil.copy2(filepath.name,fac_cv_file_path)
                            wobjGlobal.customlabels(scrollablecan1,'','none 20 bold',None,510,498,fg='green')
                            messagebox.showinfo('Uploaded',
                                                'Previous file is removed and new file is uploaded successfully.',
                                                parent=win)
                        else:
                            messagebox.showinfo('Upload Paused','CV Upload is currently paused.\n\nTry rename the file and upload.',parent=win)
                else:
                    pass

        def exit():
            win.destroy()

        def deletefacdata():
            response=messagebox.askyesno('Confirmation','The selected data will be deleted from the database and so does the user account associated with this.'
                                               'Do you want to delete?\nConfirm with Yes/No.',parent=win)
            if  response==True:
                delete_faculty(metafacdata[2])
                deletefacultyuseraccount(metafacdata[2])
                deletingfacimg_onaccount(metafacdata[2])
                removecv(metafacdata[2])

                messagebox.showinfo('Deleted!','Data is successfully deleted.',parent=win)
                win.destroy()

            else:
                pass

        def removeDp():
            checkaval = fetchfacid()

            if metafacdata[2] in checkaval:
                torm=fetchfacimg(metafacdata[2])
                deletingfacimg(metafacdata[2])

                wfobju19.image(f"{fac_displaypic_path}//defaultdp.png",0,0)
                os.remove(f'{fac_displaypic_path}//{torm[0]}')
            else:
                print('gotcha!')




        #-----------------------------BUTTONS---------------------------------
        wobjGlobal.custombuttons(footer,'Update',10,1,getting_values,50,10)
        wobjGlobal.custombuttons(footer,'Delete',10,1,deletefacdata,150,10)
        wobjGlobal.custombuttons(footer,'Cancel',10,1,exit,250,10)

        wobjGlobal.custombuttons(scrollablecan1,'Update Resume',20,1,cv,370,500,fg='white',bg='#323b38')
        wobjGlobal.custombuttons(scrollablecan1,'Update Image',20,1,fac_img,25,550,fg='white',bg='#323b38')
        wobjGlobal.custombuttons(scrollablecan1,'Remove Image',20,1,removeDp,200,550,fg='white',bg='#323b38')


        win.mainloop()


#========================================================================= MAIN UPDATE OPERATIONS FUNCTION =========================================================================

def showdat(table):
        row = table.focus()
        content_info = table.item(row)
        metadata = content_info['values']
        if metadata=='':
            return
        else:

            win = Toplevel()
            width = 850
            win.resizable(False, False)
            center = ' ' * 110
            x = (win.winfo_screenwidth() // 2) - (width // 2)
            y = 20
            win.geometry(f'{width}x700+{x}+{y}')
            win.iconbitmap(cg_logo)
            win.title(center + 'Student Update Panel')
            win.focus()


            def errorinfo(tag, xc, xy):
                wobjGlobal.customlabels(scrollablecan, tag, None, None, xc, xy, 2, 1, fg='red')

            # Objects of Mainframe
            wobjGlobal = Mainframe2()

            wobj1 = Mainframe2()
            wobj2 = Mainframe2()
            wobj3 = Mainframe2()
            wobj4 = Mainframe2()
            wobj5 = Mainframe2()
            wobj6 = Mainframe2()
            wobj7 = Mainframe2()
            wobj8 = Mainframe2()
            wobj9 = Mainframe2()
            wobj10 = Mainframe2()
            wobj13 = Mainframe2()
            wobj14 = Mainframe2()
            wobj15 = Mainframe2()
            wobj16 = Mainframe2()
            wobj17 = Mainframe2()
            wobj18 = Mainframe2()
            wobj19 = Mainframe2()
            wobj20 = Mainframe2()
            wobj23 = Mainframe2()
            wobj24 = Mainframe2()
            wobj25 = Mainframe2()
            wobj26 = Mainframe2()
            wobj27 = Mainframe2()
            wobj28 = Mainframe2()
            wobj30 = Mainframe2()
            wobj31 = Mainframe2()
            wobj32 = Mainframe2()

            # ---------------------------------DIVIDERS----------------------

            holderframe = wobjGlobal.customframes(win, 850, 720, 'green', 0, 0)
            scrollablecan = Canvas(holderframe, width=1355, height=720)
            scrollablecan.pack(side=LEFT, expand=True, fill=BOTH)

            divider1 = scrollablecan.create_line(25, 190, 800, 190, fill='black', width=1)
            divider2 = scrollablecan.create_line(25, 280, 800, 280, fill='black', width=1)
            divider3 = scrollablecan.create_line(610, 300, 610, 600, fill='black', width=1)
            divider4=scrollablecan.create_line(830,20,830,610,fill='black',width=1)

            # --------Display Pic-----------------------------------
            dp = wobj30.customcan(scrollablecan, 150, 150, 'white', 30, 20)

            # --------------------------------------------------- I M A G E PROCESSING-------------------------------------------------------------
            assign_img = {}

            roldat = fetch_rol2()

            if str(metadata[2]) in roldat:
                imgpathdat = fetch_image(str(metadata[2]))

                if imgpathdat[0] !=None:
                    wobj30.image(f'{studir_path}//{imgpathdat[0]}',0,0)

                else:
                    wobj30.image(f'{studir_path}//defaultuser.png', 0, 0)

            else:
                wobj30.image(f'{studir_path}//defaultuser.png',0,0)


            #---------------------------------------------------------------------------------------------------------------------------------------

            # ------------------------------Personal details-------------------------------
            stufirstname = wobjGlobal.customlabels(scrollablecan, 'First Name : ', 'none', None, 200, 30)
            wobj1.userEntry(scrollablecan, 325, 35, 25)

            stulastname = wobjGlobal.customlabels(scrollablecan, 'Last Name: ', 'none', None, 510, 30)
            wobj2.userEntry(scrollablecan, 640, 35, 25)

            stufathername = wobjGlobal.customlabels(scrollablecan, "Father's Name: ", 'none', None, 200,80)
            wobj3.userEntry(scrollablecan, 325, 85, 25)

            stumothername = wobjGlobal.customlabels(scrollablecan, "Mother's Name :", 'none', None, 510, 80)
            wobj5.userEntry(scrollablecan, 640, 85, 25)

            stuparentcontact = wobjGlobal.customlabels(scrollablecan, 'Parents Contact : ', 'none', None, 200, 130)
            wobj4.userintentry(scrollablecan, 325, 135, 25)

            stuphoneno = wobjGlobal.customlabels(scrollablecan, 'Phone no.: ', 'none', None, 510, 130)
            wobj6.userintentry(scrollablecan, 640, 135, 25)

            # ---------------------------Year branch course-----------------------
            stucourse = wobjGlobal.customlabels(scrollablecan, 'Course :', 'none', None, 25, 200)
            c = wobj7.customcombobox(scrollablecan, '-Select Course-', courses, 20, 100, 200)

            stubranch = wobjGlobal.customlabels(scrollablecan, 'Branch :', 'none', None, 290, 200)
            br=wobj8.customcombobox(scrollablecan, '-Select Branch-', None, 20, 370, 200)

            stuyear = wobjGlobal.customlabels(scrollablecan, 'Year :', 'none', None, 550, 200)
            yo = wobj9.customcombobox(scrollablecan, '-Select Year-', None, 20, 610, 200)

            wobjGlobal.customlabels(scrollablecan, 'Fee :', 'none', None, 25, 530)
            feeentry = wobj27.userintentry(scrollablecan, 130, 530, 25)
            wobj27.setintegerentry(0)

            wobjGlobal.customlabels(scrollablecan, 'Transport Service :', 'none', None, 300, 530)
            trans = wobj28.customcombobox(scrollablecan, 'select', None, 15, 450, 534)
            # -------------------------------------------------------------------

            studob = wobjGlobal.customlabels(scrollablecan, 'D.O.B :', 'none', None, 25, 240)
            month = wobj10.customcombobox(scrollablecan, '', None, 20, 100, 240)

            sturollno = wobjGlobal.customlabels(scrollablecan, 'Roll No :', 'none', None, 290, 240)
            wobj13.genralentry(scrollablecan, 370, 240, 25)

            stusem = wobjGlobal.customlabels(scrollablecan, 'SEM :', 'none', None, 550, 240)
            semset=wobj14.customcombobox(scrollablecan, '-Semester-', None, 20, 610, 240)

            stucountry = wobjGlobal.customlabels(scrollablecan, 'Country :', 'none', None, 25, 300)
            wobj15.userEntry(scrollablecan, 130, 300, 25)

            stucity = wobjGlobal.customlabels(scrollablecan, 'City :', 'none', None, 25, 340)
            wobj16.userEntry(scrollablecan, 130, 340, 25)

            stupin = wobjGlobal.customlabels(scrollablecan, 'PIN Code :', 'none', None, 25, 380)
            wobj17.userintentry(scrollablecan, 130, 380, 25)

            stuemail = wobjGlobal.customlabels(scrollablecan, 'E-mail :', 'none', None, 25, 420)
            wobj18.emailentry(scrollablecan, 130, 420, 25)
            # ------------------------------------------------------------------------------------- LEFT...
            stuadhaar = wobjGlobal.customlabels(scrollablecan, 'Adhaar No.:', 'none', None, 320, 300)
            wobj19.userintentry(scrollablecan, 430, 300, 25)

            stureg = wobjGlobal.customlabels(scrollablecan, 'Date of Reg. :', 'none', None, 320, 340)
            regmonth = wobj20.customcombobox(scrollablecan, '',None, 20, 430, 340)
            # regd=wobj21.customcombobox(scrollablecan, '-D-', None, 5, 480, 340)
            # regy=wobj22.customcombobox(scrollablecan, '-Y-', yearofdob, 5, 530, 340)

            stubatch = wobjGlobal.customlabels(scrollablecan, 'Batch :', 'none', None, 320, 380)
            batchstart = wobj23.customcombobox(scrollablecan, 'Year', yearofdob, 5, 430, 380)
            wobjGlobal.customlabels(scrollablecan, 'To', 'none', None, 495, 380)
            batchend=wobj24.customcombobox(scrollablecan, 'Year', ['select from'], 5, 530, 380)

            stugender = wobjGlobal.customlabels(scrollablecan, 'Gender :', 'none', None, 320, 420)
            genderdata=wobj26.customcombobox(scrollablecan, 'Select Gender', ['Male', 'Female', 'Others'], 20, 430, 420)

            stuaddress = wobjGlobal.customlabels(scrollablecan, 'Address :', 'none', None, 25, 460)
            candidateaddress=wobj25.txtarea(scrollablecan, 56, 2, 130, 460)


            #-------------provided documents---------------

            wobjGlobal.customlabels(scrollablecan, 'Documents Provided', 'none', None, 638, 290)
            docinfo=wobj32.txtarea(scrollablecan,20,15,625,320)
            for docs in metadata[-1]:
                docinfo.insert('end',docs)
            docinfo.config(state=DISABLED)

    #-0000000000000000000000000000000000000000000000000000000000000000======================== SETTING DATA ======================0000000000000000000000000000000000000000000000---------

            Name=wobj1.setuserentry(metadata[0])
            LastNamme=wobj2.setuserentry(metadata[1])
            RollNo=wobj13.setgenraluser(metadata[2])
            Course=c.set(metadata[3])
            Branch=br.set(metadata[4])
            Year=yo.set(metadata[5])
            Semester=semset.set(metadata[6])
            Father=wobj3.setuserentry(metadata[7])
            Mother=wobj5.setuserentry(metadata[8])
            ParentContact=wobj4.setintegerentry(metadata[9])
            DOB_Month=month.set(metadata[10])
            PhoneNo=wobj6.setintegerentry(metadata[11])
            EMAil=wobj18.setemail(metadata[12])
            Country=wobj15.setuserentry(metadata[13])
            City=wobj16.setuserentry(metadata[14])
            PINNO=wobj17.setintegerentry(metadata[15])
            AdhaarCard=wobj19.setintegerentry(metadata[16])
            Reg_M=regmonth.set(metadata[17])
            batch_spliting=str(metadata[18]).split('-')
            Batch_Start=batchstart.set(batch_spliting[0])
            Batch_end=batchend.set(batch_spliting[1])
            Gender=genderdata.set(metadata[19])
            FEE=wobj27.setintegerentry(metadata[20])
            TransPort=trans.set(metadata[21])
            candidateaddress.delete(1.0,END)
            Address=candidateaddress.insert('end',metadata[22])

            # ---------------------------SUGGESTION EVENT BINDINGS---------------------------------
            def tranfeeconfig(transincluded):
                wobj27.setintegerentry(transincluded)

            def hover_transport(event):
                selected_choice = wobj28.getcombodata()
                if selected_choice == 'Yes':
                    rawfee = int(wobj27.getint())
                    transincluded = rawfee + 20000
                    tranfeeconfig(transincluded)
                elif selected_choice == 'No':
                    accord_branch = wobj7.getcombodata()
                    if accord_branch == 'B.Tech':
                        tranfeeconfig(btech_fee[0])
                    elif accord_branch == 'BSc':
                        tranfeeconfig(35000)

            trans.bind('<<ComboboxSelected>>', hover_transport)

            # --------------------branch year semester events------------------------------------------

            def branch_config(brlist):
                br.config(values=brlist)
            def year_config(yearl):
                yo.config(values=yearl)

            def hover_select(event):
                selected_course_for_branch = wobj7.getcombodata()
                print(selected_course_for_branch)

                if selected_course_for_branch == 'B.Tech':
                    branch_config(btech_fileld)
                    year_config(btech_years)
                    # sem_config(semester_btech)
                    # ------transport-----------
                    wobj27.setintegerentry(btech_fee[0])
                    trans.config(values=choice_list)

                elif selected_course_for_branch == 'BSc':
                    branch_config(bsc_fields)
                    year_config(ug_years)
                    # sem_config(semester_bsc)
                    # -----transport-----------
                    wobj27.setintegerentry(bsc_fee[0])
                    trans.set('select')

                else:
                    branch_config(['No Information'])
                    year_config(['No Information'])
                    # sem_config('No Data')

            c.bind('<<ComboboxSelected>>', hover_select)

            # ---------------semester suggestion------------
            def sem_config(semdata):
                wobj14.customcombobox(scrollablecan, '-Semester-', semdata, 20, 610, 240)

            def accord_year_sem(event):
                sel_year = wobj9.getcombodata()
                if sel_year == '1st year':
                    sem_config(['1st semester', '2nd semester'])
                elif sel_year == '2nd year':
                    sem_config(['3rd semester', '4th semester'])
                elif sel_year == '3rd year':
                    sem_config(['5th semester', '6th semester'])
                elif sel_year == '4th year':
                    sem_config(['7th semester', '8th semester'])
                else:
                    sem_config(['select year first'])

            yo.bind('<<ComboboxSelected>>', accord_year_sem)

            # ----------------DATES------------------
            def dobupdating(event):
                def print_sel():
                    print(cal.selection_get())
                    month.set(cal.selection_get())
                    top.destroy()

                top = Toplevel(win)

                cal = Calendar(top,
                               font="Arial 14", selectmode='day',
                               cursor="hand2", year=1999)
                cal.pack(fill="both", expand=True)
                Button(top, text="Submit", width=15, height=1, command=print_sel, bg='green', fg='white').pack()

            month.bind('<ButtonRelease-1>', dobupdating)

            def dorupdate(event):
                def print_sel():
                    print(cal.selection_get())
                    regmonth.set(cal.selection_get())
                    top.destroy()

                top = Toplevel(win)

                cal = Calendar(top,
                               font="Arial 14", selectmode='day',
                               cursor="hand2")
                cal.pack(fill="both", expand=True)
                Button(top, text="Submit", width=15, height=1, command=print_sel, bg='green', fg='white').pack()

            regmonth.bind('<ButtonRelease-1>', dorupdate)

            # ---------------BATCH-------------------
            def endbatchconfig(dataofendbatch):
                wobj24.customcombobox(scrollablecan, 'Year', dataofendbatch, 5, 530, 380)

            def batchhover(event):
                startdate = int(wobj23.getcombodata())
                onindex = yearofdob.index(startdate)

                endbatchconfig(yearofdob[onindex:])

            batchstart.bind('<<ComboboxSelected>>', batchhover)
            # ------------------------------------------------------------------------------------------------------

            # -----------------------------FOOTER FRAME----------------------------
            footer = wobjGlobal.customframes(scrollablecan, 9000, 50, 'steelblue', 0, 650)

            def errorhandleing(message):
                messagebox.showerror('Invalid Entry', message, parent=win)

            def getting_values():

                # ------------------------------------------
                first_name = wobj1.getuserentry()
                last_name = wobj2.getuserentry()
                father_name = wobj3.getuserentry()
                mother_name = wobj5.getuserentry()
                # ----------COMBODATA-------------------
                course_name = wobj7.getcombodata()
                branch_name = wobj8.getcombodata()
                year_name = wobj9.getcombodata()
                rollno = wobj13.getgenralentrydata()
                # --------------dates-------------------------------
                monthofdob = wobj10.getcombodata()

                monthofreg = wobj20.getcombodata()

                finaldob = str(monthofdob)
                finaldateofreg = str(monthofreg)

                batchstarting = wobj23.getcombodata()
                batchending = wobj24.getcombodata()
                batch_duration = batchstarting + '-' + batchending
                # -----------------------------------------------------
                genderdata = wobj26.getcombodata()
                email = wobj18.getemail()

                sem = wobj14.getcombodata()
                transport_service = wobj28.getcombodata()
                # --------------------------------------
                country_name = wobj15.getuserentry()
                city_name = wobj16.getuserentry()
                addressofstu = wobj25.gettext()

                pcontact = list(wobj4.getint())
                phno = list(wobj6.getint())
                pinno = list(wobj17.getint())
                adhaarcardno = list(wobj19.getint())
                # ----------EXCEPTION HANDELING----------------------
                if first_name == '':
                    errorhandleing('Please enter Name')

                elif last_name == '':
                    errorhandleing('Please enter surname')

                elif father_name == '':

                    errorhandleing("Please enter Father's Name")

                elif mother_name == '':
                    errorhandleing("Please enter Mother's Name")

                elif pcontact == []:
                    errorhandleing('Enter Parents Contact')

                elif phno == []:
                    errorhandleing('Enter your Phone No.')

                elif course_name == '-Select Course-' or course_name == '':
                    errorhandleing('Please select a course to proceed.')

                elif branch_name == '-Select Branch-' or branch_name == '':
                    errorhandleing('Please select the Branch associated with that course')

                elif year_name == '-Select Year-' or year_name == '':
                    errorhandleing('Select the year')

                elif monthofdob == 'select' or monthofdob == '':
                    errorhandleing('Select Month For D.O.B')

                elif rollno == '':
                    errorhandleing('Enter the new Roll No. of Student')

                elif sem == '-Semester-' or sem == '':
                    errorhandleing('select the Semester')

                elif country_name == '':
                    errorhandleing('Enter the country name')

                elif city_name == '':
                    errorhandleing('Enter the name of city')

                elif pinno == []:
                    errorhandleing('Enter the PIN no.')

                elif email == False:
                    errorhandleing('Please enter a valid email in "@gmail.com" format.')

                elif adhaarcardno == '':
                    errorhandleing('Please enter a valid Adhaar card no.')

                elif monthofreg == 'select' or monthofreg == '':
                    errorhandleing('Selct the month of registration')

                elif batchstarting == 'Year' or batchstarting == '':
                    errorhandleing('Select batch starting year')
                elif batchending == 'Year' or batchending == '':
                    errorhandleing('Select batch ending year')

                elif genderdata == 'Select Gender' or genderdata == '':
                    errorhandleing('Please select Gender')

                elif addressofstu == '':
                    errorhandleing('Enter your address')

                elif transport_service == 'select' or transport_service == '':
                    errorhandleing('Please select transport services')

                else:
                    if len(pcontact) == 10:
                        if len(phno) == 10:
                            errorinfo('', 800, 135)
                            stuphoneno.config(fg='black')
                            wobjGlobal.customlabels(scrollablecan, '', None, None, 800, 135, 2, 1)

                            if len(pinno) == 6:
                                errorinfo('', 290, 382)
                                stupin.config(fg='black')

                                if len(adhaarcardno) == 12:
                                    errorinfo('', 582, 300)
                                    stuadhaar.config(fg='black')

                                    try:
                                        parentscontact = int(wobj4.getint())
                                        phoneno = int(wobj6.getint())
                                        pincode = int(wobj17.getint())
                                        adhaar = int(wobj19.getint())
                                        feeofstu = int(wobj27.getint())
                                    except ValueError:
                                        messagebox.showerror('Invalid', 'Some of the information you entered is invalid')
                                    else:

                                        responce = messagebox.askyesno('Confirmation',
                                                                       'The entered data will be Update in database.\nConfirm with yes/no',parent=win)
                                        if responce == True:
                                            try:
                                                updates_in_datawarehouse(first_name, last_name, rollno, course_name, branch_name,
                                                               year_name, sem, father_name, mother_name, parentscontact,
                                                               finaldob,
                                                               phoneno, email, country_name, city_name, pincode, adhaar,
                                                               finaldateofreg,
                                                               batch_duration, genderdata, feeofstu, transport_service,
                                                               addressofstu,metadata[2])

                                                messagebox.showinfo('Success','Data Updated Successfully.',parent=win)
                                                win.destroy()
                                            except sqlite3.IntegrityError:
                                                messagebox.showerror('Alredy assigned','This roll no. is already exists',parent=win)
                                        else:
                                            pass
                                else:
                                    errorinfo('', 582, 300)
                                    stuadhaar.config(fg='red')
                                    messagebox.showerror('Invalid Value',
                                                         'Please enter a valid 12-digit Adhaar Card Number.')
                            else:
                                errorinfo('', 290, 382)
                                stupin.config(fg='red')
                                messagebox.showerror('Inavalid Value', 'Please enter a valid 6-digit PIN Code.')
                        else:
                            errorinfo('', 800, 135)
                            stuphoneno.config(fg='red')
                            messagebox.showerror('Invalid', 'Please enter a valid 10-digit phone no.')
                    else:
                        errorinfo('', 425, 135)
                        stuparentcontact.config(fg='red')
                        messagebox.showerror('Invalid', 'Please enter a valid 10-digit phone no.')

            def exit():
                win.destroy()

            def removing_dp():
                import os
                rollno=wobj13.getgenralentrydata()
                if rollno=='':
                    messagebox.showerror('Fatal Error','Cann not romove image without Roll No.',parent=win)
                else:
                    toremove=fetch_image(rollno)
                    if toremove[0]!=None:
                        os.remove(f'{stu_displaypic_path}//{toremove[0]}')
                        deleting_img(rollno)
                        wobj30.image(f'{stu_displaypic_path}//defaultuser.png', 0, 0)
                    else:
                        messagebox.showerror('Critical Error','There is no pic to remove',parent=win)


            def updatingdp():
                rol = metadata[2]
                if rol ==wobj13.getgenralentrydata():
                    if wobj13.getgenralentrydata() == '':
                        messagebox.showerror('Fatal Error',
                                             "Can't assign the pic withot full information.\nFill the form completely first.",parent=win)
                    else:
                        from tkinter import filedialog

                        path = filedialog.askopenfile(parent=win,title='Choose Image',filetype=[('png Files', '*.png'), ('jpeg Files', '*.jpeg'),
                                                                    ('jpg Files', '*.jpg')])
                        renamed_path = str(path.name).split('/')[-1]
                        if list(renamed_path).count('.')==1:
                            try:
                                image_name_spliting=str(renamed_path).split('.')


                                rolwithpic=fetch_rol2()
                                if metadata[2] not in rolwithpic:
                                    image_insert(metadata[2],f'{image_name_spliting[0]}.png')

                                    imgfile_dp = Image.open(path.name)
                                    imgfile_dp.thumbnail(dp_max_size)
                                    imgfile_dp.save(f'{studir_path}//{image_name_spliting[0]}.png')

                                    imgwithrol=fetch_image(rol)
                                    wobj30.image(f'{studir_path}//{imgwithrol[0]}', 0, 0)
                                else:
                                    updating_image(rol,f'{image_name_spliting[0]}.png')
                                    imgfile_dp = Image.open(path.name)
                                    imgfile_dp.thumbnail(dp_max_size)
                                    imgfile_dp.save(f'{studir_path}//{image_name_spliting[0]}.png')
                                    fetched_image = fetch_image(rol)
                                    wobj30.image(f'{studir_path}//{fetched_image[0]}', 0, 0)
                            except sqlite3.IntegrityError:
                                messagebox.showerror('Already Exist ~~ Rare Case!','The Image name alredy exist in database.\n\nTry Renaming the image.',parent=win)
                        else:
                                messagebox.showwarning("Parsing Error!",'Your image file contain too many  ". DOTS" in name.\nPlease rename the file and try again.',parent=win)
                else:
                    messagebox.showwarning("Fatal Error!",
                                           'You are trying to assign the new image to other rollno. which is not possible until you update the rollno. first.',
                                           parent=win)

            def deleting_student_fromdatabase():
                response=messagebox.askyesno('Confirmation!',"The data and user account"
                                                             "associated with this data will be deleted permanently."
                                                             "This action can't be undone\nAre you Sure to delete this?",parent=win)
                if response==True:
                    detectingAccount=studentrollno()

                    detectingImage=fetch_rol2()
                    deleteing_student(metadata[2],metadata[3],metadata[4],metadata[5],metadata[6])

                    if metadata[2] in detectingAccount:
                        deleting_student_account(metadata[2])
                    else:
                        pass
                    if metadata[2] in detectingImage:
                        #-------deleting image from directory--------
                        delimg=fetch_image(metadata[2])
                        if delimg!=[None]:
                            import os
                            os.remove(f'{studir_path}//{delimg[0]}')
                        else:
                            pass
                        #------------------------------------------
                        deleting_image_onaccount(metadata[2])

                    messagebox.showinfo('Deleted!','The data is deleted successfully from Database.',parent=win)
                    win.destroy()
                else:
                    pass
            # -----------------------------BUTTONS---------------------------------
            wobjGlobal.custombuttons(footer, 'Update', 10, 1, getting_values, 50, 10)
            wobjGlobal.custombuttons(footer,'Delete',10,1,deleting_student_fromdatabase,150,10)
            wobjGlobal.custombuttons(footer, 'Close', 10, 1, exit, 250, 10)

            wobjGlobal.custombuttons(scrollablecan,'Update Profile Pic',15,1,updatingdp,25,590,bg='#323b38',fg='white')
            wobjGlobal.custombuttons(scrollablecan, 'Remove Profile Pic', 15, 1, removing_dp, 150, 590,bg='#323b38',fg='white')

            win.mainloop()

class FacultyView:

    def displayFaculty(self,frameno,intro,winname,butname1,butname2,butname3,butname4):

        #---------objects--------
        self.globalobj=Mainframe2()
        self.obj1=Mainframe2()
        self.obj2=Mainframe2()
        self.obj3=Mainframe2()
        self.obj4=Mainframe2()
        self.obj5=Mainframe2()
        self.obj6=Mainframe2()
        self.obj7=Mainframe2()
        self.obj8=Mainframe2()


        #===========================================    scrollable area and tree view   ====================================================

        from tkinter.ttk import Treeview

        self.infoframe = Frame(frameno, width=500, height=500, bg='white')
        self.infocan = self.globalobj.packedFrame(frameno, 200, 200, '#f2dd22', LEFT, fill=Y)

        self.xscrollbar = Scrollbar(self.infoframe, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)

        self.yscrollbar = Scrollbar(self.infoframe, orient=VERTICAL)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.table = Treeview(self.infoframe,
                              columns=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                       '16'), xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)

        self.table.heading('1', text='NAME')
        self.table.heading('2', text='SURNAME')
        self.table.heading('3', text="Employee ID NO.")
        self.table.heading('4', text="TITLE")
        self.table.heading('5', text='DEPARTMENT')
        self.table.heading('6', text='PHONE NO.')
        self.table.heading('7', text='BACKUP CONTACT')
        self.table.heading('8', text="D.O.B")
        self.table.heading('9', text="GENDER")
        self.table.heading('10', text='E-MAIL')
        self.table.heading('11', text='STIPEND')
        self.table.heading('12', text='COUNTRY')
        self.table.heading('13', text='CITY')
        self.table.heading('14', text='PIN CODE')
        self.table.heading('15', text='ADHAAR CARD NO.')
        self.table.heading('16', text='ADDRESS')

        self.table['show']='headings'

        self.table.pack(side=TOP, fill=BOTH, expand=1)

        self.xscrollbar.config(command=self.table.xview)
        self.yscrollbar.config(command=self.table.yview)
        self.infoframe.pack(side=RIGHT, fill=BOTH, expand=1)
        def callupdate(event):
            showdataoffaculty(self.table)

        self.table.bind('<ButtonRelease-1>',callupdate)

#=============================================================================================================
        self.datainputframe1 = self.globalobj.customframes(self.infocan, 200, 720, '#f2dd22', 0, 28)

        self.globalobj.customlabels(self.datainputframe1, winname, 'none', 'black', 0, 10,22,1,fg='white')

        self.titlename=self.globalobj.customlabels(self.datainputframe1, 'Title :', 'none', '#f2dd22', 10, 40)
        self.branch_choice = self.obj4.customcombobox(self.datainputframe1, 'Select', staff_title, 25, 10, 70)

        self.departname=self.globalobj.customlabels(self.datainputframe1, 'Department :', 'none', '#f2dd22', 10, 100)
        self.obj3.customcombobox(self.datainputframe1, 'Select', departments, 25, 10, 130)

        self.stipendammount= self.globalobj.customlabels(self.datainputframe1, 'Stipend :', 'none', '#f2dd22', 10, 170)
        self.obj1.userintentry(self.datainputframe1, 10, 200,28)

        self.empID=self.globalobj.customlabels(self.datainputframe1, 'Employee ID :', 'none', '#f2dd22', 10, 240)
        self.obj2.genralentry(self.datainputframe1, 10, 270, 28)




        def cleartxt():
            self.table.delete(*self.table.get_children())
        def exit():
            self.infocan.destroy()
            self.infoframe.destroy()
            self.datainputframe1.destroy()
            butback.destroy()
            buthlp.destroy()

        # -----------------------------------------------------------------------------

        butback = self.globalobj.custombuttons(intro, 'Back ', 10, 1, exit, 1130, 13)
        buthlp = self.globalobj.custombuttons(intro, 'Help ', 10, 1, None, 1230, 13)

        butback.bind('<Enter>',lambda event,bc=butback: bc.config(bg="red",fg='white'))
        butback.bind('<Leave>',lambda event,bc=butback: bc.config(bg="white",fg='black'))

        buthlp.bind('<Enter>',lambda event,bc=buthlp: bc.config(bg="green",fg='white'))
        buthlp.bind('<Leave>',lambda event,bc=buthlp: bc.config(bg="white",fg='black'))
        # -----------------------------------------------------------------------------

        def fetchfromdatabase():
            title=self.obj4.getcombodata()
            depart=self.obj3.getcombodata()
            salary=self.obj1.getint()
            empID=self.obj2.getgenralentrydata()

            def emptydathandle(mess):
                messagebox.showerror('Empty Data',mess,parent=frameno)


            allcolumn,supernarrow,tds,tde,td,tse,ts,te,onlytitle,dse,ds,de,onlydepartment,se,onlystipend,onlyid=fetch_faculty_fromdatabase(title,depart,salary,empID)

            #=========0000000000000000000000000000---------0000000000-------MAIN FETCH OPERATIONS FOR FACULTY--------00000000000--------------000000000000000000000------------------
            if title !='Select' and title !='':
                if depart !='Select' and depart !='':
                    if salary !='':
                        if empID !='':
                            if supernarrow==[]:
                                emptydathandle('No record found for the given data.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val1 in supernarrow:
                                    self.table.insert('',END,values=val1)
                        else:
                            if tds==[]:
                                emptydathandle('No data for this stipend.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val2 in tds:
                                    self.table.insert('',END,values=val2)
                    else:
                        if empID !='':
                            if tde==[]:
                                emptydathandle('There is no faculty with this title in this department with the given Employee ID')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val3 in tds:
                                    self.table.insert('',END,values=val3)
                        else:
                            if td==[]:
                                emptydathandle('No faculty in this department with this title.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val4 in td:
                                    self.table.insert('', END, values=val4)
                else:
                    if salary !='':
                        if empID !='':
                            if tse==[]:
                                emptydathandle('Rare case.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val5 in tse:
                                    self.table.insert('',END,values=val5)
                        else:
                            if ts==[]:
                                emptydathandle('No faculty is getting this ammount of salary.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val6 in ts:
                                    self.table.insert('',END,values=val6)
                    else:
                        if empID !='':
                            if te==[]:
                                emptydathandle('This employee ID is not assigned to any faculty member.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val7 in te:
                                    self.table.insert('',END,values=val7)
                        else:
                            if onlytitle==[]:
                                emptydathandle("There is no faculty with this title.")
                            else:
                                self.table.delete(*self.table.get_children())
                                for val8 in onlytitle:
                                    self.table.insert('',END,values=val8)
            else:
                if depart !='Select' and depart !='':
                    if salary !='':
                        if empID !='':
                            if dse==[]:
                                emptydathandle('There is no one in this department with thisstipend or employeeID.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val9 in dse:
                                    self.table.insert('', END, values=val9)
                        else:
                            if ds==[]:
                                emptydathandle('No faculty is getting this salry in this department')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val10 in ds:
                                    self.table.insert('',END,values=val10)
                    else:
                        if empID !='':
                            if de==[]:
                                emptydathandle('No one in this department with this employee ID.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val15 in de:
                                    self.table.insert('',END,values=val15)
                        else:
                            if onlydepartment==[]:
                                emptydathandle('Rare case!\nNo faculty for this department.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val11 in onlydepartment:
                                    self.table.insert('', END, values=val11)
                else:
                    if salary !='':
                        if empID !="":
                            if se==[]:
                                emptydathandle('Not Relevent data were given.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val12 in se:
                                    self.table.insert('',END,values=val12)
                        else:
                            if onlystipend==[]:
                                emptydathandle('No Faculty found for this stipend')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val13 in onlystipend:
                                    self.table.insert('',END,values=val13)
                    else:
                        if empID !='':
                            if onlyid==[]:
                                emptydathandle('This ID is not assigned to any faculty member.')
                            else:
                                self.table.delete(*self.table.get_children())
                                for val14 in onlyid:
                                    self.table.insert('',END,values=val14)
                        else:
                            self.table.delete(*self.table.get_children())
                            for val in allcolumn:
                                self.table.insert('',END,values=val)



        self.butfetch=self.globalobj.custombuttons(self.datainputframe1, butname1, 10, 1, fetchfromdatabase, 100, 500)
        self.butcancel=self.globalobj.custombuttons(self.datainputframe1, butname2, 10, 1, exit, 10, 500)
        self.butadvance = self.globalobj.custombuttons(self.datainputframe1, butname3, 10, 1, None, 10, 530)
        self.butclear = self.globalobj.custombuttons(self.datainputframe1, butname4, 10, 1, cleartxt, 100, 530)


class Accounts_Managments:

    def accountDisplay(self,frameno,intro,uniqueid,winname,actype):
        self.globalobj = Mainframe2()
        self.obj1 = Mainframe2()
        self.obj2 = Mainframe2()
        self.obj3 = Mainframe2()
        self.obj4 = Mainframe2()
        self.obj5 = Mainframe2()
        self.obj6 = Mainframe2()
        self.obj7 = Mainframe2()
        self.obj8 = Mainframe2()

        # ===========================================    scrollable area and tree view   ====================================================

        from tkinter.ttk import Treeview

        self.infoframe = Frame(frameno, width=500, height=500, bg='white')
        self.infocan = self.globalobj.packedFrame(frameno, 200, 200, '#f2dd22', LEFT, fill=Y)

        self.xscrollbar = Scrollbar(self.infoframe, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)

        self.yscrollbar = Scrollbar(self.infoframe, orient=VERTICAL)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.table = Treeview(self.infoframe,
                              columns=('1', '2', '3', '4', '5'), xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)

        self.table.heading('1', text='Name')
        self.table.heading('2', text='Phone No.')
        self.table.heading('3', text=uniqueid)
        self.table.heading('4', text='Username')
        self.table.heading('5', text='Password')

        self.table['show'] = 'headings'

        self.table.pack(side=TOP, fill=BOTH, expand=1)

        self.xscrollbar.config(command=self.table.xview)
        self.yscrollbar.config(command=self.table.yview)
        self.infoframe.pack(side=RIGHT, fill=BOTH, expand=1)

        self.datainputframe1 = self.globalobj.customframes(self.infocan, 200, 720, '#f2dd22', 0, 28)

        self.globalobj.customlabels(self.datainputframe1, winname, 'none', 'black', 0, 10, 22, 1, fg='white')

        self.titlename = self.globalobj.customlabels(self.datainputframe1, 'Username :', 'none', '#f2dd22', 10, 40)
        self.branch_choice = self.obj4.genralentry(self.datainputframe1, 10, 70,25)

        self.departname = self.globalobj.customlabels(self.datainputframe1, uniqueid, 'none', '#f2dd22', 10,100)
        self.obj3.genralentry(self.datainputframe1,10, 130,25)

        def closepanel():
            self.infocan.destroy()
            self.infoframe.destroy()
            self.datainputframe1.destroy()
            butback.destroy()
            buthlp.destroy()

        # -----------------------------------------------------------------------------

        butback = self.globalobj.custombuttons(intro, 'Back ', 10, 1, closepanel, 1130, 13)
        buthlp = self.globalobj.custombuttons(intro, 'Help ', 10, 1, None, 1230, 13)

        butback.bind('<Enter>',lambda event,bc=butback: bc.config(bg="red",fg='white'))
        butback.bind('<Leave>',lambda event,bc=butback: bc.config(bg="white",fg='black'))

        buthlp.bind('<Enter>',lambda event,bc=buthlp: bc.config(bg="green",fg='white'))
        buthlp.bind('<Leave>',lambda event,bc=buthlp: bc.config(bg="white",fg='black'))
        # -----------------------------------------------------------------------------

        def deleting_account(event):
            rowall = self.table.focus()
            content_info1 = self.table.item(rowall)
            metadata1 = content_info1['values']

            responsetodel=messagebox.askyesno('Confirm Delete!',f'Selected Account  : \n\n        Username :   {metadata1[3]}\n\n        Rollno.      :   {metadata1[2]}'
            f'\n\nThe account will be deleted and so does the profile associated with this account.\n\nConfirm delete with Yes/No.',parent=frameno)

            if actype=='student':
                if responsetodel==True:
                    success=deletestudenuseraccount(metadata1[3],metadata1[2])
                    if success==1:
                        messagebox.showinfo('Success!','The Account is Deleted sucessfully!',parent=frameno)
                    else:
                        messagebox.showerror('Unknown Error! (Rare Case)',
                                             'Something went wrong!\nCan not delete this account as it might does not exist already.',parent=frameno)
                else:
                    pass
            else:
                if responsetodel==True:
                    suc=deletefacultyuseraccount(metadata1[2])
                    if suc==1:
                        messagebox.showinfo('Success!', 'The Account is Deleted sucessfully!', parent=frameno)
                    else:
                        messagebox.showerror('Unknown Error! (Rare Case)',
                                             'Something went wrong!\nCan not delete this account as it might does not exist already.',parent=frameno)
                else:
                    pass



        def fetchaccounts():
            def emptydatahandeler(mess):
                messagebox.showerror('User not Found',mess,parent=frameno)

            username = self.obj4.getgenralentrydata()
            userID = self.obj3.getgenralentrydata()

            #------------------------------------------------------------FETCH OPERATIONS-------------------------------------------------
            if actype=='student':

                defaultall,idofstu,u,uid=fetchingstudentaccount(username,userID)

                if username != '':
                    if userID != '':
                        if uid==[]:
                            emptydatahandeler('No match found for given data.')
                        else:
                            self.table.delete(*self.table.get_children())
                            for value1 in uid:
                                self.table.insert('',END,values=value1)
                    else:
                        if u==[]:
                            emptydatahandeler('No user found with this username.')
                        else:
                            self.table.delete(*self.table.get_children())
                            for value2 in u:
                                self.table.insert('',END,values=value2)
                else:
                    if userID != '':
                        if idofstu==[]:
                            emptydatahandeler('No user found for this Roll NO.')
                        else:
                            self.table.delete(*self.table.get_children())
                            for value3 in idofstu:
                                self.table.insert('',END,values=value3)
                    else:
                        if defaultall==[]:
                            emptydatahandeler('No data yet.\nMight be no one has signed Up for a student user account.')
                        else:
                            self.table.delete(*self.table.get_children())
                            for value4 in defaultall:
                                self.table.insert('',END,values=value4)
            else:
                defaultallfac,facid,facu,facuid=fetchingfacultyaccount(username,userID)

                if username != '':
                    if userID != '':
                        if facuid==[]:
                            emptydatahandeler('No matching data found for given information.')
                        else:
                            self.table.delete(*self.table.get_children())
                            for facval1 in facuid:
                                self.table.insert('',END,values=facval1)
                    else:
                        if facu==[]:
                            emptydatahandeler('No user found with this username.')
                        else:
                            self.table.delete(*self.table.get_children())
                            for facval2 in facu:
                                self.table.insert('',END,values=facval2)
                else:
                    if userID != '':
                        if facid==[]:
                            emptydatahandeler('No user found for this Employee ID.')
                        else:
                            self.table.delete(*self.table.get_children())
                            for facval3 in facid:
                                self.table.insert('',END,values=facval3)
                    else:
                        if defaultallfac==[]:
                            emptydatahandeler('No data yet,\n Might be no one has signed up for an employee account.')
                        else:
                            self.table.delete(*self.table.get_children())
                            for facval4 in defaultallfac:
                                self.table.insert('',END,values=facval4)

        self.table.bind('<ButtonRelease-1>',deleting_account)
        self.butfetch=self.globalobj.custombuttons(self.datainputframe1, 'Fetch', 10, 1, fetchaccounts, 100, 500)  #............... KEY BUTTON
        self.butcancel=self.globalobj.custombuttons(self.datainputframe1, 'Exit', 10, 1, closepanel, 10, 500)


class Dattoshow:

    def maindisplay(self, frameno,intro,windowname,task_no,butname1,butname2,butname3,butname4):

        # object of OOPS 2
        self.objoops21 = Mainframe2()
        self.objoops22 = Mainframe2()
        self.objoops23 = Mainframe2()
        self.objoops24 = Mainframe2()
        self.objoops25 = Mainframe2()
        self.objoops26 = Mainframe2()
        self.objoops225 = Mainframe2()

        self.globalobj=Mainframe2()

#                                          ====================== SCROLLABLE TEXT AREA =======================
        from tkinter.ttk import Treeview

        self.infoframe = Frame(frameno, width=500, height=500, bg='white')
        self.infocan = self.objoops21.packedFrame(frameno, 200, 200, '#f2dd22', LEFT, fill=Y)

        self.xscrollbar = Scrollbar(self.infoframe, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)

        self.yscrollbar = Scrollbar(self.infoframe, orient=VERTICAL)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.table = Treeview(self.infoframe, columns=('1', '2', '3', '4', '5', '6', '7','8','9','10','11','12','13','14','15',
                                                       '16','17','18','19','20','21','22','23','24'),
                              xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)
        self.table.heading('1',text='NAME')
        self.table.heading('2', text='SURNAME')
        self.table.heading('3', text="ROLL NO.")
        self.table.heading('4', text="COURSE")
        self.table.heading('5', text='BRANCH')
        self.table.heading('6', text='YEAR')
        self.table.heading('7', text='SEMESTER')
        self.table.heading('8', text="FATHER'S NAME")
        self.table.heading('9', text="MOTHER'S NAME")
        self.table.heading('10', text='PARENTS CONTACT')
        self.table.heading('11', text='D.O.B')
        self.table.heading('12', text='PHONE NO.')
        self.table.heading('13', text='E-MAIL')
        self.table.heading('14', text='COUNTRY')
        self.table.heading('15', text='CITY')
        self.table.heading('16', text='PIN CODE')
        self.table.heading('17', text='ADHAAR CARD')
        self.table.heading('18', text='D.O.R')
        self.table.heading('19', text='BATCH')
        self.table.heading('20', text='GENDER')
        self.table.heading('21', text='FEE')
        self.table.heading('22', text='TRANSPORT')
        self.table.heading('23', text='ADDRESS')
        self.table.heading('24', text='DOCUMENTS PROVIDED')

        self.table['show']='headings'

        self.table.column('1',width=100)
        self.table.column('2',width=100)
        self.table.column('3',width=100)
        self.table.column('4',width=100)
        self.table.column('5',width=100)
        self.table.column('6',width=70)
        self.table.column('7',width=90)
        self.table.column('8',width=100)
        self.table.column('9',width=100)
        self.table.column('10',width=100)
        self.table.column('11',width=80)
        self.table.column('12',width=100)
        self.table.column('13',width=150)
        self.table.column('14', width=100)
        self.table.column('15',width=100)
        self.table.column('16',width=100)
        self.table.column('17',width=100)
        self.table.column('18',width=80)
        self.table.column('19',width=80)
        self.table.column('20',width=70)
        self.table.column('21',width=80)
        self.table.column('22',width=70)
        self.table.column('23',width=250)
        self.table.column('24',width=250)


        self.table.pack(side=TOP, fill=BOTH, expand=1)

        self.xscrollbar.config(command=self.table.xview)
        self.yscrollbar.config(command=self.table.yview)
        self.infoframe.pack(side=RIGHT, fill=BOTH, expand=1)
        # def scrolling_speed(event):
        #     self.table.yview_scroll(int(-1*(event.delta/20)),'units')
        #
        #
        # self.table.bind_all('<MouseWheel>',scrolling_speed)


        def calling_display(event):
            showdat(self.table)

        self.table.bind('<ButtonRelease-1>',calling_display)


        #=============================================================================================================
        self.datainputframe1 = self.objoops21.customframes(self.infocan, 200, 720, '#f2dd22', 0, 28)

        self.objoops21.customlabels(self.datainputframe1, windowname, 'none', 'black', 0, 10,22,1,fg='white')

        self.cname=self.objoops21.customlabels(self.datainputframe1, 'Course Name :', 'none', '#f2dd22', 10, 40)
        self.branch_choice = self.objoops22.customcombobox(self.datainputframe1, 'select', courses, 25, 10, 70)

        self.bname=self.objoops21.customlabels(self.datainputframe1, 'Branch Name :', 'none', '#f2dd22', 10, 100)
        self.bn=self.objoops24.customcombobox(self.datainputframe1, 'select', None, 25, 10, 130)

        self.yname= self.objoops21.customlabels(self.datainputframe1, 'Select Year :', 'none', '#f2dd22', 10, 170)
        self.yn=self.objoops25.customcombobox(self.datainputframe1, 'select', None, 25, 10, 200)

        self.yname= self.objoops21.customlabels(self.datainputframe1, 'Select Semester :', 'none', '#f2dd22', 10, 240)
        self.semselfs=self.objoops225.customcombobox(self.datainputframe1, 'select',None, 25, 10, 270)


        self.roll=self.objoops21.customlabels(self.datainputframe1, 'Roll No. :', 'none', '#f2dd22', 10, 300)
        self.objoops23.genralentry(self.datainputframe1, 10, 330, 28)

        def semconfig(event):
            yeartouse=self.yn.get()
            print('YO!')
            if yeartouse == '1st year':
                self.semselfs.config(values=['select','1st semester', '2nd semester'])
            elif yeartouse == '2nd year':
                self.semselfs.config(values=['select','3rd semester', '4th semester'])
            elif yeartouse == '3rd year':
                self.semselfs.config(values=['select','5th semester', '6th semester'])
            elif yeartouse == '4th year':
                self.semselfs.config(values=['select','7th semester', '8th semester'])
            else:
                self.semselfs.config(values=['select','select year first'])
        self.yn.bind("<<ComboboxSelected>>",semconfig)


        def courseSelection(info):
            self.bn.config(values=info)

        def yearSelection(info1):
            self.yn.config(values=info1)
        def semselction(s):
            self.semselfs.config(values=s)

        def foo(event):
            meta=self.branch_choice.get()
            if meta=='B.Tech' or meta=='M.Tech':
                courseSelection(btech_fileld)
                if meta=='M.Tech':
                    yearSelection(btech_years[0:3])
                else:
                    yearSelection(btech_years)

            elif meta=='BSc/UG':
                courseSelection(bsc_fields)
                yearSelection(ug_years)
            else:
                courseSelection(['No information'])
                yearSelection(['No information'])

        self.branch_choice.bind('<<ComboboxSelected>>',foo)

        def fetching():

            selected_course=self.branch_choice.get()
            selected_branch=self.objoops24.getcombodata()
            given_roll=self.objoops23.getgenralentrydata()
            selected_year=self.objoops25.getcombodata()
            selected_semester=self.objoops225.getcombodata()

            narrowfetch, cbys, cbyr, cby, cbsr, cbs, cbr, cb, cs, onlyc, cys, cy, bysr, bys, byr, by, bsr, bs, onlyb, ys, onlyyear, onlysem, defaultinfo = fetchstudentsdata(
                selected_course,
                selected_year,
                selected_branch,
                given_roll,
                selected_semester)
            maindata=(narrowfetch, cbys, cbyr, cby, cbsr, cbs, cbr, cb, cs, onlyc, cys, cy, bysr, bys, byr, by, bsr, bs, onlyb, ys, onlyyear, onlysem, defaultinfo)

            fetch(selected_course,selected_year,selected_branch,given_roll,frameno,selected_semester,self.table,maindata)

#=====================================================================================================================================================================================
        def exit():
            self.infocan.destroy()
            self.infoframe.destroy()
            self.datainputframe1.destroy()
            butback.destroy()
            buthlp.destroy()

        # -----------------------------------------------------------------------------

        butback = self.globalobj.custombuttons(intro, 'Back ', 10, 1, exit, 1130, 13)
        buthlp = self.globalobj.custombuttons(intro, 'Help ', 10, 1, None, 1230, 13)

        butback.bind('<Enter>',lambda event,bc=butback: bc.config(bg="red",fg='white'))
        butback.bind('<Leave>',lambda event,bc=butback: bc.config(bg="white",fg='black'))

        buthlp.bind('<Enter>',lambda event,bc=buthlp: bc.config(bg="green",fg='white'))
        buthlp.bind('<Leave>',lambda event,bc=buthlp: bc.config(bg="white",fg='black'))
        # -----------------------------------------------------------------------------

        def cleartxt():
            self.table.delete(*self.table.get_children())
        def set_default_filter():
            self.branch_choice.set('select')
            self.bn.set('select')
            self.yn.set('select')
            self.semselfs.set('select')
            self.objoops23.setgenraluser('')

        self.butfetch=self.objoops21.custombuttons(self.datainputframe1, butname1, 10, 1, None, 100, 500)
        self.butcancel=self.objoops21.custombuttons(self.datainputframe1, butname2, 10, 1, exit, 10, 500)
        self.butadvance = self.objoops21.custombuttons(self.datainputframe1, butname3, 10, 1, set_default_filter, 10, 530)
        self.butclear = self.objoops21.custombuttons(self.datainputframe1, butname4, 10, 1, cleartxt, 100, 530)

        if task_no==1:
            self.butfetch.config(command=fetching)

#======================================================================= HOVER KEYS BINDING =======================================================================================
        self.butfetch.bind('<Enter>',lambda event,bf=self.butfetch: bf.config(bg="black",fg='white'))
        self.butcancel.bind('<Enter>',lambda event,bc=self.butcancel: bc.config(bg="red",fg='white'))
        self.butadvance.bind('<Enter>',lambda event,ba=self.butadvance: ba.config(bg="green",fg='white'))
        self.butclear.bind('<Enter>',lambda event,bcc=self.butclear: bcc.config(bg="black",fg='white'))

        self.butfetch.bind('<Leave>',lambda event,bf=self.butfetch: bf.config(bg="white",fg='black'))
        self.butcancel.bind('<Leave>',lambda event,bc=self.butcancel: bc.config(bg="white",fg='black'))
        self.butadvance.bind('<Leave>',lambda event,ba=self.butadvance: ba.config(bg="white",fg='black'))
        self.butclear.bind('<Leave>',lambda event,bcc=self.butclear: bcc.config(bg="white",fg='black'))
# ===================================================================================================================================================================================