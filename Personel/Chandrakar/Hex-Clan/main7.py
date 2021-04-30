from tkinter import *
from functools import partial
from sqlite3 import *
from tkinter.messagebox import *
from PIL import ImageTk
from tkinter import ttk
import datetime


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<< data base connetion user ragistation>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def add_f():
    try:
        if name_var1.get()=="" or email_var1.get()=="":
            showerror("Error","all field are required to fill")

        else:   
            con = database_connection()
            cur = con.cursor()
            sql = "create table if not exists contact(srno INTEGER primary key AUTOINCREMENT,name TEXT,email TEXT,gender TEXT,contact TEXT,dob TEXT,address TEXT)"
            cur.execute(sql)
            sql1 = "insert into contact(name,email,gender,contact,dob,address) values('%s','%s','%s','%s','%s','%s')"
            name = name_var1.get()
            email =email_var1.get()
            gender =gender_var1.get()
            contact =contact_var4.get()
            dob =dob_var5.get()
            address =text_address5.get()

            cur.execute(sql1 % (name ,email,gender,contact,dob,address))
            con.commit()
            fetch_data()
            clear()
            showinfo("Sucsess", "Data stored sucessfully, Please click on contact list ")
    except Exception as e:
        con.rollback()
        print(e)
def fetch_data():
    con = database_connection()
    cur = con.cursor()
    cur.execute("SELECT * from contact")    
    rows = cur.fetchall()
   # print(rows)
    if len (rows)!=0:
        
        for row in rows:
            s9.insert('',END,values=row)
            #print("new  : ",s.insert('',END,values=row))
        print(row)    
        con.commit()
        con.close()    
#<<<<<<<<<<<<<<<<<<<<<<<<<< clear database connection>>>>>>>>>>>>>>>>>
def clear ():
    name_var1.set("")
    email_var1.set("")
    gender_var1.set("")
    contact_var4.set("")
    dob_var5.set("")
    text_address5.set("")
def cursor(ev):
    cursor_row = s9.focus()
    conttents = s9.item(cursor_row)
    row = conttents['values']
    name_var1.set(row[0])
    email_var1.set(row[1])
    gender_var1.set(row[2])
    contact_var4.set(row[3])
    dob_var5.set(row[4])
    text_address5.set(row[5])

def store_registration_data():
    
    if first_name.get()=="" or email_var.get()=="" or security_q.get()=="" or password1.get()=="":
        showerror("Error","All field requard")
    elif password1.get() != c_password1.get():
        showerror("Error","doesn't match password")
    elif checkbtn_var.get()==0:
        showerror("Error","please agree our tearm & condition")    
    else:
        try:
         
            con = database_connection()
            cur = con.cursor()
            sql = "create table if not exists login_user(srno INTEGER primary key AUTOINCREMENT, First_Name text,Last_Name text,contact text,Email text,Security_Q text,Security_A text,password text)"
            cur.execute(sql)
            sql1 = "insert into login_user(First_Name,Last_Name,contact,Email,Security_Q,Security_A ,password) values('%s','%s','%s','%s','%s','%s','%s')"
           
            First_Name = first_name.get()
            Last_Name  = last_name.get()
            contact  = contact_var.get()
            Email  = email_var.get()
            Security_Q = security_q.get()
            Security_A =security_a.get()
            password  = password1.get()

            cur.execute(sql1 % (First_Name,Last_Name,contact,Email,Security_Q,Security_A ,password))
            con.commit()
            showinfo("Sucsess", "Data stored sucessfully, Please click on Login ")
            f8()
        except Exception as e:
            con.rollback()
            print(e)

def database_connection():
    conn = None
    try:
        conn = connect("contact_details3.db")
    except Error as e:
        print("Connection Issue ",  e)
    return conn  
#<<<<<<<<<<<<<<<<<<<<<< update database >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def update_data():
    con = database_connection()
    cur = con.cursor()
    
    con.commit()
    fetch_data()
    clear()
    showinfo("Sucsess", "Data stored sucessfully, Please click on contact list ")

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<log in data base connection>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def user_login():
    if mail.get()=="" or loginpassword.get()=="":
        showerror("Error","All fields are required")
    else:    

        try:
            con = database_connection()
            cur = con.cursor()
            e_mail1 = mail.get()
            password2 = loginpassword.get()
            sql = ("""select * from login_user where Email = '%s' and password = '%s'""" % (e_mail1,password2))
            #print(sql)
            cur.execute(sql)
            row = cur.fetchone()
            if row == None:
                #showinfo("susser","right")
                showerror("Error", "Invaild USER-ID &  PASSWORD")
                
            else:
                f6()
                
        except Exception as e:
            showerror("Error", e)


        













