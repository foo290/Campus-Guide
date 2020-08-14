from oops2 import *
from tkinter import messagebox
from info import *
from database import fillattendance,rollforattendance,aforstudentbymonth
from backend import rectanglefade
from  libraryManagement import library

rights="You own a Student type account which has only read access." \
       "\nYou are not able to change anything in your profile, only admin\n has rights to alter any profile."

faculty_rights="You own a Faculty type account which has read and write access." \
       "\nStill you are not able to change anything in your profile, only admin\n has rights to alter any profile."

def students_panel(account_type,student,imagename,un,pw,butlist):


    if account_type=='student':
        name,  surname, rollno, course, branch, year, sem, father, mother, pcontact, dob, phone, email, _,city, pincode, adharno, dor,batch, gender,  fee, trans, address=student[0]

       
    else:
        nameoffac, surnameoffac, empid, factitle, facdepart,  facph1, facph2, facdob, facgender,   facemail, facsal, faccountry, faccity,facpincode, facadhaar,facaddress=student[0]  
 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if factitle=='Librarian':
            library('stupan')
            return
        else:
            pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    stu=Toplevel()
    w=stu.winfo_screenwidth()
    h=stu.winfo_screenheight()
    stu.geometry(f"{w}x{h}+0+0")
    stu.state('zoomed')
    stu.resizable(False,False)
    stu.title('students pannel')
    stu.minsize(800,600)


    #--------objects of mainframe-------
    sglobalobj=Mainframe2()
    sobj1=Mainframe2()
    sobj2=Mainframe2()
    sobj3=Mainframe2()
    sobj4=Mainframe2()
    sobj5=Mainframe2()
    sobj6=Mainframe2()
    sobj7=Mainframe2()
    sobj8=Mainframe2()
    sobj9=Mainframe2()
    sobj10=Mainframe2()
    sobj11=Mainframe2()
    sobj12=Mainframe2()
    sobj13=Mainframe2()
    sobj14=Mainframe2()
    sobj15=Mainframe2()
    sobj16=Mainframe2()
    sobj17=Mainframe2()
    sobj18=Mainframe2()
    sobj19=Mainframe2()
    sobj20=Mainframe2()
    sobj21=Mainframe2()
    sobj22=Mainframe2()
    sobj23=Mainframe2()




    #-----------------------------------

    #========MAIN CANVAS================

    maincan=sobj6.customcan(stu,w,h,None,0,0)

    #-----header-----
    header=sobj1.packedFrame(stu,50,50,'black',TOP,fill=X)
    #-----intro-----
    intro=sobj2.packedFrame(stu,50,50,'#f2dd22',TOP,fill=X)
    charec=sobj3.packedFrame(stu,200,30,'#23241d',LEFT,fill=Y)

    #-----logo canvas-----
    sobj4.customcan(stu,50,50,'white',0,0)
    sobj4.image(f'{components_path}//cglogo.png',1,0)

    introlabel = Label(stu, text='C a m p u s', fg='white', font='none 15', bg='black')
    introlabel.place(x=70, y=9)
    intropart2 = Label(stu, text='Guide', fg='white', font='none 20 bold', bg='black')
    intropart2.place(x=185, y=5)

    panel_label = sglobalobj.customlabels(intro, '', 'none 20', '#f2dd22', 570, 5, fg='black')

    if account_type=='student':
        panel_label.config(text='Students Profile')
    else:
        panel_label.config(text='Faculty Profile')

    sobj5.customcan(charec,150,150,'#23241d',25,30)
    sobj5.image(f'{components_path}//studentmale.png',0,0)

    displayname=sglobalobj.customlabels(charec,None,'none 20','#23241d',60,180,fg='white')
    if account_type=='student':
        displayname.config(text=name)
    else:
        displayname.config(text=nameoffac)

    menuframe=sglobalobj.customframes(maincan,2000,25,'#ffa703',160,100)

    def homepage():
        home=sobj11.customcan(maincan,w,h,None,201,125)

        sobj11.image(f'{components_path}//stu.png',0,0)
        sobj11.text(150,50,'Welcome!','none 45','black')

        if account_type=='student':
            sobj11.text(130,120,name+' '+surname,'none 25','black')
        else:
            sobj11.text(130,120,nameoffac+' '+surnameoffac,'none 25','black')


    def dashboard():

        profile=sobj9.customcan(maincan,w,h,'white',201,125)
        heading=sglobalobj.customlabels(profile,'','none 15 bold','white',400,5)
        if account_type=='student':
            heading.config(text='This is all we know about you!')

            #-----------IMAGE PROCESSING------------------
            sobj10.customcan(profile,150,150,'white',380,90)
            sobj10.image(f'{studir_path}//{imagename}',0,0)

            #-------dividers-----------------
            sobj9.line(100,40,1050,40,'black',2)
            sobj9.line(550,50,550,700,'black',2)

            #------------personal details students---------------------------------------------------------------
            sglobalobj.customlabels(profile,'Personal Details :','none 12 bold','white',20,80)

            sglobalobj.customlabels(profile,'Name :','none','white',40,120)
            sglobalobj.customlabels(profile,name+' '+surname,'none','white',200,120)

            sglobalobj.customlabels(profile,"Father's Name :",'none','white',40,160)
            sglobalobj.customlabels(profile,father,'none','white',200,160)

            sglobalobj.customlabels(profile,"Mother's Name :",'none','white',40,200)
            sglobalobj.customlabels(profile,mother,'none','white',200,200)

            sglobalobj.customlabels(profile,'Phone No. :','none','white',40,240)
            sglobalobj.customlabels(profile,phone,'none','white',200,240)

            sglobalobj.customlabels(profile,'Parents Contact :','none','white',40,280)
            sglobalobj.customlabels(profile,pcontact,'none','white',200,280)

            sglobalobj.customlabels(profile,'Gender :','none','white',40,320)
            sglobalobj.customlabels(profile,gender,'none','white',200,320)

            sglobalobj.customlabels(profile,'E-mail ID :','none','white',40,360)
            sglobalobj.customlabels(profile,email,'none','white',200,360)

            sglobalobj.customlabels(profile,'Adhaar Card :','none','white',40,400)
            sglobalobj.customlabels(profile,adharno,'none','white',200,400)

            sglobalobj.customlabels(profile,'City :','none','white',40,440)
            sglobalobj.customlabels(profile,city,'none','white',200,440)

            sglobalobj.customlabels(profile,'PIN Code :','none','white',40,480)
            sglobalobj.customlabels(profile,pincode,'none','white',200,480)

            sglobalobj.customlabels(profile,'Address :','none','white',40,520)
            addresfield=sobj7.txtarea(profile,30,2,200,520)
            addresfield.delete(1.0,END)
            addresfield.insert('end',address)
            addresfield.config(state=DISABLED)

            #----------------------------------------------------------------------------------------------------------

            #-------------------------------------ACADMIC DETAILS-----------------------------------------------------
            sglobalobj.customlabels(profile,'Acadmic Details :','none 12 bold','white',570,70)

            sglobalobj.customlabels(profile,'Course :','none','white',590,110)
            sglobalobj.customlabels(profile,course,'none','white',750,110)

            sglobalobj.customlabels(profile,'Branch:','none','white',590,150)
            sglobalobj.customlabels(profile,branch,'none','white',750,150)

            sglobalobj.customlabels(profile,'Year :','none','white',590,190)
            sglobalobj.customlabels(profile,year,'none','white',750,190)

            sglobalobj.customlabels(profile,'Semester :','none','white',590,230)
            sglobalobj.customlabels(profile,sem,'none','white',750,230)

            sglobalobj.customlabels(profile,'Transport :','none','white',590,270)
            sglobalobj.customlabels(profile,trans,'none','white',750,270)

            sglobalobj.customlabels(profile,'Session :','none','white',590,310)
            sglobalobj.customlabels(profile,batch,'none','white',750,310)

            sglobalobj.customlabels(profile,'Roll No. :','none','white',590,350)
            sglobalobj.customlabels(profile,rollno,'none','white',750,350)
        else:
            sobj9.line(100,40,1050,40,'black',2)
            sobj9.line(550,50,550,700,'black',2)

            heading.config(text='This is all we know about you!')

            #------------personal details faculty---------------------------------------------------------------
            sglobalobj.customlabels(profile,'Personal Details :','none 12 bold','white',20,80)

            sglobalobj.customlabels(profile,'Name :','none','white',40,120)
            sglobalobj.customlabels(profile,nameoffac+' '+surnameoffac,'none','white',200,120)

            sglobalobj.customlabels(profile,'Phone No. :','none','white',40,160)
            sglobalobj.customlabels(profile,facph1,'none','white',200,160)

            sglobalobj.customlabels(profile,'E-mail ID :','none','white',40,200)
            sglobalobj.customlabels(profile,facemail,'none','white',200,200)

            sglobalobj.customlabels(profile,'Adhaar Card :','none','white',40,240)
            sglobalobj.customlabels(profile,facadhaar,'none','white',200,240)

            sglobalobj.customlabels(profile,'City :','none','white',40,280)
            sglobalobj.customlabels(profile,faccity,'none','white',200,280)

            sglobalobj.customlabels(profile,'PIN Code :','none','white',40,320)
            sglobalobj.customlabels(profile,facpincode,'none','white',200,320)

            sglobalobj.customlabels(profile,'Address :','none','white',40,420)
            addresfield=sobj20.txtarea(profile,30,2,200,390)
            addresfield.delete(1.0,END)
            addresfield.insert('end',facaddress)
            addresfield.config(state=DISABLED)

