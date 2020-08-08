from oops import *
from login_frontend import signupfun
import threading
from oops2 import Mainframe2
from backend import Verification,login_load,can_but
from database import *
from info import cg_logo, components_path



fonttxt = 'Ebrima'


def proceed():
    root= Tk()
    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()
    root.geometry(f"{w}x{h}+0+0")
    root.minsize(800,600)
    root.title('Campus Guide Software')
    root.iconbitmap(cg_logo)
    root.state('zoomed')
    root.update()
    root.attributes('-topmost',True)
    root.after(10,root.attributes('-topmost',False))
    # root.bind('<FocusIn>',lambda event :root.focus()  )
    # root.focus_get()
    root.focus()


    # FUNCTIONS OF FRONTEND
    obj11=Verification()
    # Mainframe objects

    obj1=Mainframe()
    obj2=Mainframe()
    obj3=Mainframe2()
    obj4=Mainframe2()
    obj5=Mainframe2()


    def about_section():
        import webbrowser
        about_root=Toplevel()
        about_root.resizable(0,0)
        bgc='white'
        txtclr='#323b38'
        about_root.iconbitmap(about_root,cg_logo)
        about_root.title('About Us --')
        about_root.focus()

        width=900
        hight=550
        x=(about_root.winfo_screenwidth()//2)-width//2
        y=(about_root.winfo_screenheight()//2)-hight//2

        about_root.geometry(f'{width}x{hight}+{x}+{y}')

        global_objab=Mainframe2()
        root_can=global_objab.customcan(about_root,width,hight,bgc,0,0)

        p=PhotoImage(file=f'{components_path}//cg_big.png')
        root_can.create_image(50,120,image=p,anchor=NW)

        root_can.create_text(165,300,text='C a m p u s Guide', font=f'{fonttxt} 20 bold',fill=txtclr)
        root_can.create_text(165,335,text='by', font=f'{fonttxt} 20 ',fill=txtclr)
        root_can.create_text(165,370,text='Team CampusGuide', font=f'{fonttxt} 20 ',fill=txtclr)

        pro = global_objab.customcan(root_can, 100, 30, 'white', 110, 405)
        pro.config(highlightthickness=1, highlightbackground=txtclr, cursor='hand2')
        butinfo = pro.create_text(50, 15, text='See Project', font=f'{fonttxt} 12', fill=txtclr)
        def profileconfig(pname):
            pname.config(bg=txtclr)
            pname.itemconfig(butinfo, fill='white')

        def profileconfig2(pname):
            pname.config(bg='white')
            pname.itemconfig(butinfo, fill=txtclr)

        pro.bind('<Enter>', lambda event: profileconfig(pro))
        pro.bind('<Leave>', lambda event: profileconfig2(pro))
        pro.bind('<Button-1>', lambda event: webbrowser.open_new_tab(
            'https://www.showcaseport.blogspot.com/2019/07/myprojects.html?m=1'))

        root_can.create_line(310,30,310,500,fill=txtclr,width=2)

        root_can.create_text(575,50,text='About', font=f'{fonttxt} 35 ',fill=txtclr)
        root_can.create_line(450,90,6855,90,fill=txtclr,width=10)
        root_can.create_line(330,150,550,150,fill='black',width=2)

        root_can.create_text(425,125,text='Team Members :', font=f'{fonttxt} 18 ',fill=txtclr)
        root_can.create_text(550,180,text='Nitin Sharma : Main Designer / Coder', font=f'{fonttxt} 18 bold',fill=txtclr)
        root_can.create_text(565,215,text='Gaurav Sharma : Database Queries Handler', font=f'{fonttxt} 18 ',fill=txtclr)
        root_can.create_text(535,250,text='Niharika Gupta : Layout and Database', font=f'{fonttxt} 18 ',fill=txtclr)
        root_can.create_text(575,285,text='Nitin Dabas : Backend Database Connectivity', font=f'{fonttxt} 18 ',fill=txtclr)

        root_can.create_text(400,330,text='Guided by :', font=f'{fonttxt} 18 bold',fill=txtclr)
        root_can.create_line(330,355,550,355,fill='black',width=2)
        root_can.create_text(430,375,text='Ms. Monika Mam', font=f'{fonttxt} 18 ',fill=txtclr)

        root_can.create_text(575,430,text='Powered by Python 3.7', font=f'{fonttxt} 25 bold',fill=txtclr)
        root_can.create_line(450,470,6500,470,fill=txtclr,width=10)

        about_root.mainloop()

    def usersignupfun():
        usrtyp=Toplevel()
        utobj1=Mainframe2()
        utobj2=Mainframe2()
        # calculating dimensions  of screen
        width = 400
        height = 400
        x = (usrtyp.winfo_screenwidth() // 2) - (width // 2)
        y = 50
        usrtyp.geometry(f'{width}x{height}+{x}+{y}')
        usrtyp.title('Choose Type of Account')
        usrtyp.iconbitmap(cg_logo)
        usrtyp.resizable(False, False)
        usrtyp.focus()
        #callables-----------------------------------------
        def students():
            usrtyp.destroy()
            invalidstuuser = studentusername()
            attempting_twice=studentrollno()
            signupfun('S t u d e n t', 'Roll No. :',invalidstuuser,studentsignup,valid_rollno,'Roll No.','Student',attempting_twice)

        def faculty():
            usrtyp.destroy()
            invalidfacultyuser=facultyusername()
            attempting_twice=facultyempid()
            signupfun('F a c u l t y', 'Emp No. :',invalidfacultyuser,facultysignup,valid_empid,'Employee ID','Staff',attempting_twice)

        #canvas1-------------------------------------------
        canone=utobj1.customcan(usrtyp,width,height,'#323b38',0,0)
        #background image-----------------------------------
        bgimg=PhotoImage(file=f'{components_path}//accounts.png')
        canone.create_image(100,10,image=bgimg,anchor=NW)
        #divider--------------------------------------------
        canone.create_line(0,300,500,300,width=2,fill='white')
        canone.create_line(80,257,340,257,width=2,fill='white')
        #text-----------------------------------------------
        utobj1.text(170,240,'C a m p u s','none 15','white')
        utobj1.text(270,240,'Guide','none 20 bold','white')
        utobj1.text(210,275,'Choose Account Type','none 15','white')
        #buttons-------------------------------------------
        utobj1.custombuttons(usrtyp,'Students',40,1,students,60,315)
        utobj1.custombuttons(usrtyp,'Faculty',40,1,faculty,60,355)
        usrtyp.mainloop()

    def loggeduser(username,userpw,uniqueid):
            if username in adminusername() or username in studentusername() or username in facultyusername():
                if uniqueid in studentrollno() or uniqueid in facultyempid() or uniqueid in adminuniqueid():
                   obj11.authenticate(username,userpw,uniqueid)
                else:
                    messagebox.showerror('Invalid User','ID not Recognised!')
            else:
                messagebox.showerror('Invalid User','Username not Recognised')

    # header frame 1

    frame1=obj1.coustomframe(root, 6000,50,'black',50,0)

    # label on header
    #
    intro = Label(frame1, text='LogIn ', fg='white', font='none 20 bold', bg='black')
    intro.place(x=10, y=5)
    #
    intro2=Label(frame1,text='C a m p u s',fg='white',font='none 15',bg='black')
    intro2.place(x=560,y=10)

    intro3=Label(frame1,text='Guide',fg='white',font='none 25 bold',bg='black')
    intro3.place(x=670,y=4)
    # #footer frame 2

    canvas1=obj1.coustomcan(root,w,h,'black',0,50)
    canvas2=obj2.coustomcan(root,50,50,'steelblue',0,0)

    # images on root
    #logoontop
    obj2.image(f'{components_path}//cglogo.png',1,0)
    #login----AVATAR----
    avatarimg=PhotoImage(file=f'{components_path}//cg_big.png')
    canvas1.create_image(280,150,image=avatarimg,anchor=NW)
    canvas1.create_text(380, 350, text='C a m p u s Guide', font=f'{fonttxt} 20 bold', fill='white')
    canvas1.create_text(380, 390, text='by', font=f'{fonttxt} 15 ', fill='white')
    canvas1.create_text(380, 430, text='Team CampusGuide', font=f'{fonttxt} 15 ', fill='white')

    canvas1.create_text(655, 120, text='Log In ', font=f'none 30 bold', fill='white')
    canvas1.create_line(530,50,530,600,fill='white')

    canvas1.create_text(650, 180, text='Username : ', font=f'{fonttxt} 20 ', fill='white')
    obj3.genralentry(canvas1,580,210,40)

    canvas1.create_text(650, 260, text='ID/Roll no. : ', font=f'{fonttxt} 20 ', fill='white')
    obj5.genralentry(canvas1,580,290,40)

    canvas1.create_text(650, 340, text='Password : ', font=f'{fonttxt} 20 ', fill='white')
    obj4.passwordentry(canvas1,580,370,40)

    # PROCESSING MODULE SCRIPT (LOADER)-------------------------------------------------------------------

    def processing(event=''):
        metadatauser = obj3.getgenralentrydata()
        metausrid=obj5.getgenralentrydata()
        metadata = obj4.getpassword()

        if metadatauser == '':
            messagebox.showerror('Empty field', 'Enter a username to login.')
        else:
            if metadata == '':
                messagebox.showerror('Empty field', 'enter the password associated with this username.')
            else:
                if metausrid=='':
                    messagebox.showerror('Empty Field','Please enter your registered ID/Roll No.')
                else:
                    def sucessfull_match():
                        obj3.cleangenral()
                        obj4.clearpassword()
                        obj5.cleangenral()
                        loggeduser(metadatauser,metadata,metausrid)
                        print('yess')
                        return 1

                    t1=threading.Thread(target=lambda :login_load('Logging In...'))
                    t1.start()
                    root.after(1500,sucessfull_match)
                    # sucessfull_match()
                    print('pass')

    # PROCESSING SCRIPT ENDS----------------------------------------------------------------------------
    # ENTER KEY--- S H O R T C U T--- FOR LOGIN
    root.bind('<Return>',processing)
    #------------------------------------------

    def closing_soft():
        width = 300
        xc = (root.winfo_screenwidth() // 2) - (width // 2)
        yc = 290

        globalobj = Mainframe2()
        close_root=Toplevel()
        close_root.geometry(f'302x152+{xc}+{yc}')
        close_root.overrideredirect(True)
        close_root.focus()

        close_root.after(10,lambda :close_root.attributes('-alpha',0.3))
        close_root.after(50,lambda :close_root.attributes('-alpha',0.4))
        close_root.after(100,lambda :close_root.attributes('-alpha',0.5))
        close_root.after(150,lambda :close_root.attributes('-alpha',0.6))
        close_root.after(200,lambda :close_root.attributes('-alpha',0.7))
        close_root.after(250,lambda :close_root.attributes('-alpha',0.8))
        close_root.after(300,lambda :close_root.attributes('-alpha',0.9))

        close_root.after(300,lambda :close_root.attributes('-alpha',1))

        holdercan = Canvas(close_root,width=300,height=150,highlightthickness=1,highlightbackground='red',bg='#171616')
        holdercan.place(x=0,y=0)

        headerframe=globalobj.customframes(holdercan,300,30,'black',1,1)
        def clDestroy(event=''):
            close_root.after(10, lambda: close_root.attributes('-alpha', 0.9))
            close_root.after(50, lambda: close_root.attributes('-alpha', 0.8))
            close_root.after(100, lambda: close_root.attributes('-alpha', 0.7))
            close_root.after(150, lambda: close_root.attributes('-alpha', 0.6))
            close_root.after(200, lambda: close_root.attributes('-alpha', 0.5))
            close_root.after(250, lambda: close_root.attributes('-alpha', 0.4))
            close_root.after(300, lambda: close_root.attributes('-alpha', 0.3))
            close_root.after(350, lambda: close_root.attributes('-alpha', 0.2))
            close_root.after(400, lambda: close_root.attributes('-alpha', 0.1))
            close_root.after(400,close_root.destroy)

        message=globalobj.customlabels(headerframe, 'C a m p u s', 'none 10', 'black', 85, 5,fg='white')
        message=globalobj.customlabels(headerframe, 'Guide', 'none 10 bold', 'black', 160, 5,fg='white')
        close=globalobj.customlabels(headerframe, '', 'none 10 bold', 'black', 268, 3,3,1,fg='white')
        close.bind("<Enter>",lambda x,b=close:close.config(bg='red',cursor='hand2'))
        close.bind("<Leave>",lambda x,b=close:close.config(bg='black'))
        close.bind('<Button-1>',clDestroy)

        message=globalobj.customlabels(holdercan, 'Do you want to Exit?', 'none 12 bold', '#171616', 70, 50,fg='white')

        l1=holdercan.create_line(20,85,280,85,fill='white',width=1)
        l2=holdercan.create_line(150,90,150,140,fill='white',width=1)

        y=Canvas(holdercan,width=50,height=30,bg='#171616',highlightthickness=1,highlightbackground='cyan')
        n=Canvas(holdercan,width=50,height=30,bg='#171616',highlightthickness=1,highlightbackground='cyan')

        y.create_text(25,15,text='Yes',fill='white',font='none 9')
        n.create_text(25,15,text='No',fill='white',font='none 9')

        y.place(x=70,y=100)
        n.place(x=180,y=100)

        y.bind("<Enter>",lambda x,b=y:y.config(highlightbackground='white',cursor='hand2'))
        y.bind("<Leave>",lambda x,b=y:y.config(highlightbackground='cyan'))
        y.bind('<Button-1>',lambda event:root.destroy())

        n.bind("<Enter>",lambda x,b=n:n.config(highlightbackground='white',cursor='hand2'))
        n.bind("<Leave>",lambda x,b=n:n.config(highlightbackground='cyan'))
        n.bind('<Button-1>',clDestroy)

        close_root.mainloop()

    # Buttons
    globalobj=Mainframe2()

    projectbut = globalobj.customcan(canvas1, 250, 45,'black',580,420)
    projectbut.config(highlightthickness=1, highlightbackground='white', cursor='hand2')
    projectbut.create_text(120, 19, text='LogIn', font=f'{fonttxt} 20', fill='white')

    projectbut.bind('<Enter>', lambda event: projectbut.config(highlightthickness=1, highlightbackground='green'))
    projectbut.bind('<Leave>', lambda event: projectbut.config(highlightthickness=1, highlightbackground='white'))
    projectbut.bind('<Button-1>', processing)

    can_but(frame1,'Sign Up  ','black','red','white',950,15,usersignupfun,100,30,50)
    # can_but(frame1,'About us','black','red','white',1080,15,about_section,100,30,50)

    root.protocol('WM_DELETE_WINDOW',closing_soft)

    root.mainloop()
def prescreen():

    preload=Tk()

    preload.resizable(0,0)
    bgc='white'
    fonttxt = 'Ebrima'
    txtclr='#323b38'
    preload.iconbitmap(preload,cg_logo)
    preload.title('About Us --')
    preload.overrideredirect(True)
    preload.attributes('-alpha',0.0)
    preload.attributes('-topmost',True)
    width=900
    hight=550
    x=(preload.winfo_screenwidth()//2)-width//2
    y=(preload.winfo_screenheight()//2)-hight//2

    preload.geometry(f'{width}x{hight}+{x}+{y}')

    global_objab=Mainframe2()
    root_can=global_objab.customcan(preload,width,hight,'black',0,0)

    timings=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    def animation_controler(event,tl):
        times=[]
        if event=='appear':
            times=tl
        else:
            times = tl[::-1]
        a, b, c, d, e, f, g, h, i, j=times
        preload.after(10 ,lambda :preload.attributes('-alpha',a))
        preload.after(60 ,lambda :preload.attributes('-alpha',b))
        preload.after(110,lambda :preload.attributes('-alpha',c))
        preload.after(150,lambda :preload.attributes('-alpha',d))
        preload.after(200,lambda :preload.attributes('-alpha',e))
        preload.after(250,lambda :preload.attributes('-alpha',f))
        preload.after(300,lambda :preload.attributes('-alpha',g))
        preload.after(350,lambda :preload.attributes('-alpha',h))
        preload.after(400,lambda :preload.attributes('-alpha',i))
        preload.after(440,lambda :preload.attributes('-alpha',j))
        if event !='appear':
            preload.after(450,preload.destroy())

    p=PhotoImage(file=f'{components_path}//cg_big.png')
    root_can.create_image(330,120,image=p,anchor=NW)

    root_can.create_text(450,320,text='C a m p u s Guide',font=f'{fonttxt} 25 bold',fill=bgc)
    root_can.create_text(450,420,text='Starting...',font=f'{fonttxt} 15 ',fill=bgc)

    animation_controler('appear',timings)
    preload.after(5000,lambda :animation_controler('disappear',timings))

    preload.mainloop()

thread1=threading.Thread(target=prescreen)
thread1.start()
thread1.join()
proceed()


