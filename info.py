#----------------------------------------------------   PATH FINDING    -----------------------------------------------
import os

installed_path=os.getcwd()

cg_logo=f'{installed_path}//CampusGuide//softwaredependencies//configurations//subdata//softlookNfeel//bitimagelogoCG//mainlogo.ico'

#--------------------------------------------   Paths  -------------------------------------------------------------------------
fac_resume_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//faculty_data_warehouse-Untouch//facultyResumeDataBase//facultyresume_file.db'
fac_cv_file_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//faculty_data_warehouse-Untouch//facultyResumeDataBase//cvs'
#----------------------------------------------------   FACULTY D_P IMAGES   -----------------------------------------------

fac_dp_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//faculty_data_warehouse-Untouch//facultyProfileDatabaseFiles//database(.db)_FAC_FILE//facimagedata_file.db'
fac_displaypic_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//faculty_data_warehouse-Untouch//facultyProfileDatabaseFiles//faculty_image_DP'
#---------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------   STUDENT D_P IMAGES   -----------------------------------------------

stu_dp_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//student_data_warehouse-Untouch//studentProfileDatabaseFile//database(.db)file//imagedata_file.db'
stu_displaypic_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//student_data_warehouse-Untouch//studentProfileDatabaseFile//student_image_DP'
#---------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------  D A T A B A S E S  -----------------------------------------------

stu_warehouse_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//student_data_warehouse-Untouch//studentmaindatabase_warehouse//studentdatabase_file.db'

fac_warehouse_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//faculty_data_warehouse-Untouch//facultymain_datawarehouse//facultydatabase_file.db'

fee_database_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//student_data_warehouse-Untouch//studentFeeDataBaseFiles//students_fee_database.db'

attendance_database_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//student_data_warehouse-Untouch//studentAttendanceDatabaseFiles//attendancedata.db'

stu_accountDatabase_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//student_data_warehouse-Untouch//studentUserAccountDatabaseFiles//student_signupdata_file.db'

fac_accountDatabase_path=f'{installed_path}//CampusGuide//database\sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//faculty_data_warehouse-Untouch//facultyUserAccountDatabaseFile//faculty_signupdata_file.db'

admin_accountDatabase_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//ADMIN-Untouch//hashval-999012219090//dataval290670-UNTOUCH//admin_access//admindatabase_file.db'

#----------------------------------------------------  C O M P O N E N T S   -----------------------------------------------
components_path=f'{installed_path}//CampusGuide//softwaredependencies//configurations//subdata//softlookNfeel//canimages'

#----------------------------------------------------  L I B R A R Y  -----------------------------------------------

librarydatabase_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//library_data_warehouse-Untouch//library_books_database.db'

library_issued_books_path=f'{installed_path}//CampusGuide//database//sqldata//databaseconfigurationfiles//ACCESS_NOT_RECOMENDED//library_data_warehouse-Untouch//library_bookIssued_database.db'

#---------------------------------------------------------------------------------------------------------------------

courses=['select','B.Tech','M.Tech','BSc/UG','MSc']

btech_fileld=['select','CSE','Mechanical Engg.','Electrical Engg.','Civil Engg.']

btech_years=['select','1st year','2nd year','3rd year','4th year']

bsc_fields=['select','Bsc(PMC)','Bsc(H).Phy','Bsc(H).Maths','Bsc(H).Chemisty','Bsc(H).Life Science','B.Com','BBA','BCA']

ug_years=['select','1st year','2nd year','3rd year']

btech_fee=[45000]
bsc_fee=[35000]
mtech_fee=[40000]
msc_fee=[38000]

optionlist=['Home','Profile','Log Out']

#----------------------------------------------------------------  subjects LISTS -----------------------------------------------------------------------------

all_branches=btech_fileld+bsc_fields

#------------------------------------------------------------------- B.Tech Subjects --------------------------------------------------------------------------

#===================================== C S E ======================================================================
btechcse11subs=['Maths-1','Physics-1','Industrial Chemistry','FCFS','Basics of electronics']
btechcse12subs=['Maths-2','Physics-2','Basics of mechanics','Basics of civil engg.']
btechcse23subs=['SPSA','Discrete Mathemetics','Computer Architecture','IWT','Data structures']
btechcse24subs=['Database Management','OOPS','Multimedia Technology','Algorithms','Operating System']
btechcse35subs=['Computer Networks','Cryptography','Theory of Computation','Computer Graphics','Image Processing']
btechcse36subs=['Artificial Intelligance','Language Processing','Data Communication','Software Engineering']
btechcse47subs=['Visual Programming techniques','Java Programming','Distributed System','System Programming']
btechcse48subs=['Robotics','Compiler Design','Network IP']