#>>>>>>>>>>>>>>>>>>>>>>>>>define functions  window>>>>>>>>>>>>>>>>>>>>>>




def f8():
    menu.deiconify()
    Register.withdraw()
def f7 ():
    root.deiconify()
    menu.withdraw()
def f6():
    menu.deiconify()
    root.withdraw()
def f4():
    Register.deiconify()        #show register page
    root.withdraw()  

def f5():
    root.deiconify()
    Register.withdraw   
def f3():        #show login page
    root.withdraw()             #hide start page
    root.withdraw()    
             #hide start page
      

#<<<<<<<<<<<<<<<<<<<<<<<<<ragister database   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


root = Tk()
root.title("log in  Page") 
root.geometry("1920x1080")
date = datetime.datetime.now().date()
date =str(date)


left = Frame(root,height=1000,width=1400,bg='white',bd=10).place(x=0,y=0)
cg=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/2154012.jpg")
bg_image=Label(root,image=cg,bg='#34baeb',bd=4).place(x=200,y=0)
date_lbl=Label(root,text="Today's date:"+date,font='arial 15 bold',fg='#327fa8',bg='white').place(x=1050,y=60)

cg1=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/p2.png")
bg_image1=Label(root,image=cg1,bg='white').place(x=20,y=50)

#<<<<<<<<<<<<<<<<<<<<center fram>>>>>>>>>>>>>>>>>>>
center = Frame(left,height=400,width=400,bg='white',bd=10).place(x=500,y=150)
#pc=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/log.png")
#pc_image1=Label(root,image=pc,bg='white',bd=50).place(x=600,y=50)

#<<<<<<<<<<<<<<username >>>>>>>>>>>>>>>>>>>>>>>>
pc1=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/user.png")
pc_image2=Label(root,image=pc1,bg='white',bd=50).place(x=570,y=155)
pc2=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/pass1.png")
pc_image3=Label(root,image=pc2,bg='white',bd=50).place(x=570,y=220)

userid = Label(center,text="Username",font="Liberation  15 ",bg='white',fg='#eb0578').place(x=650,y=200)
mail = StringVar()
txtuser = ttk.Entry(center , font="Liberation  10 ",textvariable=mail).place(x=635,y=230)

#<<<<<<<<<<<<<<<<<<<user password>>>>>>>>>>>>>>>>

userpassword = Label(center,text="Password",font="Liberation  15 ",bg='white',fg='#eb0578').place(x=650,y=260)
loginpassword = StringVar()
txtpass = ttk.Entry(center , font="Liberation  10 ",textvariable=loginpassword,show='*').place(x=635,y=290)

#<<<<<<<<<<<<<<<<<<<<<login botton>>>>>>>>>>>>>>>>>>>

#pc3=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/login2.png")
#pc_image4=Label(root,image=pc3,bg='blue',bd=0)
log_in = Button(center,text=" log in ",bg="#eb3449",fg="white",cursor="hand2",command=user_login,font="arial  10 bold",bd=0).place(x=770,y=400)

#<<<<<<<<<<<<<<<<<<<<ragister>>>>>>>>>>>>>>>>>>>>>>>

ragister_in = Button(center,text="register now ",cursor="hand2",bg="#34aeeb",fg="white",command=f4,font="arial  10 bold ",bd=0,height=1,width=10).place(x=520,y=400)

#pc5=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/go.png")
#pc_image6=Label(root,image=pc5,bg='white',bd=0)
#ragister_in = Button(center,image=pc5,cursor="hand2",font="arial  15 bold",bd=0,bg='white').place(x=900,y=300)

#pc6=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/fb.png")
#pc_image7=Label(root,image=pc6,bg='white',bd=0)
#ragister_in = Button(center,image=pc6,cursor="hand2",font="arial  15 bold",bd=0,bg='white').place(x=900,y=375)
#>>>>>>>>>>>>>>>>>>>>>>>forget password>>>>>>>>>>>>>>>>>>>>>>>>

