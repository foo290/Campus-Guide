import sqlite3
import pandas as pd
from info import *


connection = sqlite3.connect(stu_warehouse_path)
connectiontofacultydatabase=sqlite3.connect(fac_warehouse_path)
connectiontofeedata=sqlite3.connect(fee_database_path)
connectiontoattendance=sqlite3.connect(attendance_database_path)
connection_to_library=sqlite3.connect(librarydatabase_path)
connection_to_issued_books=sqlite3.connect(library_issued_books_path)
connection_to_admin=sqlite3.connect(admin_accountDatabase_path)

pd.set_option('display.max_columns',None)
pd.set_option('display.width',600)

def showAdmin():
    cur=connection_to_admin.cursor()
    cur.execute('select * from admin')
    a_details=cur.fetchall()
    return a_details[0]
def updateadmin(name,username,id,pas):
    cur=connection_to_admin.cursor()
    cur.execute(f'update admin set name="{name}" , username="{username}", id="{id}", password="{pas}" ')
    connection_to_admin.commit()
    return 1


def addNewBook(title,author,subject,sno,ammount):
    cur=connection_to_library.cursor()

    cur.execute(f'insert into lib values(?,?,?,?,?)',(title,author,subject,sno,ammount))
    connection_to_library.commit()
    return 1


def lib_fetch_student(rol):
    cur=connection_to_library.cursor()
    details=pd.read_sql_query(f'select name,roll_no,branch,semester from students where roll_no="{rol}"',connection)
    connection.commit()

    fetched_students=details.values.tolist()
    if fetched_students==[]:
        return 1
    else:
        return fetched_students[0]

def update_book_databse(t,a,sub,sn,q):
    cur=connection_to_library.cursor()
    cur.execute(f'update lib set name="{t}", author="{a}", subject="{sub}",s_no="{sn}", quantity="{q}" where s_no="{sn}" ')
    connection_to_library.commit()
    return 1

def issued_stuff():
    data=pd.read_sql_query('select serialno,rollno from issue',connection_to_issued_books)
    connection_to_issued_books.commit()
    sno=data['serialno'].to_list()
    rno=data['rollno'].to_list()
    return sno,rno

def library_full_data():
    cur=connection_to_library.cursor()
    cur.execute('select * from lib')
    stack=cur.fetchall()
    return stack
def critical_library(rno):
    cur=connection_to_issued_books.cursor()
    meta=pd.read_sql_query(f'select serialno from issue where rollno="{rno}" ',connection_to_issued_books)
    fl=meta['serialno'].to_list()
    connection_to_issued_books.commit()
    return fl

def one_to_one():
    tempdic = {}
    sno_list, r_list = issued_stuff()
    for s, r in zip(sno_list, r_list):
        tempdic[r] = s
    return tempdic


def issued_books_students(roldat):
    issued_books=pd.read_sql_query(f'select serialno from issue where rollno="{roldat}" ',connection_to_issued_books)
    connection_to_issued_books.commit()

    list_issued=issued_books['serialno'].to_list()

    return list_issued

def available_books():
    sno=pd.read_sql_query('select s_no from lib',connection_to_library)
    list_sno=sno['s_no'].to_list()
    return  list_sno

def book_details_toIssue(snum):
    details=pd.read_sql_query(f'select * from lib where s_no="{snum}" ',connection_to_library)
    list_details=details.values.tolist()
    if list_details==[]:
        return 1
    else:
        return list_details[0]

def issue_book(name,rollno,title,serialno,sem,branch):
    cur=connection_to_issued_books.cursor()
    cur.execute(f'insert into issue values(?,?,?,?,?,?)',(name,rollno,title,serialno,sem,branch))
    connection_to_issued_books.commit()

def return_book(rol,sno):
    cur=connection_to_issued_books.cursor()
    cur.execute(f'delete from issue where rollno="{rol}" and serialno="{sno}" ')
    connection_to_issued_books.commit()
    return 1

def delete_book(b_no):
    cur=connection_to_library.cursor()
    cur.execute(f'delete from lib where s_no="{b_no}" ')
    connection_to_library.commit()



