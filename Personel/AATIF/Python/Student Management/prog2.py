from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

win = tk.Tk()
win.geometry("1400x700+0+0")
win.title("Student Management System")

#----------------------------------->           Detail Entry    <-----------------------------------------

detail_ent = tk.LabelFrame(win,text = "Enter Details", font = ("Arial",20), bd = 3, relief = tk.GROOVE)
detail_ent.place(x = 20 , y = 40, width = 420, height = 630)

#----------------------------------->           Detail Frame    <-----------------------------------------

detail_frame = tk.LabelFrame(win,bd = 3, relief = tk.GROOVE)
detail_frame.place(x = 475 , y = 50, width = 810, height = 630)

#***********************************                Variable            **************************************************************************

name = tk.StringVar()
rollno = tk.StringVar()
section = tk.StringVar()
class_ = tk.StringVar()
fathersname = tk.StringVar()
Gender = tk.StringVar()
dob = tk.StringVar()
contact = tk.StringVar()
address = tk.StringVar()
search_by = tk.StringVar()
search_txt = tk.StringVar()

#----------------------------------->           Roll No.Col     <-----------------------------------------

roll_lable = tk.Label(detail_ent, text = "Roll No: ", font = ("Arial", 15))
roll_lable.grid(row = 0, column = 0, padx = 0, pady = 6)

roll_entry = tk.Entry(detail_ent,bd = 3, font = ("Arial", 15), textvariable = rollno)
roll_entry.grid(row = 0, column = 1, padx = 2, pady = 6)

#----------------------------------->           Name .Col       <-----------------------------------------


name_lable = tk.Label(detail_ent, text = "NAME: ", font = ("Arial", 15))
name_lable.grid(row = 1, column = 0, padx = 0, pady = 6)

name_entry = tk.Entry(detail_ent,bd = 3, font = ("Arial", 15), textvariable = name)
name_entry.grid(row = 1, column = 1, padx = 2, pady = 6)

#----------------------------------->           Class .Col      <-----------------------------------------


class_lable = tk.Label(detail_ent, text = "Class: ", font = ("Arial", 15))
class_lable.grid(row = 2, column = 0, padx = 0, pady = 6)

class_entry = tk.Entry(detail_ent,bd = 3, font = ("Arial", 15), textvariable = class_)
class_entry.grid(row = 2, column = 1, padx = 2, pady = 6)

#----------------------------------->           Section .Col    <-----------------------------------------


section_lable = tk.Label(detail_ent, text = "Section: ", font = ("Arial", 15))
section_lable.grid(row = 3, column = 0, padx = 0, pady = 6)

section_entry = tk.Entry(detail_ent,bd = 3, font = ("Arial", 15), textvariable = section)
section_entry.grid(row = 3, column = 1, padx = 2, pady = 6)

#----------------------------------->            Contact .col   <-----------------------------------------


contact_lable = tk.Label(detail_ent, text = "Contact: ", font = ("Arial", 15))
contact_lable.grid(row = 4, column = 0, padx = 0, pady = 6)

contact_entry = tk.Entry(detail_ent,bd = 3, font = ("Arial", 15), textvariable = contact)
contact_entry.grid(row = 4, column = 1, padx = 2, pady = 6)

#----------------------------------->            D.O.B .Col     <-----------------------------------------


dob_lable = tk.Label(detail_ent, text = "D.O.B: ", font = ("Arial", 15))
dob_lable.grid(row = 5, column = 0, padx = 0, pady = 6)

dob_entry = tk.Entry(detail_ent,bd = 3, font = ("Arial", 15), textvariable = dob)
dob_entry.grid(row = 5, column = 1, padx = 2, pady = 6)


#----------------------------------->            Address .Col   <-----------------------------------------

address_lable = tk.Label(detail_ent, text = "Address: ", font = ("Arial", 15))
address_lable.grid(row = 6, column = 0, padx = 0, pady = 6)

address_entry = tk.Entry(detail_ent,bd = 3, font = ("Arial", 15), textvariable = address)
address_entry.grid(row = 6, column = 1, padx = 2, pady = 6)


#----------------------------------->            Gender .Co     <-----------------------------------------

gender_lable = tk.Label(detail_ent, text = "Gender: ", font = ("Arial", 15))
gender_lable.grid(row = 7, column = 0, padx = 0, pady = 6)