btechcse_subsem_list=[btechcse11subs,btechcse12subs,btechcse23subs,btechcse24subs,btechcse35subs,btechcse36subs,btechcse47subs,btechcse48subs,]
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#===================================== Mechanical==================================================================
btechmec11subs=['Maths-1','Physics-1','Chemistry-1','Engineering Graphics']
btechmec12subs=['Maths-2','Physics-2','Electrical technology','Engineering Mechanics']
btechmec23subs=['Value Education','Mechanics Of Solid','Maths-3','Applied Thermodynamics']
btechmec24subs=['Fluid Mechanics','Dynamics Of Machinary','Numaerical Methods','Electrical Machines and Control']
btechmec35subs=['Fluid Mechanics-2','Heat And Mass Transfer','Production Technology','Indusstrial Engineering']
btechmec36subs=['Internal Combustion Engine','Mechanical Vibrations','Computer Aided Design','Production Technology-2']
btechmec47subs=['Measurement And Instrumerntation','Operations Reserch','Energy Conversion','Mechatroniocs']
btechmec48subs=['Advance Fluid Mechanics','Automobile Engineering','Finite Element Analysis','Automation And Robotics']

btechmec_subsem_list=[btechmec11subs,btechmec12subs,btechmec23subs,btechmec24subs,btechmec35subs,btechmec36subs,btechmec47subs,btechmec48subs,]
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#===================================== Civil =======================================================================
btechcivil11subs=['Surveying-land','Physics-1','Maths-1','Chemistry']
btechcivil12subs=['Physics-2','Maths-2','Chemistry-2','Material Science']
btechcivil23subs=['Coastal Engineering','Constuction Engineering','Building Technology','Structural Analysis']
btechcivil24subs=['Geotechnical Engineering','Environmental Engineering','Forensic Engineering','Architecture and Town Planning']
btechcivil35subs=['Erthquake Engineering','Hydraulic Structure','Control Strucrures','Urban Engineering']
btechcivil36subs=['Steel Structure Design','Transportation Engineering','Structural Drawing','Survay camp']
btechcivil47subs=['Foundation Engineering','Project Management','Solid Waste',' Environmental Polution']
btechcivil48subs=['Design Of Hydraaulic Structure-2','Communication Skills','Thermodynamics']

btechcivil_subsem_list=[btechcivil11subs,btechcivil12subs,btechcivil23subs,btechcivil24subs,btechcivil35subs,btechcivil36subs,btechcivil47subs,btechcivil48subs,]
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#===================================== Electrical ==================================================================
btechece11subs=['Maths-1','Engineering graphics','Physics-1','Chemisstry-1']
btechece12subs=['Maths-2','Physics-2','Electrical technology','Electronics and Instrumentation']
btechece23subs=['Mechanics of Solid','Circuit Theory','Digital Circuits','Applied Thermodynamics']
btechece24subs=['Electrical Measurements','Megnatism and electricity','Analouge Circuits','Signals And System']
btechece35subs=['Electrical Machines-2','Power System','Digital Signal Processing','Field Theory']
btechece36subs=['Power Electronics','Instrumentation','Power System-2','Control System-2']
btechece47subs=['Electrical Devices','Advance Power Electronics','Electrical Transportation','Artificial Intelligance']
btechece48subs=['Computer Applications','Static Relays','Filter Design','Robotics']

btechece_subsem_list=[btechece11subs,btechece12subs,btechece23subs,btechece24subs,btechece35subs,btechece36subs,btechece47subs,btechece48subs,]
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````

main_btech_sujects=['.',btechcse_subsem_list,btechmec_subsem_list,btechece_subsem_list,btechcivil_subsem_list]
#------------------------------------------------------------------------------------------------------------------

#--------------------- BSc Subjects ------------------------------------------------------------------------------
#===================================== BSc (PCM) =================================================================
bsc11subs=['Maths-1','English','Hindi','Physics','Chemistry']
bsc12subs=['Computers','Englisj-2','Digital Electronics','Maths-2']
bsc23subs=['Maths-3','English-3','Botany','Zoology']
bsc24subs=['Maths-4','Physics','Statistics','Number Series']
bsc35subs=['Computer Networks','Basics of Digital electronics','Maths-5','English-4']
bsc36subs=['Physics-Q','Maths-6','English-5','P.com']


