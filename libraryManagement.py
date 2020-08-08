from oops2 import *
from info import components_path,cg_logo
from datetime import datetime
from tkinter import messagebox
from tkinter.ttk import Treeview
from database import (addNewBook,valid_rollno,
                      lib_fetch_student,issued_books_students,issue_book,
                      available_books,book_details_toIssue,issued_stuff,return_book,library_full_data,delete_book,update_book_databse,critical_library)

current_date='-'.join(str(datetime.today().date()).split('-')[::-1])

def library(caller):

    rootwin=Toplevel()

    w=rootwin.winfo_screenwidth()
    h=rootwin.winfo_screenheight()

    rootwin.geometry(f'{w}x{h}+0+0')
    rootwin.minsize(800,600)

    rootwin.iconbitmap(rootwin,cg_logo)

    rootwin.state('zoomed')
    # rootwin.resizable(False, False)
    rootwin.title('Library Management System')

    def error_handler(title,msg,win):
        messagebox.showerror(title,msg,parent=win)

    def validate(win,datatup):
        for data in datatup:
            if data=='':
                error_handler("Empty Field",'All the fields are compulsory.',win)
                return -1
            else:
                pass


    global_obj=Mainframe2()
    lobj1=Mainframe2()
    lobj2=Mainframe2()
    lobj3=Mainframe2()
    lobj4=Mainframe2()
    lobj5=Mainframe2()
    lobj6=Mainframe2()

    fonttxt = 'Ebrima'
    bgc='white'

    minican = global_obj.customcan(rootwin, w, h, bgc, 0, 100)
    pic=PhotoImage(file=f'{components_path}//stu.png')
    minican.create_image(210,0,image=pic,anchor=NW)

    # -----header-----
    header = global_obj.packedFrame(rootwin, 50, 50, 'black', TOP, fill=X)
    # -----intro-----
    intro = global_obj.packedFrame(rootwin, 50, 50, '#f2dd22', TOP, fill=X)
    # charec = global_obj.packedFrame(rootwin, 200, 30, '#23241d', LEFT, fill=Y)

    # -----logo canvas-----
    lobj1.customcan(rootwin, 50, 50, 'white', 0, 0)
    lobj1.image(f'{components_path}//cglogo.png', 1, 0)

    introlabel = Label(rootwin, text='C a m p u s', fg='white', font='none 15', bg='black')
    introlabel.place(x=70, y=9)
    intropart2 = Label(rootwin, text='Guide', fg='white', font='none 20 bold', bg='black')
    intropart2.place(x=185, y=5)

    panel_label = global_obj.customlabels(intro, 'Library Management Panel', 'none 20', '#f2dd22', 510, 5, fg='black')

    rol_label=global_obj.customlabels(minican,'Roll No.:',f'{fonttxt} 15 bold',bgc,50,30)
    rol_entry=Entry(minican,width=25,highlightbackground='black',highlightthickness=1)
    rol_entry.place(x=55,y=70)


    def addBook():

        addbook_panel=Toplevel()
        w=400
        h=400
        addbook_panel.title('Add New Book')
        x=(rootwin.winfo_screenwidth()//2)-(w//2)
        y=(rootwin.winfo_screenheight()//2)-(h//2)
        addbook_panel.geometry(f'{w}x{h}+{x}+{y}')
        addbook_panel.focus()
        addbook_panel.iconbitmap(addbook_panel,cg_logo)

        holder=global_obj.customcan(addbook_panel,w,h,None,0,0)

        global_obj.customlabels(holder,'Title','none',None,20,50)
        bname=lobj2.userEntry(holder,170,50,25)

        global_obj.customlabels(holder,'Author','none',None,20,90)
        author=lobj3.userEntry(holder,170,90,25)

        global_obj.customlabels(holder,'Subject','none',None,20,130)
        subject=lobj4.userEntry(holder,170,130,25)

        global_obj.customlabels(holder,'Serial No.','none',None,20,170)
        sno=lobj5.userintentry(holder,170,170,25)

        global_obj.customlabels(holder,'Quantity (in no.)','none',None,20,210)
        amount=lobj6.userintentry(holder,170,210,25)

        existing_sno = available_books()

        global_obj.customlabels(holder,f'Last Assigned Serial No. > ','none',None,20,10)
        if len(existing_sno) !=0:
            existingsnoofbook=global_obj.customlabels(holder,f'{existing_sno[-1]}','none',None,220,10,fg='green')
        else:
            existingsnoofbook=global_obj.customlabels(holder,f'-----','none',None,220,10,fg='green')


        def gettingValues():
            try:
                title=lobj2.getuserentry()
                writer=lobj3.getuserentry()
                subtyp=lobj4.getuserentry()
                serial=int(lobj5.getint())
                quantity=int(lobj6.getint())
                existing_sno1001 = available_books()

                if serial in existing_sno1001:
                    error_handler('Already Exists','This serial no is already been assigned to a book.',addbook_panel)
                else:
                    data_tup=(title,writer,subtyp,serial,quantity)

                    data_validation=validate(addbook_panel,data_tup)

                    if data_validation != -1:


                            confirmation = addNewBook(title,writer,subtyp,serial,quantity)
                            if confirmation == 1:
                                messagebox.showinfo('success!', 'The new book hass been added successfully in database',
                                                    parent=addbook_panel)
                                existing_sno2 = available_books()
                                existingsnoofbook.config(text=existing_sno2[-1])


                            else:
                                error_handler('Unknown Error', 'There is some unknown error occured. Contact the developer team.',
                                              addbook_panel)
            except :
                    error_handler('Invalid Value', 'Something is not as we expected!\n\nCheck the serial no. and quantity to be valid.', addbook_panel)




        submitbut=global_obj.custombuttons(holder,'Add Book',15,1,gettingValues,20,280,fg=bgc,bg='steelblue')
        cancelbut=global_obj.custombuttons(holder,'Cancel',15,1,addbook_panel.destroy,170,280,fg=bgc,bg='steelblue')

        addbook_panel.mainloop()

    def update_book(table,roottod):
        rowinfo = table.focus()
        contentinfo = table.item(rowinfo)
        metalibdata = contentinfo['values']

        if metalibdata !='':

            addbook_panel=Toplevel()
            w=400
            h=400
            addbook_panel.title('Add New Book')
            x=(rootwin.winfo_screenwidth()//2)-(w//2)
            y=(rootwin.winfo_screenheight()//2)-(h//2)
            addbook_panel.geometry(f'{w}x{h}+{x}+{y}')
            addbook_panel.focus()
            addbook_panel.iconbitmap(addbook_panel,cg_logo)

            holder=global_obj.customcan(addbook_panel,w,h,None,0,0)

            global_obj.customlabels(holder,'Title','none',None,20,50)
            bname=lobj2.userEntry(holder,170,50,25)

            global_obj.customlabels(holder,'Author','none',None,20,90)
            author=lobj3.userEntry(holder,170,90,25)

            global_obj.customlabels(holder,'Subject','none',None,20,130)
            subject=lobj4.userEntry(holder,170,130,25)

            global_obj.customlabels(holder,'Serial No.','none',None,20,170)
            sno=lobj5.userintentry(holder,170,170,25)

            global_obj.customlabels(holder,'Quantity (in no.)','none',None,20,210)
            amount=lobj6.userintentry(holder,170,210,25)

            existing_sno = available_books()

            global_obj.customlabels(holder,f'Last Assigned Serial No. > ','none',None,20,10)
            if len(existing_sno) !=0:
                existingsnoofbook=global_obj.customlabels(holder,f'{existing_sno[-1]}','none',None,220,10,fg='green')
            else:
                existingsnoofbook=global_obj.customlabels(holder,f'-----','none',None,220,10,fg='green')


            t,a,s,sn,q=metalibdata

            lobj2.setuserentry(t)
            lobj3.setuserentry(a)
            lobj4.setuserentry(s)
            lobj5.setintegerentry(sn)
            lobj6.setintegerentry(q)

            def gettingValues():
                title=lobj2.getuserentry()
                writer=lobj3.getuserentry()
                subtyp=lobj4.getuserentry()
                serial=int(lobj5.getint())
                quantity=lobj6.getint()

                if int(lobj5.getint()) !=int(sn) and int(serial) in existing_sno:
                        error_handler('Already Exists','This serial no is already been assigned to a book.',addbook_panel)
                else:
                    data_tup=(title,writer,subtyp,serial,quantity)

                    data_validation=validate(addbook_panel,data_tup)

                    if data_validation != -1:
                        try:
                            int(serial)
                            int(quantity)

                            confirmation = update_book_databse(title,writer,subtyp,serial,quantity)
                            if confirmation == 1:
                                messagebox.showinfo('success!', 'The book has been Updated successfully in database',
                                                    parent=addbook_panel)
                                addbook_panel.destroy()
                                roottod.destroy()
                                display_books()


                            else:
                                error_handler('Unknown Error', 'There is some unknown error occured. Contact the developer team.',
                                              addbook_panel)
                        except ValueError:
                            error_handler('Invalid Value', 'Something is not as we expected!\n\nCheck the serial no. and quantity to be valid.', addbook_panel)

            def deleting_book():
                serial=lobj5.getint()
                if serial !='':

                    try:

                        int(serial)

                        if int(serial) in available_books():

                            resp1=messagebox.askyesno('Confirmation',f'The book will be deleted by SERIAL NUMBER.\n\nBook with serial_no={serial} will be deleted.',parent=addbook_panel)
                            if resp1==True:

                                delete_book(int(serial))
                                messagebox.showinfo('Deleted','The book is deleted successfully from database.',parent=addbook_panel)
                                addbook_panel.destroy()
                                roottod.destroy()
                                display_books()
                            else:

                                pass
                        else:
                            error_handler('Book not found','Book with this serial no. not found',addbook_panel)
                    except ValueError:

                        error_handler('Invalid Value','The serial no. must be an INTEGER',addbook_panel)
                else:

                    error_handler('Empty Field','Please enter serial number of the book',addbook_panel)


            submitbut=global_obj.custombuttons(holder,'Update',15,1,gettingValues,20,280,fg=bgc,bg='steelblue')
            cancelbut=global_obj.custombuttons(holder,'Cancel',15,1,addbook_panel.destroy,140,280,fg=bgc,bg='steelblue')
            delbut=global_obj.custombuttons(holder,'Delete Book',15,1,deleting_book,265,280,fg=bgc,bg='steelblue')

            addbook_panel.mainloop()
        else:
            pass


    def display_books():
        display=Toplevel()
        w=1300
        h=600
        display.title('BOOK WAREHOUSE')
        x=(rootwin.winfo_screenwidth()//2)-(w//2)
        y=(rootwin.winfo_screenheight()//2)-(h//2)
        display.geometry(f'{w}x{h}+{x}+{y}')
        display.focus()
        display.iconbitmap(display,cg_logo)
        infoframe = Frame(display, width=500, height=500, bg='white')

        xscrollbar = Scrollbar(infoframe, orient=HORIZONTAL)
        xscrollbar.pack(side=BOTTOM, fill=X)

        yscrollbar = Scrollbar(infoframe, orient=VERTICAL)
        yscrollbar.pack(side=RIGHT, fill=Y)

        table = Treeview(infoframe,
                              columns=('1', '2', '3', '4', '5'),
                              xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

        table.heading('1', text='TITLE')
        table.heading('2', text='AUTHOR')
        table.heading('3', text="SUBJECT")
        table.heading('4', text="SERIAL NO.")
        table.heading('5', text='QUANTITY')

        table['show'] = 'headings'

        table.pack(side=TOP, fill=BOTH, expand=1)

        xscrollbar.config(command=table.xview)
        yscrollbar.config(command=table.yview)
        infoframe.pack(side=TOP, fill=BOTH, expand=1)

        stack=library_full_data()

        for val in stack:
            table.insert('',END,values=val)
        def upbk(event):
            update_book(table,display)

        table.bind('<ButtonRelease-1>',upbk)

        display.mainloop()

    holder_list=[]

    def display_panel(event=''):
        if holder_list !=[]:
            holder_list[0].destroy()
        else:
            pass
        input_id=rol_entry.get()

        if input_id=='':
            error_handler('Empty Fields','field id required for processing information.',rootwin)

        else :
            print(input_id)
            if input_id not in valid_rollno():
                error_handler('Invalid ID','The ID you entered does not exist in college database.',rootwin)
            elif input_id in valid_rollno():

                holder_can = global_obj.customcan(minican, 700, 600, bgc, 650,20)
                holder_can.config(highlightthickness=1,highlightbackground='black')
                holder_list.insert(0,holder_can)

                name = global_obj.customlabels(holder_can, 'Name       : ', f'{fonttxt} 15', bgc, 10, 10)
                namestu = global_obj.customlabels(holder_can, '', f'{fonttxt} 15', bgc, 130, 10)

                rolid = global_obj.customlabels(holder_can, 'Roll No.    : ', f'{fonttxt} 15', bgc, 10, 40)
                rollno = global_obj.customlabels(holder_can, '', f'{fonttxt} 15', bgc, 130, 40)

                brname = global_obj.customlabels(holder_can, 'Branch      : ', f'{fonttxt} 15', bgc, 10, 70)
                branch = global_obj.customlabels(holder_can, '', f'{fonttxt} 15', bgc, 130, 70)

                semstu = global_obj.customlabels(holder_can, 'Semester  : ', f'{fonttxt} 15', bgc, 10, 100)
                semester = global_obj.customlabels(holder_can, '', f'{fonttxt} 15', bgc, 130, 100)

                bnames = global_obj.customlabels(holder_can, 'Books        : ', f'{fonttxt} 15', bgc, 10, 130)
                booknums = global_obj.customlabels(holder_can, '', f'{fonttxt} 15', bgc, 130, 130)

                cancel = global_obj.custombuttons(holder_can, 'X', 5, 2, holder_can.destroy, 650, 2, fg='white', bg='red')

                fetched_details=lib_fetch_student(input_id)
                if fetched_details !=1:
                    books_in_num=issued_books_students(input_id)
                    if len(books_in_num)==0:
                        booknums.config(text='No Books Issued')
                    else:
                        if len(books_in_num)<4:
                            booknums.config(text=len(books_in_num),fg='green')
                        else:
                            booknums.config(text=len(books_in_num),fg='red')
    #-------------------------------------------------------------------------  STUDENTS DETAILS U N P A C K I N G  -------------------------------------------------
                    nameofstu,rol,brname,sem=fetched_details

                    namestu.config(text=nameofstu)
                    rollno.config(text=rol)
                    branch.config(text=brname)
                    semester.config(text=sem)

                else:
                    error_handler('TargetNotFound','Rare case.\nNo details found for the entered ID ',rootwin)

                def issuetouser(type):
                    sno_label = global_obj.customlabels(holder_can, '-', f'{fonttxt} 15 bold', bgc, 10, 240)
                    if type=='issue':
                        sno_label.config(text='Serial no. (for   Issue book)')
                    else:
                        sno_label.config(text='Serial no. (for Return book)')

                    sno_variable=StringVar()

                    sno_entry = Entry(holder_can, width=25, highlightbackground='black', highlightthickness=1,textvariable=sno_variable)
                    sno_entry.place(x=10, y=280)

                    def checking_availablity():
                        input_sno=sno_variable.get()
                        if type=='issue':
                            in_database=available_books()
                        else:
                            in_database=issued_stuff()[0]

                        info=global_obj.customlabels(holder_can,'','none',bgc,170,280)
                        if input_sno=='':
                            info.config(text='-',width=30)
                            global_obj.customcan(holder_can,150,50,bgc,10,320)
                            sno_entry.config(highlightbackground='black')
                        else:
                            allotbut=global_obj.custombuttons(holder_can, '', 15, 1, None, 10, 320)
                            if type=='issue':
                                allotbut.config(text='Allot')
                            else:
                                allotbut.config(text='Return')
                            try:
                                int(input_sno)
                                if int(input_sno) in in_database:
                                    sno_entry.config(highlightbackground='green')
                                    info.config(text='Available',fg='green',width=30)
                                    book_details = book_details_toIssue(input_sno)

        # -------------------------------------------------------------------------  BOOK DETAILS U N P A C K I N G  -------------------------------------------------
                                    title, author, subject,sno, q = book_details
                                    def assign():
                                        allotbut.config(text='Assign')
                                        if len(books_in_num)<4:
                                            print('yes1')
                                            invalid_attempt=critical_library(rol)
                                            print(invalid_attempt,input_sno)
                                            if int(input_sno) in invalid_attempt:
                                                messagebox.showerror('Already Assigned','This book is already issued to this user',parent=rootwin)
                                            else:
                                                resp = messagebox.askyesno('Issue Book',
                                                                           'Issue this book to this user?',
                                                                                               parent=rootwin)
                                                if resp == True:
                                                    issue_book(nameofstu, rol, title, int(input_sno),
                                                               sem,
                                                               brname)
                                                    messagebox.showinfo('Success!',
                                                                        f'Book with Serial no. = [ {sno} ] is assingned to {nameofstu}',
                                                                        parent=rootwin)
                                                else:
                                                    pass

                                        else:
                                            global_obj.customlabels(holder_can,'Can not Issue more books','none',bgc,170,135,fg='red')
                                            allotbut.config(text="Can't Issue",command=lambda :messagebox.showerror('Limit Exceeded','The maximum limit of books to be issue is exceeded for this user'
                                                                                                                  '\nCan not Issue more books ',parent=rootwin),fg='white',bg='red')
                                    def take_back():
                                        invalid_attempt = critical_library(rol)
                                        print(invalid_attempt, input_sno)
                                        if int(input_sno) not in invalid_attempt:
                                            messagebox.showerror('No Book',
                                                                 'This book is not assigned to this user, or may be already returned.',
                                                                 parent=rootwin)
                                        else:
                                            return_book(rol,int(input_sno))
                                            messagebox.showinfo('Returned',
                                                                 'The book is returned successfully!.',
                                                                 parent=rootwin)

                                    if type=='issue':
                                        allotbut.config(command=assign)
                                    else:
                                        allotbut.config(command=take_back)

                                else:
                                    allotbut.config(text="Can't Issue",fg='white',bg='red',command=lambda :messagebox.showerror('Invalid Request','This book is not Available.',parent=rootwin))
                                    sno_entry.config(highlightbackground='red')
                                    info.config(text='')
                                    info.config(text='This book is not Available', fg='red')
                            except ValueError:
                                    error_handler('Value Error','The Serial no. must be an Integer',rootwin)

                    sno_variable.trace('w',lambda name,index,mode : checking_availablity())

                issue = global_obj.custombuttons(holder_can, 'Issue Book', 20, 1, lambda : issuetouser('issue'), 10, 200)
                return_book_ = global_obj.custombuttons(holder_can, 'Return Book', 20, 1, lambda : issuetouser('return'), 170, 200)


    rootwin.bind('<Return>',display_panel)
    rol_entry.focus()
    subbut = global_obj.custombuttons(minican, 'Submit', 20, 1, display_panel, 55, 120)
    if caller=='admin':
        add_book = global_obj.custombuttons(minican, 'Add Book', 20, 1, addBook, 55, 160)
        seebook = global_obj.custombuttons(minican, 'See Books database', 20, 1, display_books, 55, 200)
    elif caller=='stupan':
        seebook = global_obj.custombuttons(minican, 'See Books database', 20, 1, display_books, 55, 160)
    else:
        pass


    rootwin.mainloop()
