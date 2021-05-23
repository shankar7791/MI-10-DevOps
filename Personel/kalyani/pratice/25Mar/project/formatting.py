

import mysql.connector as mysql 
from openpyxl import workbook 
from openpyxl , styles import border ,side , color
from os import path
db= mysql.connect(host =" localhost",user =" root" , password=  ,database="excel")
command_handler=db.cursor(buffered=true)


def create_Excel():
    print("\n****Creating Excel File*****\n")
    workbook = workbook()
    sheet = workbook.actively
    file_name("Enter the file name you want create with xlsx extension:")
    workbook_save(filename = file_name)
    print("\nExcel file is created in current folder\n")
    

#print the sheet name in the file
print(format.sheetname)

#Create a sheet from summary results tab
sheetname = int(input(" Enter the name of the sheet :"))
sheet = format(sheetname)

# prints the value in A1 in order to verify sheet import
print (sheet('B2')value)
os.system(pause)
    

sheet.cell(row = 2 ,column =2).border (bottomside(border_style'thin',color =ff0000))
format.save('temp XLSXfile processed xlsx')
os.system(" pause")