def data_warehouse(first_name,last_name,rollno,course_name,branch_name,
                                      year_name,sem,father_name,mother_name,parentscontact,finaldob,phoneno,email,country_name,city_name,pincode,adhaar,finaldateofreg,
                                      batch_duration,genderdata,feeofstu,transport_service,addressofstu,listof_doc):


    cur = connection.cursor()
    cur.execute('insert into students values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (first_name,last_name,rollno,course_name,branch_name,
                                      year_name,sem,father_name,mother_name,parentscontact,finaldob,phoneno,email,country_name,city_name,pincode,adhaar,finaldateofreg,
                                      batch_duration,genderdata,feeofstu,transport_service,addressofstu,listof_doc))
    connection.commit()

# data_warehouse('Palak', 'Sharma', '45', 'B.Tech', 'CSE', '1st year', '1st semester', 'Kabir',
#                'Mahi', 989677809, 'Jan,2,1991', 9089786756, 'palak@gmail.com', 'India', 'Delhi', 112222,
#                211212121212, 'March,3,1992', '1992-1996', 'Female', 45000, 'No', 'Rohini', '["none"]')
#
def faculty_data_warehouse(first_name,last_name,emp_id,faculty_title,depart,eph,eph2,finaldob,genderdata,email,stipend,country_name,city_name,
                                          pincode,adhaar,addressofstu):

    curtofaculty=connectiontofacultydatabase.cursor()
    curtofaculty.execute('insert into faculty values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(first_name,last_name,emp_id,faculty_title,depart,
                                                                                        eph,eph2,finaldob,genderdata,email,stipend,country_name,city_name,
                                                                                            pincode,adhaar,addressofstu))
    connectiontofacultydatabase.commit()
#
def delete_faculty(empno):
    curtodelfac=connectiontofacultydatabase.cursor()
    curtodelfac.execute(f'delete from faculty where emp_id="{empno}" ')
    connectiontofacultydatabase.commit()
#
#
def updates_in_datawarehouse(first_name, last_name, rollno, course_name, branch_name, year_name, sem, father_name, mother_name, parentscontact, finaldob,
                                                       phoneno, email, country_name, city_name, pincode, adhaar,  finaldateofreg,
                             batch_duration, genderdata, feeofstu, transport_service, addressofstu,condition_rollNo):
    curupdates=connection.cursor()
    curupdates.execute(f'update students set name="{first_name}", surname="{last_name}",roll_no="{rollno}", course="{course_name}",branch="{branch_name}",'
                       f'year="{year_name}",semester="{sem}",father_name="{father_name}",mothername="{mother_name}",father_phone="{parentscontact}",'
                       f'dob="{finaldob}",phone_no="{phoneno}",email="{email}",country="{country_name}",city="{city_name}",pin_code={pincode},'
                       f'adhaar="{adhaar}",dateofreg="{finaldateofreg}",session="{batch_duration}",gender="{genderdata}",fee="{feeofstu}",transport="{transport_service}",'
                       f'address="{addressofstu}" where roll_no="{condition_rollNo}"')
#     connection.commit()
#
def studentFeestatus(name,surname,rollno,father,course,branch,year,sem,fee,feestat):
    curtofee=connectiontofeedata.cursor()
    curtofee.execute(f'insert into fee values(?,?,?,?,?,?,?,?,?,?)',(name,surname,rollno,father,course,branch,year,sem,fee,feestat))
    connectiontofeedata.commit()

def fetch_feeStatus(rolldat):
    curtof=connectiontofeedata.cursor()
    cur=connectiontofeedata.cursor()

    curtof.execute('select * from fee')
    cur.execute(f'select * from fee where rollno="{rolldat}" ')
    rolfee=cur.fetchall()
    feedat=curtof.fetchall()

    return feedat,rolfee

def updateFee(ammount,roldat):
    curtoupdate=connectiontofeedata.cursor()
    curtoupdate.execute(f'update fee set feestat="{ammount}" where rollno="{roldat}" ')
    connectiontofeedata.commit()