#-------------------------------------ACADMIC DETAILS faculty-----------------------------------------------------
            sglobalobj.customlabels(profile,'Other Details :','none 12 bold','white',600,80)

            sglobalobj.customlabels(profile,'Title :','none','white',620,120)
            sglobalobj.customlabels(profile,factitle,'none','white',750,120)

            sglobalobj.customlabels(profile,'Department :','none','white',620,160)
            sglobalobj.customlabels(profile,facdepart,'none','white',750,160)

            sglobalobj.customlabels(profile,'Stipend :','none','white',620,200)
            sglobalobj.customlabels(profile,facdepart,'none','white',750,200)

        #================000000000========================================

    def user_profile():
        usercanvas=sglobalobj.customcan(maincan,w,h,'white',201,130)
        sglobalobj.customlabels(usercanvas,'Your Profile :-','none 12 bold','white',40,20)

        sglobalobj.customlabels(usercanvas,'Username :','none','white',40,60)
        sglobalobj.customlabels(usercanvas,un,'none','white',200,60)

        sglobalobj.customlabels(usercanvas,'User ID/Roll No. :','none','white',40,100)
        sglobalobj.customlabels(usercanvas,rollno,'none','white',200,100)

        sglobalobj.customlabels(usercanvas, 'Password :', 'none', 'white', 40, 140)
        sglobalobj.customlabels(usercanvas,pw,'none','white',200,140)

    def college_notice():
        messagebox.showinfo('NOTICE !','Attendance should be greater than 75% for every student.',parent=stu)
        defaultclr()

    def attendance():
        if account_type=='student':

            attendancecanvas=sglobalobj.customcan(maincan,w,h,'white',201,130)

            heading = sglobalobj.customlabels(attendancecanvas, 'Attendance Pannel', 'none 15 bold', 'white', 450, 5)

            sglobalobj.customlabels(attendancecanvas,'Your Roll No. :','none 12 bold','white',40,40)
            sglobalobj.customlabels(attendancecanvas,rollno,'none 12 bold','white',170,40)

            m=sglobalobj.customlabels(attendancecanvas,'Month :','none 12','white',40,80)
            s=sglobalobj.customlabels(attendancecanvas,'Subject :','none 12 ','white',40,120)

            sobj18.customcombobox(attendancecanvas,'month',months,25,150,80)
            subs=sobj19.customcombobox(attendancecanvas, 'subject', None, 25, 150, 120)

            for bstu in all_branches:
                if branch == bstu:
                    branch_index = all_branches.index(bstu)
                    branch_to_display = subjects_of_branches[branch_index]
                    for subsem1 in ugsem:
                        if sem == subsem1:
                            indexsem1 = ugsem.index(subsem1)
                            subject_to_display = branch_to_display[indexsem1]
                            subs.set('subject')
                            subs.config(values=subject_to_display)


            def showattendance():
                monthsel=sobj18.getcombodata()
                sub=sobj19.getcombodata()

                if monthsel=='month' or monthsel=='':
                    m.config(fg='red')

                elif sub=='subject' or sub=='':
                    s.config(fg='red')
                    m.config(fg='black')
                else:
                    m.config(fg='black')
                    s.config(fg='black')

                    alec,tlec=aforstudentbymonth(rollno,sub,monthsel)
                    if alec==[]:
                        messagebox.showerror('Not Found','No data found for your attendance of this month or subject',parent=stu)
                    elif tlec==[]:
                        messagebox.showerror('Not Found','No data found for your attendance of this month or subject',parent=stu)
                    else:
                        sglobalobj.customlabels(attendancecanvas, 'Total Lectures :', 'none 12', 'white', 40, 240)
                        sglobalobj.customlabels(attendancecanvas, tlec[0], 'none 12','white', 200, 240)

                        sglobalobj.customlabels(attendancecanvas, 'Attended Lectures :', 'none 12', 'white', 40, 280)
                        sglobalobj.customlabels(attendancecanvas,alec[0],'none 12','white',200,280)

                        calculating=(alec[0]/tlec[0])*100
                        percentagetocal = round(calculating, 2)
                        percentage=str(round(calculating,2))

                        sglobalobj.customlabels(attendancecanvas, 'Percentage :', 'none 12', 'white', 40, 320)
                        ptage=sglobalobj.customlabels(attendancecanvas,percentage+' %','none 12','white',200,320)
                        ptage.config(width=5)

                        if percentagetocal<50:
                            a1=sglobalobj.customlabels(attendancecanvas, 'Your Attendance is below then minimum criteria in this subject.\n'
                                                                      'Try to attend more classes to compensate.', 'none 12', 'white', 40, 360,fg='red')
                            a1.config(width=50)
                        else:

                            a2=sglobalobj.customlabels(attendancecanvas,
                                                    'Your Attendance is meeting the minimum criteria for attendance.', 'none 12', 'white', 40, 360,
                                                    fg='green')
                            a2.config(height=2)

            sglobalobj.custombuttons(attendancecanvas,'Submit',12,1,showattendance,200,160)

        else:
            attendancecanvas = sglobalobj.customcan(maincan, w, h, 'white', 201, 130)
            sglobalobj.customlabels(attendancecanvas, 'Attendance Pannel :', 'none 12 bold', 'white', 40, 20)

            sglobalobj.customlabels(attendancecanvas,'Branch :','none 12 ','white',40,60)
            fields=sobj10.customcombobox(attendancecanvas,'select',None,25,45,90)

            sglobalobj.customlabels(attendancecanvas,'Year :','none 12 ','white',40,130)
            ye=sobj11.customcombobox(attendancecanvas,'select',btech_years,25,45,160)

            sglobalobj.customlabels(attendancecanvas,'Semester :','none 12 ','white',40,200)
            semofsub=sobj12.customcombobox(attendancecanvas,'select',None,25,45,230)

            sglobalobj.customlabels(attendancecanvas,'Subject :','none 12 ','white',40,270)
            subject=sobj13.customcombobox(attendancecanvas,'select',None,25,45,300)

            sglobalobj.customlabels(attendancecanvas,'Month :','none 12 ','white',40,340)
            sobj17.customcombobox(attendancecanvas,'select',months,25,45,370)
            # =['Computer Science', 'Faculty of life science', 'Physical Science']
            print(facdepart)

            if facdepart=='Computer Science':
                fields.config(values=['CSE'])
            elif facdepart=='Faculty of life science':
                fields.config(values=bsc_fields[4])
            elif facdepart=='Physical Science':
                fields.config(values=bsc_fields[0:4])
            elif facdepart=='Commerse':
                fields.config(values=bsc_fields[-3:])
            else:
                fields.config(values=['No Data for Your title'])

    #-----------------------------------------------Semester Automation-------------------------------------------------
            def semester_config(semdata):
                semofsub.set('select')
                subject.set('select')
                semofsub.config(values=semdata)

            def accord_year_sem(event):
                sel_year = sobj11.getcombodata()
                if sel_year == '1st year':
                    semester_config(['1st semester', '2nd semester'])
                elif sel_year == '2nd year':
                    semester_config(['3rd semester', '4th semester'])
                elif sel_year == '3rd year':
                    semester_config(['5th semester', '6th semester'])
                elif sel_year == '4th year':
                    semester_config(['7th semester', '8th semester'])
                else:
                    semester_config(['select year first'])

            ye.bind('<<ComboboxSelected>>', accord_year_sem)
    #--------------------------------------------------------------------------------------------------------------------

    #--------------------------------------------------Subject Automation------------------------------------------------

            def branchforsub():
                branchselforsub=sobj10.getcombodata()
                return branchselforsub

            global sem_counter

            def callingbindings(event):
                global sem_counter
                sem_counter = 0

                semselforsub=sobj12.getcombodata()
                branchforsubject=branchforsub()
                print(semselforsub,branchforsubject)

                if branchforsubject=='CSE':

                    if semselforsub==semesters[0]:
                        subject.set('select')
                        subject.config(values=btechcse11subs)
                    elif semselforsub==semesters[1]:
                        subject.set('select')
                        subject.config(values=btechcse12subs)
                    elif semselforsub==semesters[2]:
                        subject.set('select')
                        subject.config(values=btechcse23subs)
                    elif semselforsub==semesters[3]:
                        subject.set('select')
                        subject.config(values=btechcse24subs)
                    elif semselforsub==semesters[4]:
                        subject.set('select')
                        subject.config(values=btechcse35subs)
                    elif semselforsub==semesters[5]:
                        subject.set('select')
                        subject.config(values=btechcse36subs)
                    elif semselforsub==semesters[6]:
                        subject.set('select')
                        subject.config(values=btechcse47subs)
                    elif semselforsub==semesters[7]:
                        subject.set('select')
                        subject.config(values=btechcse48subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error',"Thats's not a valid semester",parent=stu)

                elif branchforsubject=='Mechanical Engg.':

                    if semselforsub==semesters[0]:
                        subject.set('select')
                        subject.config(values=btechmec11subs)
                    elif semselforsub==semesters[1]:
                        subject.set('select')
                        subject.config(values=btechmec12subs)
                    elif semselforsub==semesters[2]:
                        subject.set('select')
                        subject.config(values=btechmec23subs)
                    elif semselforsub==semesters[3]:
                        subject.set('select')
                        subject.config(values=btechmec24subs)
                    elif semselforsub==semesters[4]:
                        subject.set('select')
                        subject.config(values=btechmec35subs)
                    elif semselforsub==semesters[5]:
                        subject.set('select')
                        subject.config(values=btechmec36subs)
                    elif semselforsub==semesters[6]:
                        subject.set('select')
                        subject.config(values=btechmec47subs)
                    elif semselforsub==semesters[7]:
                        subject.set('select')
                        subject.config(values=btechmec48subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error',"Thats's not a valid semester",parent=stu)

                elif branchforsubject=='Electrical Engg.':

                    if semselforsub==semesters[0]:
                        subject.set('select')
                        subject.config(values=btechece11subs)
                    elif semselforsub==semesters[1]:
                        subject.set('select')
                        subject.config(values=btechece12subs)
                    elif semselforsub==semesters[2]:
                        subject.set('select')
                        subject.config(values=btechece23subs)
                    elif semselforsub==semesters[3]:
                        subject.set('select')
                        subject.config(values=btechece24subs)
                    elif semselforsub==semesters[4]:
                        subject.set('select')
                        subject.config(values=btechece35subs)
                    elif semselforsub==semesters[5]:
                        subject.set('select')
                        subject.config(values=btechece36subs)
                    elif semselforsub==semesters[6]:
                        subject.set('select')
                        subject.config(values=btechece47subs)
                    elif semselforsub==semesters[7]:
                        subject.set('select')
                        subject.config(values=btechece48subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error',"Thats's not a valid semester",parent=stu)

                elif branchforsubject=='Civil Engg.':

                    if semselforsub==semesters[0]:
                        subject.set('select')
                        subject.config(values=btechcivil11subs)
                    elif semselforsub==semesters[1]:
                        subject.set('select')
                        subject.config(values=btechcivil12subs)
                    elif semselforsub==semesters[2]:
                        subject.set('select')
                        subject.config(values=btechcivil23subs)
                    elif semselforsub==semesters[3]:
                        subject.set('select')
                        subject.config(values=btechcivil24subs)
                    elif semselforsub==semesters[4]:
                        subject.set('select')
                        subject.config(values=btechcivil35subs)
                    elif semselforsub==semesters[5]:
                        subject.set('select')
                        subject.config(values=btechcivil36subs)
                    elif semselforsub==semesters[6]:
                        subject.set('select')
                        subject.config(values=btechcivil47subs)
                    elif semselforsub==semesters[7]:
                        subject.set('select')
                        subject.config(values=btechcivil48subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error',"Thats's not a valid semester",parent=stu)

                elif branchforsubject=='Bsc(PMC)':

                    if semselforsub==ugsem[0]:
                        subject.set('select')
                        subject.config(values=bsc11subs)
                    elif semselforsub == ugsem[1]:
                        subject.set('select')
                        subject.config(values=bsc12subs)
                    elif semselforsub == ugsem[2]:
                        subject.set('select')
                        subject.config(values=bsc23subs)
                    elif semselforsub == ugsem[3]:
                        subject.set('select')
                        subject.config(values=bsc24subs)
                    elif semselforsub == ugsem[4]:
                        subject.set('select')
                        subject.config(values=bsc35subs)
                    elif semselforsub == ugsem[5]:
                        subject.set('select')
                        subject.config(values=bsc36subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error',"Thats's not a valid semester",parent=stu)

                elif branchforsubject=='Bsc(H).Phy':

                    if semselforsub==ugsem[0]:
                        subject.set('select')
                        subject.config(values=bschphy11subs)
                    elif semselforsub == ugsem[1]:
                        subject.set('select')
                        subject.config(values=bschphy12subs)
                    elif semselforsub == ugsem[2]:
                        subject.set('select')
                        subject.config(values=bschphy23subs)
                    elif semselforsub == ugsem[3]:
                        subject.set('select')
                        subject.config(values=bschphy24subs)
                    elif semselforsub == ugsem[4]:
                        subject.set('select')
                        subject.config(values=bschphy35subs)
                    elif semselforsub == ugsem[5]:
                        subject.set('select')
                        subject.config(values=bschphy36subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error',"Thats's not a valid semester",parent=stu)

                elif branchforsubject=='Bsc(H).Maths':

                    if semselforsub == ugsem[0]:
                        subject.set('select')
                        subject.config(values=bschmath11subs)
                    elif semselforsub == ugsem[1]:
                        subject.set('select')
                        subject.config(values=bschmath12subs)
                    elif semselforsub == ugsem[2]:
                        subject.set('select')
                        subject.config(values=bschmath23subs)
                    elif semselforsub == ugsem[3]:
                        subject.set('select')
                        subject.config(values=bschmath24subs)
                    elif semselforsub == ugsem[4]:
                        subject.set('select')
                        subject.config(values=bschmath35subs)
                    elif semselforsub == ugsem[5]:
                        subject.set('select')
                        subject.config(values=bschmath36subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error',"Thats's not a valid semester",parent=stu)

                elif branchforsubject=='Bsc(H).Chemisty':

                    if semselforsub == ugsem[0]:
                        subject.set('select')
                        subject.config(values=bschchem11subs)
                    elif semselforsub == ugsem[1]:
                        subject.set('select')
                        subject.config(values=bschchem12subs)
                    elif semselforsub == ugsem[2]:
                        subject.set('select')
                        subject.config(values=bschchem23subs)
                    elif semselforsub == ugsem[3]:
                        subject.set('select')
                        subject.config(values=bschchem24subs)
                    elif semselforsub == ugsem[4]:
                        subject.set('select')
                        subject.config(values=bschchem35subs)
                    elif semselforsub == ugsem[5]:
                        subject.set('select')
                        subject.config(values=bschchem36subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error',"Thats's not a valid semester",parent=stu)

                elif branchforsubject=='Bsc(H).Life Science':

                    if semselforsub == ugsem[0]:
                        subject.set('select')
                        subject.config(values=bschlfsci11subs)
                    elif semselforsub == ugsem[1]:
                        subject.set('select')
                        subject.config(values=bschlfsci12subs)
                    elif semselforsub == ugsem[2]:
                        subject.set('select')
                        subject.config(values=bschlfsci23subs)
                    elif semselforsub == ugsem[3]:
                        subject.set('select')
                        subject.config(values=bschlfsci24subs)
                    elif semselforsub == ugsem[4]:
                        subject.set('select')
                        subject.config(values=bschlfsci35subs)
                    elif semselforsub == ugsem[5]:
                        subject.set('select')
                        subject.config(values=bschlfsci36subs)
                    else:
                        subject.set('select')
                        subject.config(values=None)
                        messagebox.showerror('Error', "Thats's not a valid semester", parent=stu)

                elif branchforsubject=='B.Com':
                    for subsem in ugsem:
                        if semselforsub==subsem:
                            indexsem=ugsem.index(subsem)
                            subject.set('select')
                            subject.config(values=bcom_subsem_list[indexsem])
                            print(bcom_subsem_list[indexsem])
                        else:
                            messagebox.showinfo('Error', "Thats's not a valid semester", parent=stu)

            semofsub.bind("<<ComboboxSelected>>",callingbindings)
    #--------------------------------------------------------------------------------------------------------------------

            def fillingselected(event=''):
                bname=sobj10.getcombodata()
                yname=sobj11.getcombodata()
                semname=sobj12.getcombodata()
                subname=sobj13.getcombodata()
                monthname=sobj17.getcombodata()

                def errorhandler(mess):
                    messagebox.showerror('Empty Field!',mess,parent=stu)

                if bname=="" or bname=="select":
                    errorhandler('Please select Branch name.')
                elif yname=='' or yname=='select':
                    errorhandler('Please select year')
                elif semname=='' or semname=='select':
                    errorhandler('please select semester')
                elif subname=='' or subname=='select':
                    errorhandler('please select the subject.')
                elif monthname=="" or monthname=='select':
                    errorhandler('Please select the month name to fill attendance.')
                else:


                    filloperationholder=sglobalobj.customcan(attendancecanvas,400,500,'#dbdddd',300,40)
                    filloperationholder.config(highlightthickness=2,bd=2,highlightbackground='black')


                    r=sglobalobj.customlabels(filloperationholder, 'Roll No. :', 'none 12 ', '#dbdddd', 10, 20)
                    rolturn=sobj14.customcombobox(filloperationholder, '', None, 25, 170, 22)

                    tl=sglobalobj.customlabels(filloperationholder, 'Total Lectures :', 'none 12 ', '#dbdddd', 10, 60)
                    sobj15.userintentry(filloperationholder,170,60,25)

                    al=sglobalobj.customlabels(filloperationholder, 'Attended Lectures :', 'none 12 ', '#dbdddd', 10, 100)
                    sobj16.userintentry(filloperationholder,170,100,25)

                    rollistfora=rollforattendance(bname,yname,semname)
                    if rollistfora==[]:
                        messagebox.showerror('No data Found','No one has applied in this branch yet.',parent=stu)
                    else:
                        global j
                        j = 1
                        testlist = [i for i in range(10)]
                        print(rollistfora)

                        rolturn.set(rollistfora[0])
                        rolturn.config(values=testlist)
                        filloperationholder.focus_set()

                        def finalfill(event=''):

                            totallec=sobj15.getint()
                            taken=sobj16.getint()
                            rolfetch=sobj14.getcombodata()

                            if totallec !='':
                                tl.config(fg='black')
                                if taken !='':
                                    al.config(fg='black')
                                    if rolfetch !='':
                                        if int(totallec) < int(taken):
                                            messagebox.showerror('Invalid Entry','Attended lectures can not be greater than total lectures.',parent=stu)
                                        else:
                                            global j

                                            sobj15.setintegerentry(totallec)
                                            try:
                                                rolturn.set(rollistfora[0+j])
                                            except IndexError:
                                                rolturn.set('FINISHED !')
                                            j+=1
                                            print(totallec,taken,rolfetch)

                                            if rolfetch=='FINISHED !':
                                                messagebox.showwarning('Completed','The rollno. for this branch is finished.',parent=stu)
                                            else:
                                                fillattendance(bname,yname,semname,rolfetch,totallec,taken,subname,monthname)
                                                sobj16.clearinten()
                                    else:
                                        r.config(fg='red')
                                else:
                                    al.config(fg='red')
                            else:
                                tl.config(fg='red')

                        subbut=sglobalobj.custombuttons(filloperationholder, 'Submit', 15, 1, finalfill, 10, 140)
                        subbut.bind('<Return>',finalfill)
                        cancelbut = sglobalobj.custombuttons(filloperationholder,'Cancel',15,1,filloperationholder.destroy,170,140)

            filbut=sglobalobj.custombuttons(attendancecanvas,'Fill',10,1,fillingselected,40,410)
            filbut.bind('<Return>',fillingselected)

        defaultclr()


    def help():
        width = 400
        x = (stu.winfo_screenwidth() // 2) - (width // 2)
        y = 250
        helpdesk=sglobalobj.customcan(stu,width,300,'white',x,y)
        helpdesk.config(highlightthickness=2,bd=2,highlightbackground='black')
        sglobalobj.customlabels(helpdesk,'Your Rights :','none 12 bold','white',5,10)
        sglobalobj.customlabels(helpdesk,rights,None,'white',25,40)
        def closepage():
            helpdesk.destroy()
            defaultclr()
        sglobalobj.custombuttons(helpdesk,'Close',5,1,closepage,360,2)

#--------------------------------------------------------------faculty functions----------------------------------------------

    def assingment():
        assingmentcanvas = sobj8.customcan(maincan, w, h,'white', 201, 130)

        sobj8.line(100, 40, 1050, 40, 'black', 2)
        sglobalobj.customlabels(assingmentcanvas, 'User Profile', 'none 15 bold', 'white', 490, 5)

        sglobalobj.customlabels(assingmentcanvas, 'User Name :', 'none', 'white', 20, 110)
        sglobalobj.customlabels(assingmentcanvas, un, 'none', 'white', 150, 110)

        sglobalobj.customlabels(assingmentcanvas, 'Employee ID :', 'none', 'white', 20, 150)
        sglobalobj.customlabels(assingmentcanvas, empid, 'none', 'white', 150, 150)

        sglobalobj.customlabels(assingmentcanvas, 'Password :', 'none', 'white', 20, 190)
        sglobalobj.customlabels(assingmentcanvas, pw, 'none', 'white', 150, 190)

    def colNotice():
        messagebox.showinfo('NOTICE','Currently there is no NOTICE for faculty members.',parent=stu)
        defaultclr()

    def helpFaculty():
        width = 400
        x = (stu.winfo_screenwidth() // 2) - (width // 2)
        y = 250
        helpdesk = sglobalobj.customcan(stu, width, 300, 'white', x, y)
        helpdesk.config(highlightthickness=2, bd=2, highlightbackground='black')
        sglobalobj.customlabels(helpdesk, 'Your Rights :', 'none 12 bold', 'white', 5, 10)
        sglobalobj.customlabels(helpdesk, faculty_rights, None, 'white', 25, 40)

        def closepage():
            helpdesk.destroy()
            defaultclr()

        sglobalobj.custombuttons(helpdesk, 'Close', 5, 1, closepage, 360, 2)


    #------------Buttons-----------------------------
    b1=sglobalobj.custombuttons(menuframe,butlist[1],30,1,dashboard,250,0,bg='black',fg='white')
    b2 = sglobalobj.custombuttons(menuframe, butlist[2], 30, 1, None, 450, 0, bg='black', fg='white')
    b3=sglobalobj.custombuttons(menuframe,butlist[3],30,1,attendance,660,0,bg='black',fg='white')

    b6=sglobalobj.custombuttons(menuframe,butlist[6],30,1,None,870,0,bg='black',fg='white')
    b7=sglobalobj.custombuttons(menuframe,butlist[7],20,1,None,1075,0,bg='black',fg='white')
    b8=sglobalobj.custombuttons(menuframe,butlist[0],30,1,homepage,40,0,bg='white',fg='black')

    if account_type=='student':
        b2.config(command=user_profile)
        b6.config(command=college_notice)
        b7.config(command=help)
    else:
        b2.config(command=assingment)
        b6.config(command=colNotice)
        b7.config(command=helpFaculty)


    def logging_out():
        rectanglefade(stu,3000,'Logging out...',152,99)
        stu.after(3000,stu.destroy)


    sglobalobj.custombuttons(intro,'Log Out',15,1,logging_out,1150,10,bg='#323d38',fg='white')

    def bconfig(b,o1,o2,o3,o6,o7):
        b.config(bg='white',fg='black')
        o1.config(bg='black',fg='white')
        o3.config(bg='black',fg='white')
        o6.config(bg='black',fg='white')
        o7.config(bg='black',fg='white')
        o2.config(bg='black',fg='white')

    def b1eve(b):
        bconfig(b1,b2,b3,b6,b7,b8)
    def b2eve(b):
        bconfig(b2,b1,b3,b6,b7,b8)
    def b3eve(b):
        bconfig(b3,b1,b2,b6,b7,b8)

    def b6eve(b):
        bconfig(b6,b1,b3,b2,b7,b8)
    def b7eve(b):
        bconfig(b7,b1,b3,b2,b2,b8)
    def b8eve(b):
        bconfig(b8,b1,b3,b2,b7,b2)

    def defaultclr():
        b1.config(bg='black',fg='white')
        b2.config(bg='black',fg='white')
        b3.config(bg='black',fg='white')
        b6.config(bg='black',fg='white')
        b7.config(bg='black',fg='white')
        b8.config(bg='black',fg='white')

    b1.bind('<ButtonRelease-1>',b1eve)
    b2.bind('<ButtonRelease-1>',b2eve)
    b3.bind('<ButtonRelease-1>',b3eve)
    b6.bind('<ButtonRelease-1>',b6eve)
    b7.bind('<ButtonRelease-1>',b7eve)
    b8.bind('<ButtonRelease-1>',b8eve)


    homepage()

    stu.mainloop()