#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#===================================== BSc(H)Phy =================================================================
bschphy11subs=['Mathematical Phy','Electricity and Megnetism','Chemistry','Digital Electronics']
bschphy12subs=['Oscillations and Wave','Thermal Physics','Optics','Numerical Analysis']
bschphy23subs=['Atomic and Molicular Phy','Electromegnetic Theory','Solid State','Mechanics and wave']
bschphy24subs=['Elements of Modren Phy','Mechanics','Wave and Optics','Digital Systems']
bschphy35subs=['Microprocessor and Computers','Mathemetics','Quantum Mechanics','Electronic Devices']
bschphy36subs=['Statistical Mechanics','Kinetic Theory','Analog system','Motion','P.com']
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#===================================== BSc(H)Maths =================================================================
bschmath11subs=['Calculus','Basic Statistics','Probability','Matrices']
bschmath12subs=['Sequence and series of Numbers','Abstract Algebra','Theory Of Real Functions','Discrete Mathemetics']
bschmath23subs=['Linear Programming','Vector Analysis','Algebra','Real Analysis']
bschmath24subs=['Diffrential Equations','Data structures','Operating System','Mechanics']
bschmath35subs=['Leniar Programming','Ring Theory','Complex Analysis','Numerical Analysis']
bschmath36subs=['integration','Diffrential Equations','Permutation','P.com']
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#===================================== BSc(H)Chem =================================================================
bschchem11subs=['Atomic Structure','Periodic Proerties','Chemical Bonding','s-Block Elements']
bschchem12subs=['Structures And Bonding','Organic reactions','Alkanes and cycloalkanes','Organic Compounds']
bschchem23subs=['Akkyl and Aryl Halides','Arenes and Atomicity','Metemetical Concepts','Colloidal State']
bschchem24subs=['Liquid State','Computers','Gaseous State','Solid State']
bschchem35subs=['Chemical Kinetics','Molicular Structures','Inorganic Compounds','Hydrogen']
bschchem36subs=['Periodic table','Metals and alloys','Industrial Chemicals','Acids and Base']
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#===================================== BSc(H)Lifescience ===========================================================
bschlfsci11subs=['Applied Biology','Biochemistry','Biodiversity','Biology']
bschlfsci12subs=['Cell Structure','Bioinformatics','Chemistry','Cell Biology']
bschlfsci23subs=['Physiology of Plants','Botany','Zoology','Genetics']
bschlfsci24subs=['Food and Nutritions','Computers','Immunology and Animals','Medical Diagnostics']
bschlfsci35subs=['Methemetics for Life Science','Microbiology','Physics','Human Anatomy']
bschlfsci36subs=['Environmental Science','Evolution','Genitic Engineering','Plants Tissues']
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#===================================== B.Com subjects ===========================================================
bcom11subs=['commingsoon!']
bcom12subs=[]
bcom23subs=[]
bcom24subs=[]
bcom35subs=[]
bcom36subs=[]
bcom_subsem_list=[bcom11subs,bcom12subs,bcom23subs,bcom24subs,bcom35subs,bcom36subs,]
#------------------------------------------------------------------------------------------------------------------

subjects_of_branches=main_btech_sujects

choice_list=['Yes','No']
#----------------------------------------------------------------  ROLL NO. LISTS -----------------------------------------------------------------------------

btechrol11=[]

#----------------------------------------------------------------  Emp Id. LISTS -----------------------------------------------------------------------------

staff_empidlist=[]

#----------------------------------------------------------------   D I R E C T O R Y PATHS -----------------------------------------------------------------------------
studir_path = stu_displaypic_path
facdir_path=fac_displaypic_path


students_tabs=['Home','Student Profile','User Profile','Attendance','Request a change','Your Curriculum','College Notice','Help!']
faculty_tabs=['Home','Personal Info.','User Profile','Fill Attendance','Syllabus','Notes','College Notice','Help!']

#----------------Faculty---------------
staff_title=['Dean','H.O.D','Professor','Assistant Professor','Librarian']


departments=['Computer Science','Faculty of life science','Physical Science','Commerse','Library']


semesters=['1st semester','2nd semester','3rd semester','4th semester','5th semester','6th semester','7th semester','8th semester']
ugsem=['1st semester','2nd semester','3rd semester','4th semester','5th semester','6th semester']

semester_btech=['1st','2nd','3rd','4th','5th','6th','7th','8th']
semester_bsc=['1st','2nd','3rd','4th','5th','6th']
#----------DATES DATA--------------------------------------
datesforoddmonts=[i for i in range(1,32)]
datesforevenmonts=[i for i in range(1,31)]
datesforfeb=[i for i in range(1,29)]
#----------------------------------------------------------

#-------------------MONTHS AND YEAR------------------------
months=['Jan','Feb','March','April','May','June','July','August','Sept','Oct','Nov','Dec']
oddmonths=['Jan','March','May','July','August','Oct','Dec']
yearofdob=[i for i in range(1990,2030)]
#----------------------------------------------------------