# studentFeestatus('Neha', 'Verma', 'a40317014', 'Anil', 'B.Tech', 'CSE', '1st year', '1st semester', 65000, 65000)
def verifying_names(rol):
    nameof_student=pd.read_sql_query(f'select name from students where roll_no="{rol}" ',connection)
    final=nameof_student['name'].tolist()
    return final

def verifying_names_of_fac(eid):
    nameof_student=pd.read_sql_query(f'select name from faculty where emp_id="{eid}" ',connectiontofacultydatabase)
    final=nameof_student['name'].tolist()
    return final


print(verifying_names_of_fac('Empas004'))

def fetch_faculty_fromdatabase(title,depart,sal,empunique):
    curfetchsupernarrow=connectiontofacultydatabase.cursor()
    curfetchtds=connectiontofacultydatabase.cursor()
    curfetchtde=connectiontofacultydatabase.cursor()
    curfetchtd=connectiontofacultydatabase.cursor()
    curfetchtse=connectiontofacultydatabase.cursor()
    curfetchts=connectiontofacultydatabase.cursor()
    curfetchte=connectiontofacultydatabase.cursor()
    curfetchtitle=connectiontofacultydatabase.cursor()
    curfetchdse=connectiontofacultydatabase.cursor()
    curfetchds=connectiontofacultydatabase.cursor()
    curfetchde=connectiontofacultydatabase.cursor()
    curfetchdepartment=connectiontofacultydatabase.cursor()
    curfetchse=connectiontofacultydatabase.cursor()
    curfetchstipend=connectiontofacultydatabase.cursor()
    curfetchempid=connectiontofacultydatabase.cursor()
    curfetchdefault=connectiontofacultydatabase.cursor()

    curfetchdefault.execute('select * from faculty')
    allcolumn=curfetchdefault.fetchall()

    curfetchsupernarrow.execute(f'select * from faculty where title="{title}" and department="{depart}" and stipend="{sal}" and emp_id="{empunique}" ')
    supernarrow=curfetchsupernarrow.fetchall()

    curfetchtds.execute(f'select * from faculty where title="{title}" and department="{depart}" and stipend="{sal}" ')
    tds=curfetchtds.fetchall()

    curfetchtde.execute(f'select * from faculty where title="{title}" and department="{depart}" and emp_id="{empunique}" ')
    tde=curfetchtde.fetchall()

    curfetchtd.execute(f'select * from faculty where title="{title}" and department="{depart}" ')
    td=curfetchtd.fetchall()

    curfetchtse.execute(f'select * from faculty where title="{title}" and stipend="{sal}" and emp_id="{empunique}" ')
    tse=curfetchtse.fetchall()

    curfetchts.execute(f'select * from faculty where title="{title}" and stipend="{sal}" ')
    ts=curfetchts.fetchall()

    curfetchte.execute(f'select * from faculty where title="{title}" and emp_id="{empunique}" ')
    te=curfetchte.fetchall()

    curfetchtitle.execute(f'select * from faculty where title="{title}" ')
    onlytitle=curfetchtitle.fetchall()

    curfetchdse.execute(f'select * from faculty where department="{depart}" and stipend="{sal}" and emp_id="{empunique}" ')
    dse=curfetchdse.fetchall()

    curfetchds.execute(f'select * from faculty where department="{depart}" and stipend="{sal}" ')
    ds=curfetchds.fetchall()

    curfetchde.execute(f'select * from faculty where department="{depart}" and emp_id="{empunique}" ')
    de=curfetchde.fetchall()

    curfetchdepartment.execute(f'select * from faculty where department="{depart}" ')
    onlydepartment=curfetchdepartment.fetchall()

    curfetchse.execute(f'select * from faculty where stipend="{sal}" and emp_id="{empunique}" ')
    se=curfetchse.fetchall()

    curfetchstipend.execute(f'select * from faculty where stipend="{sal}" ')
    onlystipend=curfetchstipend.fetchall()

    curfetchempid.execute(f'select * from faculty where emp_id="{empunique}" ')
    onlyid=curfetchempid.fetchall()

    connectiontofacultydatabase.commit()

    maindata_tup=(allcolumn,supernarrow,tds,tde,td,tse,ts,te,onlytitle,dse,ds,de,onlydepartment,se,onlystipend,onlyid)

    return maindata_tup