forget_p = Label(center,text="Forget password",cursor="hand2",font="Liberation  8 ",bd=0,bg='white',fg='#2ea5e6').place(x=520,y=370)





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ragistation>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


Register = Toplevel(root)
Register.title("Add St.")
Register.geometry("1920x1080")

left1 = Frame(Register,height=1000,width=1400,bg='white',bd=10).place(x=0,y=0)
cg8=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/rag.jpg")
bg_image8=Label(Register,image=cg8,bg='red',bd=4).place(x=200,y=0)
date_lbl2=Label(Register,text="Today's date:"+date,font='arial 15 bold',fg='#327fa8',bg='white').place(x=1050,y=50)

cg9=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/p2.png")
bg_image9=Label(Register,image=cg9,bg='white').place(x=20,y=50)


#<<<<<<<<<<<<<<<<<<<<<<Varibal name>>>>>>>>>>>>>>>>>>>>>>>>>>>>

first_name = StringVar()
last_name  = StringVar()
contact_var = StringVar()
email_var   = StringVar()
security_q  = StringVar()
security_a  = StringVar()
password1   = StringVar()
c_password1 = StringVar()
#ragistation

center1     = Frame(Register,height=500,width=800,bg='white',bd=10).place(x=300,y=90)
ragister_lb1 = Label(Register,text="REGISTER HERE",font=("times new roman", 20,"bold"),fg="green",bg="white").place(x=300,y=100)

#

#<<<<<<<<<<<<<<<<<<<<<<<<<leble and frem>>>>>>>>>>>>>>>>>>>>>>>>
fname = Label(Register,text="First Name",font=("times new roman", 15,"bold"),fg="black",bg="white").place(x=330,y=150)
fname_e = ttk.Entry(Register , font=("times new roman", 15),textvariable=first_name).place(x=330,y=180)

#<<<<<<<<<<<<<<<<<<<<<<<last name>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
lname = Label(Register,text="Last Name",font=("times new roman", 15,"bold"),fg="black",bg="white").place(x=630,y=150)
lname_e = ttk.Entry(Register , font=("times new roman", 15),textvariable=last_name).place(x=630,y=180)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<contact number>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
cname = Label(Register,text="Contact Number",font=("times new roman", 15,"bold"),fg="black",bg="white").place(x=330,y=230)
cname_e = ttk.Entry(Register , font=("times new roman", 15),textvariable=contact_var).place(x=330,y=260)
#<<<<<<<<<<<<<<<<<<<<<<<<<<E-mail>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ename = Label(Register,text="E-mail",font=("times new roman", 15,"bold"),fg="black",bg="white").place(x=630,y=230)
ename_e = ttk.Entry(Register , font=("times new roman", 15),textvariable=email_var).place(x=630,y=260)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Select Security Qestions>>>>>>>>>>>>>>>>>>>
sname = Label(Register,text="Select Security Qestions",font=("times new roman", 15,"bold"),fg="black",bg="white").place(x=330,y=310)
values = ["Select","Your birth place","Your 1st school name","your best friend name"]
cmb=ttk.Combobox(Register,value=values,textvariable=security_q,width=24,height=80)
cmb.place(x=330,y=340)
cmb.current(0)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Security Answer>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
scname = Label(Register,text="Security Answer",font=("times new roman", 15,"bold"),fg="black",bg="white").place(x=630,y=310)
scname_e = ttk.Entry(Register , font=("times new roman", 15),textvariable=security_a).place(x=630,y=340)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Pssword>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
pass_name = Label(Register,text="Password",font=("times new roman", 15,"bold"),fg="black",bg="white").place(x=330,y=390)
Pass_name_e = ttk.Entry(Register , font=("times new roman", 15),textvariable=password1,show='*').place(x=330,y=420)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Confrim Password>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
scname = Label(Register,text="Confrim Password",font=("times new roman", 15,"bold"),fg="black",bg="white").place(x=630,y=390)
scname_e = ttk.Entry(Register , font=("times new roman",15),textvariable=c_password1,show='*').place(x=630,y=420)

