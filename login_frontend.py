from backend import *
from tkinter import *
from info import components_path
def signupfun(headname,idfield,invalid,insertdb,validstuff,idstuff,user_name,overattempt):
    objectOfVarification=Verification()
    
    loginroot=Toplevel()
    loginroot.title('Log In Console')
     
    
    # calculating dimensions  of screen
    width= 800
    height= 700
    x=(loginroot.winfo_screenwidth()//2)-(width//2)
    y=10
    loginroot.geometry(f'{width}x{height}+{x}+{y}')
    loginroot.focus()
    loginroot.iconbitmap(f"{components_path}//log-in.ico")
    loginroot.resizable(False,False)

    # objects of Mainframe

    obj1= Mainframe2()
    obj2= Mainframe2()
    obj3= Mainframe2()
    obj4= Mainframe2()
    obj5=Mainframe2()

    # FUNCTION OF LOGIN

    def loginpage():
        #calling backend functions
        loginroot.destroy()

    
    def createAccount():
            name1 = list(obj1.getuserentry())
            phonenouser1 = list(obj2.getint())
            usernameenter1 = list(obj3.getgenralentrydata())
            userpw1 = list(obj4.getpassword())
            rol=obj5.getgenralentrydata()

            print(rol)
            print(overattempt)

            #-----------------validating rollno----------------------
            if name1 == []:
                messagebox.showwarning('Empty Field!',
                                       "Please enter your first name",
                                       parent=loginroot)
            elif usernameenter1 == []:
                messagebox.showwarning('Empty Field!', 'Please enter the username you want to use.', parent=loginroot)
            elif userpw1 == []:
                messagebox.showwarning('Password field id empty!',
                                       'For account security. Please enter a strong password.',
                                       parent=loginroot)
            elif rol == '':
                messagebox.showwarning('Empty Field', 'Please enter the registered roll no.', parent=loginroot)
            else:
                valid_roll_list=validstuff()
                if rol in valid_roll_list:
                    if rol not in overattempt:
                            try:
                                name=obj1.getuserentry()
                                phonenouser=int(obj2.getint())
                                usernameenter=obj3.getgenralentrydata()
                                userpw=obj4.getpassword()
                                phoneno = list(str(obj2.getint()))
                                if len(phoneno) == 10:
                                    if usernameenter in invalid:
                                            messagebox.showerror('Already Exist','This username is already exist.\nTry another one.',parent=loginroot)
                                    else:
                                        print(name )
                                        if name in verifying_names(rol) or name in verifying_names_of_fac(rol):

                                            def writingdatatodatabase():
                                                # ------ WRITING DATA----------------
                                                print(name, phonenouser, rol, usernameenter, userpw)
                                                insertdb(name, phonenouser, rol, usernameenter, userpw)
                                                # -----------------------------------
                                                messagebox.showinfo('Saved','Your data is saved.\n You can login with this usertname and password.',parent=loginroot)
                                                loginroot.destroy()

                                            barcollision(loginroot, 3000,'Creating new Account...',73,45,x=250,y=250)
                                            loginroot.after(3000,writingdatatodatabase)
                                        else:
                                            messagebox.showerror('Invalid Attempt', f'The name you entered does not match with name registered to this {idstuff}.',
                                                                 parent=loginroot)

                                else:
                                    messagebox.showerror('invalid phone no', 'Enter a valid 10-digit phone no.', parent=loginroot)
                            except ValueError:
                                messagebox.showerror('aw-aw!','Enter a valid phone no.',parent=loginroot)
                    else:
                        messagebox.showerror('Overattempt',f'There is already an account associated with this {idstuff}',parent=loginroot)

                else:
                    messagebox.showerror('Invalid User',f'The {idstuff} you have entered is not registered in this college database.'
                    f'which makes you an Invalid user and not able to signup as a {user_name}.',parent=loginroot)

    # Canvases on loginroot

    canvas1=obj1.customcan(loginroot,800,700,'black',0,0)
    # background image

    
    # AVATAR
    avatar = PhotoImage(file=f'{components_path}//user-signup.png')
    canvas1.create_image(300, 100, image=avatar, anchor=NW)
    logo=PhotoImage(file=f'{components_path}//cglogo.png')
    canvas1.create_image(10,15,image=logo,anchor=NW)
    # text on canvas
    intro=Label(loginroot,text=headname,bg='black',fg='white',font='none 30')
    intro.place(x=180,y=15)
    # canvas1.create_text(500,40,'Signup!','none 40 bold','white')
    obj1.text(500,40,'Signup!','none 40 bold','white')
    canvas1.create_line(0,80,1000,80,fill='white',width=5)
    # username labels 
    obj1.text(80,170,'Name :','centurygothic 15 ','white')
    obj1.text(80,230,'Phone :','centurygothic 15 ','white')
    obj1.text(90,290,idfield,'centurygothic 15 ','white')
    obj1.text(100,350,'Username :','centurygothic 15 ','white')
    obj1.text(100,415,'Password :','centurygothic 15 ','white')
    # Entries
    #name
    obj1.userEntry(loginroot,50,190,50)
    #phone no
    obj2.userintentry(loginroot,50,250,50)
    #rollno
    obj5.genralentry(loginroot,50,310,50)
    #username
    obj3.genralentry(loginroot,50,375,50)
    # password
    obj4.passwordentry(loginroot,50,440,50)


    def processingdata(event=''):
        rectanglefade(loginroot,1600,'Verifying...',152,99,x=250,y=250)

        loginroot.after(1600,createAccount)

    # Buttons

    obj1.custombuttons(loginroot,'Submit ',20,2,processingdata,210,520,bg='green',fg='white')
    obj1.custombuttons(loginroot,'LogIn ',20,2,loginpage,50,520,bg='steelblue',fg='white')
    loginroot.bind('<Return>',processingdata)

    loginroot.mainloop()
    
# signupfun('F a c u l t y','Emp ID. :')