def fetch_on_rol(rol):
    cur=connection.cursor()
    cur.execute(f'select * from students where roll_no="{rol}" ')
    ful_dat=cur.fetchall()
    return ful_dat


def fetchstudentsdata(selected_course,selected_year,selected_branch,given_roll,selected_sem):

    curnarrow=connection.cursor()
    curcbys=connection.cursor()
    curcbyr=connection.cursor()
    curcby=connection.cursor()
    curcbsr=connection.cursor()
    curcbs=connection.cursor()
    curcbr=connection.cursor()
    curcb=connection.cursor()
    curcs=connection.cursor()
    curonlyc=connection.cursor()
    curcys=connection.cursor()
    curcy=connection.cursor()
    curbysr=connection.cursor()
    curbys=connection.cursor()
    curbyr=connection.cursor()
    curby=connection.cursor()
    curbsr=connection.cursor()
    curbs=connection.cursor()
    curonlyb=connection.cursor()
    curys=connection.cursor()
    curonlyyear=connection.cursor()
    curonlysem=connection.cursor()
    defaultdat=connection.cursor()

    curnarrow.execute(f'select * from students where course="{selected_course}" and branch="{selected_branch}" and year="{selected_year}"'
                      f'and semester="{selected_sem}" and roll_no="{given_roll}" ')
    narrowfetch=curnarrow.fetchall()

    curcbys.execute(f'select * from students where course="{selected_course}" and branch="{selected_branch}" and year="{selected_year}"'
                    f'and semester="{selected_sem}" ')
    cbys=curcbys.fetchall()

    curcbyr.execute(f'select * from students where course="{selected_course}" and branch="{selected_branch}" and year="{selected_year}"'
                    f' and roll_no="{given_roll}" ')
    cbyr=curcbyr.fetchall()

    curcby.execute(f'select * from students where course="{selected_course}" and branch="{selected_branch}" and year="{selected_year}" ')
    cby=curcby.fetchall()

    curcbsr.execute(f'select * from students where course="{selected_course}" and branch="{selected_branch}" '
                    f'and semester="{selected_sem}" and roll_no="{given_roll}" ')
    cbsr=curcbsr.fetchall()

    curcbs.execute(f'select * from students where course="{selected_course}" and branch="{selected_branch}" '
                    f'and semester="{selected_sem}" ')
    cbs=curcbs.fetchall()

    curcbr.execute(f'select * from students where course="{selected_course}" and branch="{selected_branch}" '
                    f'and roll_no="{given_roll}" ')
    cbr=curcbr.fetchall()

    curcb.execute(f'select * from students where course="{selected_course}" and branch="{selected_branch}" ')
    cb=curcb.fetchall()

    curcs.execute(f'select * from students where course="{selected_course}" and semester="{selected_sem}" ')
    cs=curcs.fetchall()

    curonlyc.execute(f'select * from students where course="{selected_course}" ')
    onlyc=curonlyc.fetchall()

    curcys.execute(f'select * from students where course="{selected_course}" and year="{selected_year}"'
                    f'and semester="{selected_sem}" ')
    cys=curcys.fetchall()

    curcy.execute(f'select * from students where course="{selected_course}" and year="{selected_year}" ')
    cy=curcy.fetchall()

    curbysr.execute(f'select * from students where  branch="{selected_branch}" and year="{selected_year}"'
                    f'and semester="{selected_sem}" and roll_no="{given_roll}" ')
    bysr=curbysr.fetchall()

    curbys.execute(f'select * from students where  branch="{selected_branch}" and year="{selected_year}"'
                    f'and semester="{selected_sem}" ')
    bys=curbys.fetchall()

    curbyr.execute(f'select * from students where  branch="{selected_branch}" and year="{selected_year}"'
                    f'and roll_no="{given_roll}" ')
    byr=curbyr.fetchall()

    curby.execute(f'select * from students where  branch="{selected_branch}" and year="{selected_year}" ')
    by=curby.fetchall()

    curbsr.execute(f'select * from students where  branch="{selected_branch}"'
                    f'and semester="{selected_sem}" and roll_no="{given_roll}" ')
    bsr=curbsr.fetchall()

    curbs.execute(f'select * from students where  branch="{selected_branch}"'
                    f'and semester="{selected_sem}" ')

    bs=curbs.fetchall()

    curonlyb.execute(f'select * from students where  branch="{selected_branch}" ')
    onlyb=curonlyb.fetchall()

    curys.execute(f'select * from students where  year="{selected_year}"'
                    f'and semester="{selected_sem}" ')
    ys=curys.fetchall()

    curonlyyear.execute(f'select * from students where  year="{selected_year}" ')
    onlyyear=curonlyyear.fetchall()

    curonlysem.execute(f'select * from students where semester="{selected_sem}" ')
    onlysem=curonlysem.fetchall()

    defaultdat.execute(f'select * from students ')
    defaultinfo=defaultdat.fetchall()

    connection.commit()

    rettup=(narrowfetch,cbys,cbyr,cby,cbsr,cbs,cbr,cb,cs,onlyc,cys,cy,bysr,bys,byr,by,bsr,bs,onlyb,ys,onlyyear,onlysem,defaultinfo)

    return rettup