#<<<<<<<<<<<<<<<<<<<<<<<<<<Check button>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
checkbtn_var = IntVar()
checkbtn = Checkbutton(Register,variable=checkbtn_var,text="I Agree The Terms & condition",bg="white",font=("times new roman", 10,"bold"),onvalue=1,offvalue=0).place(x=330,y=480)


#<<<<<<<<<<<<<<<<<<<<<<<<<ragister button>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#pc10=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/ragi1.png")
#pc_image10=Label(Register,image=pc10,bg='blue',bd=0)
ragister_in = Button(Register,text="register now ",cursor="hand2",command=store_registration_data,font="arial  10 bold",bd=0,bg="#eb3449",height=1,width=10).place(x=330,y=520)
#ragister_in = Button(center,text="register now ",cursor="hand2",bg="#34aeeb",fg="white",command=f4,font="arial  10 bold ",bd=0,height=1,width=10).place(x=520,y=400)
#<<<<<<<<<<<<<<<<<<<<<<<<Log in button >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#pc11=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/login3.png")
#pc_image11=Label(root,image=pc11,bg='blue',bd=0)
log_in = Button(Register,text="log in ",cursor="hand2",font="arial  15 bold",command=f5,bg='#34aeeb',bd=0,height=1,width=15).place(x=630,y=490)

Register.withdraw()



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Menu page >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
menu=Toplevel(root)
menu.title("Contact book")
menu.geometry("1920x1080")
date = datetime.datetime.now().date()
date =str(date)


top20 = Frame(menu,height=170,width=1400,bg='white').place(x=0,y=0)
bottom20=Frame(menu,height=550,width=1400,bg='#34baeb').place(x=0,y=170)


bg20=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/p2.png")
bg_image20=Label(menu,image=bg20,bg="white").place(x=120,y=10)

bg21=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/co1.gif")
bg_image21=Label(menu,image=bg21,bg="white").place(x=600,y=60)


headling3=Label(menu,text='My Contact book',font='arial 25 bold',bg='white',fg='#327fa8').place(x=500,y=10)
date_lbl3=Label(menu,text="Today's date:"+date,font='arial 15 bold',fg='#327fa8',bg='white').place(x=1000,y=60)
contact_frame3 = Frame(menu,bd=4,relief=RIDGE,bg='#4290f5').place(x=0,y=170,width=450,height=532)  
c_title3 = Label(menu,text="contact book",font='arial 25 bold',bd=4,relief=RIDGE,fg="#327fa8",bg="white").place(x=70,y=170)
     
lbl_name3 = Label(menu,text="Full Name",font='arial 15 bold',bg='#4290f5',fg='white').place(x=20,y=250)
name_var1 = StringVar()
c_name3 = Entry(menu, textvariable = name_var1, bd = 2).place(x=180,y=250)


       
lbl_email5 = Label(menu,text="E-mail",font='arial 15 bold',bg='#4290f5',fg='white').place(x=20,y=295)
email_var1 = StringVar()
email_name1 = Entry(menu, textvariable = email_var1, bd = 2).place(x=180,y=300)
        

lbl_gender1 = Label(menu,text="Gender",font='arial 15 bold',bd=4,bg='#4290f5',fg='white').place(x=20,y=340)
gender_var1 = StringVar()
values1 = ["male","female","other"]
cmb1=ttk.Combobox(menu,textvariable=gender_var1,value=values1,width=19,height=70)
cmb1.place(x=180,y=350)
cmb1.current(0)

lbl_contact4 = Label(menu,text="Contact",font='arial 15 bold',bg='#4290f5',fg='white').place(x=20,y=390)
contact_var4= StringVar()
co_name4 = Entry(menu, textvariable = contact_var4, bd = 2).place(x=180,y=390) 

lbl_dob5 = Label(menu,text="D.O.B",font='arial 15 bold',bg='#4290f5',fg='white').place(x=20,y=440)
dob_var5 = StringVar()
dob_name5 = Entry(menu, textvariable = dob_var5, bd = 2).place(x=180,y=440) 

lbl_address5 = Label(menu,text="Address",font='arial 15 bold',bg='#4290f5',fg='white').place(x=20,y=490)
text_address5 = StringVar()
address_name5 = Entry(menu,textvariable=text_address5, bd = 2,font='arial 10 bold').place(x=180,y=490 )   