gender_entry = ttk.Combobox(detail_ent, font = ("Arial", 15),width = 19, textvariable = Gender, state = "readonly")
gender_entry['value'] = ["Male", "Female", "Other"]
gender_entry.grid(row = 7, column = 1, padx = 0, pady = 6)


#----------------------------------->       Fathers' Name .Col   <-----------------------------------------



fname_lable = tk.Label(detail_ent, text = "Father's Name: ", font = ("Arial", 15))
fname_lable.grid(row = 8, column = 0, padx = 0, pady = 6)

fname_entry = tk.Entry(detail_ent,bd = 3, font = ("Arial", 15), textvariable = fathersname)
fname_entry.grid(row = 8, column = 1, padx = 2, pady = 6)

#****************************************************************************************************************************************************

#************************************               Database Connectivity     ***********************************************************************

def fetch_data() :
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "studentmanagementsys")
    curr = conn.cursor()
    curr.execute("SELECT * FROM student_data1")
    rows = curr.fetchall()
    if len(rows)!= 0 :
        stud_table.delete(*stud_table.get_children())
        for row in rows :
            stud_table.insert('',tk.END, values = row)
        conn.commit()
    conn.close()

#************************************         Function For Adding The Data       **********************************************************************


def add_func() :
    if  name.get() == "" or rollno.get() == "" :
        messagebox.showerror("Error!","Please Fill All The Fields!")
    else :
        conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "studentmanagementsys")
        curr = conn.cursor()
        curr.execute("INSERT INTO student_data1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name.get(),rollno.get(), section.get(), class_.get(), fathersname.get(), Gender.get(), dob.get(), contact.get(), address.get()))
        conn.commit()
        conn.close()

        fetch_data()  #---------> This Fetch Data After Adding The New Data Into Database

#************************************         Function For rows in search Bar    ********************************************************************

def get_cursor(event) :
    cursor_row = stud_table.focus()
    content = stud_table.item(cursor_row)
    row = content['values']
    name.set(row[0])
    rollno.set(row[1])
    section.set(row[2])
    class_.set(row[3])
    fathersname.set(row[4])
    Gender.set(row[5])
    dob.set(row[6])
    contact.set(row[7])
    address.set(row[8])

#************************************              Function For Clear All fields    ******************************************************************

def clear() :
    name.set("")
    rollno.set("")
    section.set("")
    class_.set("")
    fathersname.set("")
    Gender.set("")
    dob.set("")
    contact.set("")
    address.set("")

    
#************************************               Function For Updating Data    ********************************************************************

def update_func() :
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "studentmanagementsys")
    curr = conn.cursor()
    curr.execute("update student_data1 set name = %s, section = %s, class_ = %s, fathersname = %s, Gender = %s, dob = %s, contact = %s, address = %s where rollno = %s", (name.get(), section.get(), class_.get(), fathersname.get(), Gender.get(), dob.get(), contact.get(), address.get(), rollno.get()))
    conn.commit()
    fetch_data()
    clear()
    conn.close()

#************************************               Function For Deleting Data    ********************************************************************

def delete() :
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "studentmanagementsys")
    curr = conn.cursor()
    curr.execute("delete from student_data1 where rollno = %s", rollno.get())
    conn.commit()
    conn.close()
    fetch_data()
    clear()

#************************************               Function For Searching Data    ********************************************************************

def search() :
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "studentmanagementsys")
    curr = conn.cursor()
    curr.execute("select * from student_data1 where " + str(search_by.get()) + " Like '%" + str(search_txt.get()) + "%'")
    rows = curr.fetchall()
    if len(rows)!= 0 :
        stud_table.delete(*stud_table.get_children())
        for row in rows :
            stud_table.insert('', END, values = row)
        conn.commit()
    conn.close()
       

#----------------------------------->              Button Frame         <-----------------------------------------

btn_frame = tk.Frame(detail_ent, bd = 5, relief = tk.GROOVE)
btn_frame.place(x = 15, y = 450,width = 390, height = 120)

#----------------------------------->              Accept Button        <-----------------------------------------

add_btn = tk.Button(btn_frame, text = "Accept", bd = 7, font = ("Arial", 13), width = 14, command = add_func)
add_btn.grid(row = 0, column = 0, padx = 2, pady = 2)

#----------------------------------->              Update Button        <-----------------------------------------