def updatefacultydata(first_name, last_name, emp_id, faculty_title, depart,
                                                               eph, eph2, finaldob, genderdata,
                                                               email, stipend, country_name, city_name,
                                                               pincode, adhaar, addressofstu,conditionid):
    curtoupdate=connectiontofacultydatabase.cursor()
    curtoupdate.execute(f'update faculty set title="{faculty_title}", department="{depart}", name="{first_name}", surname="{last_name}", phone="{eph}",'
                        f'phone2="{eph2}", dob="{finaldob}", emp_id="{emp_id}", adhaar="{adhaar}", country="{country_name}", city="{city_name}",'
                        f'pinno="{pincode}", email="{email}", gender="{genderdata}", stipend="{stipend}", address="{addressofstu}" where emp_id="{conditionid}"')




def deleteing_student(roltodel,coursetodel,branchtodel,yeartodel,semtodel):
    curdel=connection.cursor()
    curdel.execute(f'delete from students where roll_no="{roltodel}" and course="{coursetodel}" and branch="{branchtodel}" and year="{yeartodel}"'
                   f'and semester="{semtodel}"')
    connection.commit()


def data_layout(df):
    df.rename(columns={'name': '    Name:', 'surname': '     Surname:', 'fathername': "    Father's Name:",
                      'mothername': "    Mother's Name:",
                      'phone_no': '    Phone No.:', 'father_phone': '    Parents Contact:', 'city': '    City:',
                      'roll_no': '    Roll No.:', 'course': '    Course:',
                      'branch': '    Branch:', 'year': '    Year:', 'address': '    Address:',
                      'pin_code': '    PIN Code:'}, inplace=True)


#---------------------------------------------------------USERNAME PASSWORD DATABASE FILES READ/WRITE OPERATIONS----------------------------------------------------
connectiontouser=sqlite3.connect(stu_accountDatabase_path)
connectiontofacultyuser=sqlite3.connect(fac_accountDatabase_path)
connectiontoadmin=sqlite3.connect(admin_accountDatabase_path)

#---------READ OPERATIONS FOR STUDENTS----------------------------------------------------

def studentusername():
    cur2=connectiontouser.cursor()
    metadata=pd.read_sql_query('select username from studentuser',connectiontouser)
    datalist=metadata['username'].tolist()
    connectiontouser.commit()
    return datalist

def studentpassword():
    curr=connectiontouser.cursor()
    metastupassword=pd.read_sql_query('select password from studentuser',connectiontouser)
    connectiontouser.commit()
    pwdatalist=metastupassword['password'].tolist()
    return pwdatalist

def studentrollno():
    currs=connectiontouser.cursor()
    metarolldata=pd.read_sql_query('select id from studentuser',connectiontouser)
    connectiontouser.commit()
    rollist=metarolldata['id'].tolist()
    return rollist