#<<<<<<<<<<<<botton frame >>>>>>>>>>>>>>>
cg6=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/con.png")
up6=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/up.png")
de6=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/de.png")
cl6=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/cl.png")

bg_image6=Label(menu,image=cl6,bg='#4290f5').place(x=335,y=530)
bg_image6=Label(menu,image=de6,bg='#4290f5').place(x=235,y=530)
bg_image6=Label(menu,image=up6,bg='#4290f5').place(x=135,y=530)
bg_image6=Label(menu,image=cg6,bg='#4290f5').place(x=35,y=530)
btn_frame6 = Frame(menu,bd=3,relief=RIDGE,bg="#4290f5",height=50,width=400).place(x= 20,y= 600)


#add bottons
addbtn7 = Button(menu,text="Add",bg='white',command=add_f,bd=2).place(x=40,y=610)

updbtn7 = Button(menu,text="Update",command=update_data,bg='white',bd=2).place(x=130,y=610)
deldbtn7 = Button(menu,text="Delet",bg='white',bd=2).place(x=240,y=610)
clbtn7 = Button(menu,text="Clear",bg='white',command=clear,bd=2).place(x=340,y=610)


deitel_frame7 = Frame(menu,bd=4,relief=RIDGE,bg='#4290f5').place(x=510,y=170,width=783,height=532)    

c_search7 = Label(menu,text="Search By",bg='#4290f5',font='arial 20 bold',fg="white").place(x=530,y=200)

search7 = ["Name","contact","Email"]
cmb8=ttk.Combobox(menu,value=search7,width=20,height=30)
cmb8.grid(row=3,column=4,padx=700,pady=210)
cmb8.current(0)


log8=ImageTk.PhotoImage(file = "/home/hp/Desktop/project/exit.png")
bg_image8=Label(menu,image=log8,bg='white').place(x=1010,y=100)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#display = Button(menu,font="arial  15 bold",text=email_var.get(),bg='white',bd=0).place(x=500,y=30)

#<<<<<<<<<<<<<<<<, LOG OUT  buttom>>>>>>>>>>>>>>>>>>>>>>>>>>>
logout_btn8 = Button(menu,text="Log out",bg='white',font='arial 15 bold',command=f7,fg='#327fa8',bd=2).place(x=1125,y=110)
btn_search8 = Entry(menu,font='arial 15 bold', bd = 2,width=10).place(x=910,y=205) 
search_btn8 = Button(menu,text="Search",bg='white',bd=2).place(x=1060,y=205)
search_all8 = Button(menu,text="Show all",bg='white',bd=2).place(x=1160,y=205)
#>>>>>>>>>>>>>>>>table frame>>>>>>>>>>>>>>
table_frame9 = Frame(menu,bd=4,relief=RIDGE,bg='white').place(x=530,y=270,width=745,height=410)
        
  
scroll_x9 = Scrollbar(menu,orient=HORIZONTAL)
scroll_y9 = Scrollbar(menu,orient=VERTICAL)
s9 = ttk.Treeview(menu,column=("srno","Full name","E-mail","Gender","Contact","D.O.B.","Address"),xscrollcommand=scroll_x9.set,yscrollcommand=scroll_y9.set)
scroll_x9.place(x=530 , y= 670,width=745,height=20)
scroll_y9.place(x=1270,y=270,height=420,width=20)

scroll_x9.config(command=s9.xview)
scroll_y9.config(command=s9.yview)


s9['show'] = 'headings'
s9.column("srno",width=100)
s9.column("Full name",width=100)
s9.column("E-mail",width=100)
s9.column("Gender",width=100)
s9.column("Contact",width=100)
s9.column("D.O.B.",width=100)
s9.column("Address",width=100)
        

s9.heading("srno",text="srno")
s9.heading("Full name",text="Full name")
s9.heading("E-mail",text="E-mail")
s9.heading("Gender",text="Gender")
s9.heading("Contact",text="Contact")
s9.heading("D.O.B.",text="D.O.B.")
s9.heading("Address",text="Address")
s9.place(x=530,y=270,height=400,width=740)
s9.bind("<ButtonRelease-1>",cursor)


menu.withdraw()









root.mainloop()