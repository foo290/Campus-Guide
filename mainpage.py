from oops2 import Mainframe2
from oops import Mainframe
from tkinter import *
from info import optionlist, cg_logo,components_path
import threading
from tkinter import messagebox
from database import showAdmin,updateadmin
from libraryManagement import library as lib


# datatoretfortheme = []
darkmodestatus=[2]
txttodark=['']

#==================================Main frame 2 objects----------

op2obj1=Mainframe2()
op2obj2=Mainframe2()
op2obj3=Mainframe2()
op2obj4=Mainframe2()
op2obj5=Mainframe2()
op2obj6=Mainframe2()
op2obj7=Mainframe2()
op2obj8=Mainframe2()
op2obj9=Mainframe2()
op2obj10=Mainframe2()

op2global=Mainframe2()

def mainpageon(username_super):
    from backend import Dattoshow,logged_user,FacultyView,newemployee,Accounts_Managments,Fee,custompanelfun,circleloading
    l=logged_user[0]
    # main window
    root= Toplevel()
    root.geometry('1355x720+0+0')
    root.title(f'Campus Guide Software || Logged in as @root-admin_Username={username_super}')
    root.iconbitmap(cg_logo)
    root.state('zoomed')
    root.config(bg='white')
    root.minsize(800,600)


    # Mainframe objects

    obj1=Mainframe()
    obj2=Mainframe()

    headerframe=op2global.packedFrame(root,200,100,'yellow',TOP,fill=X)

    # header frame 1

    frame1=obj1.coustomframe(headerframe, 6000,50,'black',50,0)
    frame2=obj1.coustomframe(headerframe,6000,50,'#323b38',0,50)

    # label on header
    intro = Label(frame1, text='C a m p u s', fg='white', font='none 15', bg='black')
    intro.place(x=15, y=9)
    intro2 = Label(frame1, text='Guide', fg='white', font='none 20 bold', bg='black')
    intro2.place(x=130, y=5)

    # label on frame 2
    op2global.customlabels(frame2,'Administrator Pannel','Ebrima 20','#323b38',570,2,fg='white')

    canvas2=obj2.coustomcan(headerframe,50,50,'steelblue',0,0)

    obj2.image(f"{components_path}//cglogo.png",1,0)

      # FUNCTIONS OF MAINPAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<....


    def addstudent():
        from backend import newstudent
        newstudent()

    def faculty_stuff():
        facultyinfo=FacultyView()

        width = 400
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = 250
        helpdesk = op2global.customcan(root, width, 200, '#323b38', x, y)
        helpdesk.config(highlightthickness=2, bd=2, highlightbackground='black')
        op2global.customlabels(helpdesk, 'Options ', 'Ebrima 20 ', '#323b38', 145, 40,fg='white')
        helpdesk.create_line(30,100,370,100,fill='white')
        def display_info():
            facultyinfo.displayFaculty(root,frame2,'Faculty Fetch','Fetch','Cancel','Delete!','Clear Pad')

        op2global.custombuttons(helpdesk,'Register',20,1,newemployee,20,150)
        op2global.custombuttons(helpdesk, 'Fetch Info', 20, 1,display_info, 230, 150)

        def closepage():
            helpdesk.destroy()
            # defaultclr()

        op2global.custombuttons(helpdesk, 'Close', 5, 1, closepage, 360, 2)

    def fillfee():
        foo=Fee()
        foo.fee_pannel(root,frame2,'Fee Status')



    def fetchdata():
        o3=Dattoshow()
        txtdata1=o3.maindisplay(root,frame2,'Fetch Data',1,'Fetch','Cancel','Clear Filters','Clear Pad')

    def accountmanager():
        acglobslobj = Mainframe2()

        width = 400
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = 250
        optionwin = acglobslobj.customcan(root, width, 200, '#323b38', x, y)

        optionwin.config(highlightthickness=2, bd=2, highlightbackground='black')
        acglobslobj.customlabels(optionwin, 'Select account type', 'Ebrima 20 ', '#323b38', 88, 30,fg='white')
        # acglobslobj.customlabels(optionwin, None, None, 'white', 25, 40)
        optionwin.create_line(30,100,370,100,fill='white')


        def closepage():
            optionwin.destroy()

        def stuaccount():
            accountobject=Accounts_Managments()
            accountobject.accountDisplay(root,frame2,'Roll No.','Students Accounts','student')

        def facaccounts():
            facaccobj=Accounts_Managments()
            facaccobj.accountDisplay(root,frame2,'Employee ID','Faculty Accounts','faculty')

        acglobslobj.custombuttons(optionwin, 'Close', 5, 1, closepage, 360, 2)
        acglobslobj.custombuttons(optionwin, 'Student Account', 20, 1, stuaccount, 20, 150)
        acglobslobj.custombuttons(optionwin, 'Faculty Account', 20, 1, facaccounts, 230, 150)

    def admin_profile():
        ap=Toplevel()

        w = 400
        h = 400
        ap.title('ADMIN PROFILE')
        x = (ap.winfo_screenwidth() // 2) - (w // 2)
        y = (ap.winfo_screenheight() // 2) - (h // 2)
        ap.geometry(f'{w}x{h}+{x}+{y}')
        charvar=StringVar()
        charvar2=StringVar()
        charvar3=StringVar()
        charvar4=StringVar()


        op2global.customlabels(ap,'Name :','none',None,20,10)
        en1=Entry(ap,textvariable=charvar)
        en1.place(x=150,y=10)

        op2global.customlabels(ap,'Username :','none',None,20,60)
        en1=Entry(ap,textvariable=charvar2)
        en1.place(x=150,y=60)

        op2global.customlabels(ap,'ID :','none',None,20,110)
        en1=Entry(ap,textvariable=charvar3)
        en1.place(x=150,y=110)

        op2global.customlabels(ap,'Password :','none',None,20,160)
        en1=Entry(ap,textvariable=charvar4)
        en1.place(x=150,y=160)

        nameofadmin,ph,idofa,user,pas=showAdmin()

        charvar.set(nameofadmin)
        charvar2.set(user)
        charvar3.set(idofa)
        charvar4.set(pas)


        def update():
            name = charvar.get().title()
            username = charvar2.get()
            idofadmin = charvar3.get().title()
            password = charvar4.get()
            validation_tup = (name, idofadmin, username, password)
            print(validation_tup)
            if name=='' or idofadmin=='' or username=='' or password=='':
                messagebox.showerror('Empty Field', 'All the fields are important to be filled.', parent=root)
            else:
                r=updateadmin(name,username,idofadmin,password)
                if r==1:
                    messagebox.showinfo('Sucess','Data updated successfully',parent=root)
                    ap.destroy()
                else:
                    messagebox.showerror('Unknown field', 'There is some problem in saving the data', parent=root)

        subbut=op2global.custombuttons(ap,'Update',10,1,update,20,200)

        ap.mainloop()

#-----------------------------------------------------------------------------------
    options=op2obj10.customcombobox(frame1,'Options',optionlist,20,1100,15)

    def optionhover(event):
        optionsel=op2obj10.getcombodata()
        print(optionsel)
        if optionsel=='Log Out':
            circleloading(root,1600,'Logging Out...',105,65)
            root.after(1600,root.destroy)
        elif optionsel=='Home':
            root.destroy()
            mainpageon(username_super)
        elif optionsel=='See Fee Structure':
            custompanelfun('feestruct',root,850,650,60,810,2)
        elif optionsel=='Profile':
            admin_profile()


    options.bind('<<ComboboxSelected>>',optionhover)
#-------------------------------------------------------------------------------------
    #on canvas 1

    admission=op2obj1.customcan(root,150,150,'white',100,120)
    feestat=op2obj2.customcan(root,150,150,'white',500,120)
    studentinfo=op2obj3.customcan(root,150,150,'white',300,120)
    library=op2obj5.customcan(root,150,150,'white',900,120)
    faculty=op2obj6.customcan(root,150,150,'white',1100,120)
    accounts=op2obj7.customcan(root,150,150,'white',700,120)

    design=op2global.customcan(root,1250,400,'white',50,300)
    design.create_text(630,250,text='C a m p u s  Guide',font='Ebrima 20 bold',fill='#323b38')
    design.create_text(630,300,text='Powered by Python 3.7',font='Ebrima 30 bold',fill='#323b38')
    design.create_text(630,350,text='Team : CampusGuide',font='Ebrima 15 bold',fill='#323b38')



    op2obj1.image(f'{components_path}//admission.png',0,10)
    op2obj1.text(70,130,'Addmission','none 14 bold','black')

    op2obj2.image(f'{components_path}//feestat.png',5,0)
    op2obj2.text(80,130,'Fee Status','none 14 bold','black')

    op2obj3.image(f'{components_path}//studentinfo.png',0,10)
    op2obj3.text(80,130,'Student Info.','none 14 bold','black')


    op2obj5.image(f"{components_path}//book2.png",1,10)
    op2obj5.text(80,130,'Library','none 14 bold','black')

    op2obj6.image(f"{components_path}//hirefac.png",1,10)
    op2obj6.text(80,130,'Faculty','none 14 bold','black')

    op2obj7.image(f"{components_path}//account.png",1,10)
    op2obj7.text(78,130,'User Accounts','none 14 bold','black')




    def admission_clicked(event):
        admission.config(bg='green')
        admission.bind("<ButtonRelease>",lambda event, b=admission: b.config(bg='white'))
        addstudent()

    admission.bind('<Button-1>',admission_clicked)

    def studentinfo_clicked(event):
        studentinfo.config(bg='green')
        studentinfo.bind("<ButtonRelease>",lambda event, b=studentinfo: b.config(bg='white'))
        t1=threading.Thread(target=fetchdata)
        t1.start()

    studentinfo.bind('<Button-1>',studentinfo_clicked)

    def fee_clicked(event):
        feestat.config(bg='green')
        feestat.bind("<ButtonRelease>",lambda event, b=feestat: b.config(bg='white'))
        fillfee()

    feestat.bind('<Button-1>',fee_clicked)


    def library_clicked(event):
        library.config(bg='green')
        library.bind("<ButtonRelease>",lambda event, b=library: b.config(bg='white'))
        lib('admin')

    library.bind('<Button-1>',library_clicked)

    def faculty_clicked(event):
        faculty.config(bg='green')
        faculty.bind("<ButtonRelease>",lambda event, b=faculty: b.config(bg='white'))
        faculty_stuff()

    faculty.bind('<Button-1>',faculty_clicked)

    def accounts_clicked(event):
        accounts.config(bg='green')
        accounts.bind("<ButtonRelease>",lambda event, b=accounts: b.config(bg='white'))
        accountmanager()

    accounts.bind('<Button-1>',accounts_clicked)

    admission.bind("<Enter>", lambda event,b=admission:b.config(highlightthickness=3,highlightbackground='green'))
    admission.bind("<Leave>", lambda event,b=admission:b.config(highlightthickness=0))

    feestat.bind("<Enter>", lambda event,b=feestat:b.config(highlightthickness=3,highlightbackground='green'))
    feestat.bind("<Leave>", lambda event, b=feestat: b.config(highlightthickness=0))

    studentinfo.bind("<Enter>", lambda event, b=studentinfo: b.config(highlightthickness=3, highlightbackground='green'))
    studentinfo.bind("<Leave>", lambda event, b=studentinfo: b.config(highlightthickness=0))

    library.bind("<Enter>",lambda event, b=library: b.config(highlightthickness=3, highlightbackground='green'))
    library.bind("<Leave>", lambda event, b=library: b.config(highlightthickness=0))

    faculty.bind("<Enter>",lambda event, b=faculty: b.config(highlightthickness=3, highlightbackground='green'))
    faculty.bind("<Leave>", lambda event, b=faculty: b.config(highlightthickness=0))

    accounts.bind("<Enter>",lambda event, b=accounts: b.config(highlightthickness=3, highlightbackground='green'))
    accounts.bind("<Leave>", lambda event, b=accounts: b.config(highlightthickness=0))

    def logout_admin_cross():
        circleloading(root, 1600, 'Logging Out...', 105, 65)
        root.after(1600, root.destroy)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    root.protocol('WM_DELETE_WINDOW',logout_admin_cross)
    root.mainloop()
# mainpageon('user')