def deleting_student_account(roll):
    curdel=connectiontouser.cursor()
    curdel.execute(f'delete from studentuser where id="{roll}"')
    connectiontouser.commit()

#------------------------------------------READ OPERATIONS FOR FACULTY----------------------------------------------------------------------------------------------------------

def facultyusername():
    cur3=connectiontofacultyuser.cursor()
    metadatafaculty=pd.read_sql_query('select username from facultyuser',connectiontofacultyuser)
    connectiontofacultyuser.commit()
    datalist2=metadatafaculty['username'].tolist()
    return datalist2

def facultypassword():
    metapassdata=pd.read_sql_query('select password from facultyuser',connectiontofacultyuser)
    pwlistfaculty=metapassdata['password'].tolist()
    connectiontofacultyuser.commit()
    return pwlistfaculty

def facultyempid():
    metaiddata=pd.read_sql_query('select id from facultyuser',connectiontofacultyuser)
    idlist=metaiddata['id'].tolist()
    connectiontofacultyuser.commit()
    return idlist

def deleting_faculty_account(user,empid):
    curdel=connectiontofacultyuser.cursor()
    curdel.execute(f'delete from facultyuser where id="{empid}" and username="{user}"')
    connectiontofacultyuser.commit()

#-----------------------------------------READ OPERATIONS FOR ADMIN--------------------------------------------------------------------------------------------------------------

def adminusername():
    metaadminname=pd.read_sql_query('select username from admin',connectiontoadmin)
    adminunlist=metaadminname['username'].tolist()
    connectiontoadmin.commit()
    return adminunlist

def adminpassword():
    metapw=pd.read_sql_query('select password from admin',connectiontoadmin)
    adminpwlist=metapw['password'].tolist()
    connectiontoadmin.commit()
    return adminpwlist

def adminuniqueid():
    metaid=pd.read_sql_query('select id from admin',connectiontoadmin)
    adminidlist=metaid['id'].tolist()
    connectiontoadmin.commit()
    return adminidlist


#-----------------WRITE OPERATION----------------------------------------------------

def studentsignup(name,phone,idofuser,username,password):
    cuu2=connectiontouser.cursor()
    cuu2.execute('insert into studentuser values(?,?,?,?,?)',(name,phone,idofuser,username,password))
    connectiontouser.commit()


def facultysignup(name,phone,idofuser,username,password):
    cuu3=connectiontofacultyuser.cursor()
    cuu3.execute('insert into facultyuser values(?,?,?,?,?)',(name,phone,idofuser,username,password))
    connectiontofacultyuser.commit()

def adminsignup(name,phone,idofuser,username,password):
    cur=connectiontoadmin.cursor()
    cur.execute('insert into admin values(?,?,?,?,?)',(name,phone,idofuser,username,password))
    connectiontoadmin.commit()
#====================================================================================================================================================================================

#===================================================================== U S E R  A C C O U N T...F U N C T I O N S ================================================================

def fetchingstudentaccount(uname,sturol):

    curtof=connectiontouser.cursor()
    curid=connectiontouser.cursor()
    curuser=connectiontouser.cursor()
    curuserandid=connectiontouser.cursor()

    curtof.execute('select * from studentuser')
    alldat=curtof.fetchall()

    curid.execute(f'select * from studentuser where id="{sturol}" ')
    iddat=curid.fetchall()

    curuser.execute(f'select * from studentuser where username="{uname}" ')
    userdat=curuser.fetchall()

    curuserandid.execute(f'select * from studentuser where username="{uname}" and id="{sturol}" ')
    useriddat=curuserandid.fetchall()

    connectiontouser.commit()

    return (alldat,iddat,userdat,useriddat)

def fetchingfacultyaccount(uname,sturol):

    curtof=connectiontofacultyuser.cursor()
    curid=connectiontofacultyuser.cursor()
    curuser=connectiontofacultyuser.cursor()
    curuserandid=connectiontofacultyuser.cursor()

    curtof.execute('select * from facultyuser')
    alldat=curtof.fetchall()

    curid.execute(f'select * from facultyuser where id="{sturol}" ')
    iddat=curid.fetchall()

    curuser.execute(f'select * from facultyuser where username="{uname}" ')
    userdat=curuser.fetchall()

    curuserandid.execute(f'select * from facultyuser where username="{uname}" and id="{sturol}" ')
    useriddat=curuserandid.fetchall()

    connectiontofacultyuser.commit()

    return (alldat,iddat,userdat,useriddat)