update_btn = tk.Button(btn_frame, text = "Update", bd = 7, font = ("Arial", 13), width = 14, command = update_func)
update_btn.grid(row = 0, column = 1, padx = 3, pady = 2)

#----------------------------------->              Delete Button        <-----------------------------------------

del_btn = tk.Button(btn_frame, text = "Delete", bd = 7, font = ("Arial", 13), width = 14, command = delete)
del_btn.grid(row = 1, column = 0, padx = 3, pady = 2)

#----------------------------------->              Clear Button         <-----------------------------------------

clear_btn = tk.Button(btn_frame, text = "Clear", bd = 7, font = ("Arial", 13), width = 14, command = clear)
clear_btn.grid(row = 1, column = 1, padx = 3, pady = 2)

#****************************************************************************************************************************************************

#----------------------------------->              Search Frame         <-----------------------------------------

search_frame = tk.Frame(detail_frame, bd = 5, relief = tk.GROOVE)
search_frame.pack(side = tk.TOP, fill = tk.X)

#----------------------------------->              Search Lable         <-----------------------------------------

search_lable = tk.Label(search_frame, text = "Search", font = ("Arial", 14))
search_lable.grid(row = 0, column = 0, padx = 3, pady = 3)

#----------------------------------->              Search combo-Box     <-----------------------------------------

search_in = ttk.Combobox(search_frame, font = ("Arial", 14), state = "readonly", textvariable = search_by)
search_in['values'] = ("name", "rollno", "contact", "fathersname", "class_", "section", "dob", "address")
search_in.grid(row = 0, column = 1, padx = 5, pady = 2)

txt_search = tk.Entry(search_frame,bd = 3, font = ("Arial", 15),width = 5, textvariable = search_txt)
txt_search.grid(row = 0, column = 2, padx = 2, pady = 6)

#----------------------------------->              Search Button        <-----------------------------------------

search_btn = tk.Button(search_frame, text = "Search", font = ("Arial", 13), bd = 5, width = 12, command = search)
search_btn.grid(row = 0, column = 3, padx = 10, pady = 2)

#----------------------------------->              Display Button       <-----------------------------------------

display_btn = tk.Button(search_frame, text = "Display", font = ("Arial", 13), bd = 5, width = 12, command = fetch_data)
display_btn.grid(row = 0, column = 4, padx = 10, pady = 2)

#****************************************************************************************************************************************************

#************************************         Frame To View The Student Data     ********************************************************************

data_frame = tk.Frame(detail_frame, bd = 8, relief = tk.GROOVE)
data_frame.pack(fill = tk.BOTH, expand = True)

#************************************               Frame Scroll-Bars     ***************************************************************************

y_scroll = tk.Scrollbar(detail_frame, orient = tk.VERTICAL)
x_scroll = tk.Scrollbar(detail_frame, orient = tk.HORIZONTAL)

'''name, rollno , Section, class_, fathersname, Gender, dob, contact, address'''

#************************************               TreeView - Headings    ***************************************************************************

stud_table = ttk.Treeview(data_frame, columns = ("Name", "Roll No.", "Section", "Class", "Father's Name", "Gender", "D.O.B", "Contact", "Address"), yscrollcommand = y_scroll.set, xscrollcommand = x_scroll.set )

y_scroll.config(command = stud_table.yview)
x_scroll.config(command = stud_table.xview)

y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

stud_table.heading("Name", text = "Name")
stud_table.heading("Roll No.", text = "Roll No.")
stud_table.heading("Section", text = "Section")
stud_table.heading("Class", text = "Class")
stud_table.heading("Father's Name", text = "Father's Name")
stud_table.heading("Gender", text = "Gender")
stud_table.heading("D.O.B", text = "D.O.B")
stud_table.heading("Contact", text = "Contact")
stud_table.heading("Address", text = "Address")

stud_table['show'] = 'headings'

stud_table.column("Name", width = 100)
stud_table.column("Roll No.", width = 100)
stud_table.column("Section", width = 100)
stud_table.column("Class", width = 100)
stud_table.column("Father's Name", width = 150)
stud_table.column("Gender", width = 100)
stud_table.column("D.O.B", width = 100)
stud_table.column("Contact", width = 100)
stud_table.column("Address", width = 150)

stud_table.pack(fill = tk.BOTH, expand = True)

fetch_data()

stud_table.bind("<ButtonRelease-1>", get_cursor)


win.mainloop()