def deletestudenuseraccount(username,uid):
    curtodelstuacc=connectiontouser.cursor()
    curtodelstuacc.execute(f'delete from studentuser where id="{uid}" and username="{username}" ')
    connectiontouser.commit()
    return 1

def deletefacultyuseraccount(uid):
    curtodelstuacc=connectiontofacultyuser.cursor()
    curtodelstuacc.execute(f'delete from facultyuser where id="{uid}" ')
    connectiontofacultyuser.commit()
    return 1

#---------------------------------------------------------------------- IMAGE PROCESSING for student ------------------------------------------------------------------------------------------
connectiontoimagedatabase=sqlite3.connect(stu_dp_path)

def image_insert(rol,img):
    curimg=connectiontoimagedatabase.cursor()
    curimg.execute('insert into stuimg values(?,?)',(rol,img))
    connectiontoimagedatabase.commit()

def updating_image(rol,img):
    curupdate=connectiontoimagedatabase.cursor()
    curupdate.execute(f'update stuimg set image="{img}" where rollno="{rol}"')
    connectiontoimagedatabase.commit()

def deleting_img(rol):
    curdel=connectiontoimagedatabase.cursor()
    curdel.execute(f'update stuimg set image=NULL where rollno="{rol}"')
    connectiontoimagedatabase.commit()

def fetch_rol2():
    roldata=pd.read_sql_query('select rollno from stuimg',connectiontoimagedatabase)
    rolist=roldata['rollno'].tolist()
    connectiontoimagedatabase.commit()
    return rolist

def fetch_image(roll):
    imgdata=pd.read_sql_query(f'select image from stuimg where rollno="{roll}"',connectiontoimagedatabase)
    imglist=imgdata['image'].tolist()
    connectiontoimagedatabase.commit()
    return imglist

def deleting_image_onaccount(roldel):
    curdel=connectiontoimagedatabase.cursor()
    curdel.execute(f'delete from stuimg where rollno="{roldel}"')
    connectiontoimagedatabase.commit()

#---------------------------------------------------------------------- IMAGE PROCESSING for faculty ------------------------------------------------------------------------------------------

connecttofacultyimagedata=sqlite3.connect(fac_dp_path)

def insert_facultyimg(empuniqueid,imgname):
    curtoin=connecttofacultyimagedata.cursor()
    curtoin.execute('insert into facultyimg values(?,?)',(empuniqueid,imgname))
    connecttofacultyimagedata.commit()

def updatefacimg(empid,imgname):
    curtoupdate=connecttofacultyimagedata.cursor()
    curtoupdate.execute(f'update facultyimg set image="{imgname}" where empid="{empid}" ')
    connecttofacultyimagedata.commit()

def deletingfacimg(empid):
    curtodel=connecttofacultyimagedata.cursor()
    curtodel.execute(f'update facultyimg set image=NULL where empid="{empid}" ')
    connecttofacultyimagedata.commit()

def fetchfacid():
    iddata=pd.read_sql_query('select empid from facultyimg',connecttofacultyimagedata)
    idlist=iddata['empid'].to_list()
    connecttofacultyimagedata.commit()
    return idlist

def fetchfacimg(empid):
    imgdata=pd.read_sql_query(f'select image from facultyimg where empid="{empid}" ',connecttofacultyimagedata)
    imglist=imgdata['image'].to_list()
    connecttofacultyimagedata.commit()
    return imglist

def deletingfacimg_onaccount(empid):
    curtofinal=connecttofacultyimagedata.cursor()
    curtofinal.execute(f'delete from facultyimg where empid="{empid}"')
    connecttofacultyimagedata.commit()

#========================================================================FACULTY RESUME SCRIPT====================================================================================
connectiontocv=sqlite3.connect(fac_resume_path)

def upload_resume(empid,filename):
    curtocv=connectiontocv.cursor()
    curtocv.execute('insert into facultycv values(?,?)',(empid,filename))
    connectiontocv.commit()

def update_resume(fname,empid):
    curtoup=connectiontocv.cursor()
    curtoup.execute(f'update facultycv set file="{fname}" where empid="{empid}" ')
    connectiontocv.commit()

def resume_empid():
    cvdat=pd.read_sql_query('select empid from facultycv',connectiontocv)
    cvdatlist=cvdat['empid'].to_list()
    connectiontocv.commit()
    return cvdatlist

def resume_files(empid):
    cvdata=pd.read_sql_query(f'select file from facultycv where empid="{empid}" ',connectiontocv)
    cvlist=cvdata['file'].to_list()
    connectiontocv.commit()
    return cvlist

def removecv(empid):
    currm=connectiontocv.cursor()
    currm.execute(f'delete from facultycv where empid="{empid}" ')
    connectiontocv.commit()

# # #------------------------------------------------------------------------- ROLL NO. CLASH PREVENTION SCRIPT -----------------------------------------------------------------------
# #
def existing_rollno(course,branch,year,sem):
    s1=pd.read_sql_query(f'SELECT roll_no FROM students WHERE course="{course}" AND branch="{branch}" AND year="{year}" AND semester="{sem}"',connection)
    connection.commit()
    roll_no_list=s1['roll_no'].tolist()
    return roll_no_list
#
def existing_empid():
    stafiddat=pd.read_sql_query(f'select emp_id from faculty',connectiontofacultydatabase)
    invalidlist=stafiddat['emp_id'].to_list()
    connectiontofacultydatabase.commit()
    return invalidlist

def valid_rollno():
    s1 = pd.read_sql_query('SELECT roll_no FROM students',connection)
    connection.commit()
    roll_no_list = s1['roll_no'].tolist()
    return roll_no_list
# print(valid_rollno())

def valid_empid():
    s1=pd.read_sql_query('select emp_id from faculty',connectiontofacultydatabase)
    connectiontofacultydatabase.commit()
    idlist=s1['emp_id'].to_list()
    return idlist
#================================================================================   ATTENDANCE MANAGEMENT   ==================================================================

def fillattendance(bname,yname,semname,rolfetch,totallec,taken,subname,monthname):
    curatten=connectiontoattendance.cursor()
    curatten.execute(f'insert into attendance values(?,?,?,?,?,?,?,?)',(bname,yname,semname,rolfetch,totallec,taken,subname,monthname))
    connectiontoattendance.commit()

def rollforattendance(brname,yearn,semname):
    s1 = pd.read_sql_query(f'SELECT roll_no FROM students WHERE branch="{brname}" AND year="{yearn}" and semester="{semname}" ', connection)
    attndrol=s1["roll_no"].tolist()
    connection.commit()
    return attndrol

def aforstudentbymonth(rolno,subj,month):
    a=pd.read_sql_query(f'select total_lec from attendance where rollno="{rolno}" and subject="{subj}" and month="{month}" ',connectiontoattendance)
    alisttl=a['total_lec'].tolist()
    b=pd.read_sql_query(f'select attended_lec from attendance where rollno="{rolno}" and subject="{subj}" and month="{month}" ',connectiontoattendance)
    alistal=b['attended_lec'].tolist()

    return alistal,alisttl
#===================================================================================================================================================================================
def fulldataofstudent(rolnodat):
    fdat=pd.read_sql_query(f'select * from students where roll_no="{rolnodat}"',connection)
    connection.commit()
    fulldata_list=fdat.values.tolist()
    if fulldata_list==[]:
        return 1
    else:
        return fulldata_list[0]

def fulldataoffaculty(empid):
    fdat=pd.read_sql_query(f'select * from faculty where emp_id="{empid}" ',connectiontofacultydatabase)
    connectiontofacultydatabase.commit()
    fuldatoffac=fdat.values.tolist()
    if fuldatoffac==[]:
        return 1
    else:
        return fuldatoffac[0]



#===================================================================================================================================================================================
