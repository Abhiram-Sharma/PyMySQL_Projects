# CBSE CLASS 12 IP PROJECT

# MADE BY: 
# Aditya Srivastava                                                                                    		
# Arjun Rijesh                                                                                       	
# Yashitha L Rao                                                                                     

# import libraries
import pymysql # for connecting python with mysql
import matplotlib.pyplot as plt # for plotting graph
from password import pwd as pwd # fetch password for connecting to mysql
import numpy as np

# connect to mysql
link=pymysql.connect(host="localhost",user="root",password=pwd)
a=link.cursor()

try: # try to create database
    a.execute("create database Pharmacy_management_system")
    a.execute("use Pharmacy_management_system")
    a.execute("create table inventory (id int primary key, name varchar(50), brand varchar(20), qty int)")
except: # if database aleardy exists
    a.execute("use Pharmacy_management_system")

while True: # repeat tasks
    print("WELCOME TO PHARMACY MANAGEMENT SYSTEM")
    print("CHOOSE ONE OF THE BELLOW TASKS TO PERFORM ")
    print("1. Add Medicine")
    print("2. Search Medicine")
    print("3. Edit Medicine")
    print("4. Delete Medicine")
    print("5. Medicine Quantity Analysis")
    print("6. Exit")
    task=int(input("ENTER A TASK NUMBER: "))
    if task==1:
        print("Enter details of the Medicine")
        id = int(input("Enter Medicine id: "))
        name=str(input("Medicine Name : "))
        brand = str(input("Brand of Medicine : "))
        qty = int(input("Enter Quantity of Medicine : "))
        insertvalue = 'insert into inventory values('+str(id)+",'"+name+"','"+str(brand)+"',"+str(qty)+')'
        a.execute(insertvalue)
        print('Successfully Inserted '+str(name))
    if task==2:
        print("Enter details of the Medicine")
        id = str(input("Enter Medicine id: "))
        search="select * from inventory where id="+id+";"
        a.execute(search)
        result=a.fetchall()
        try:
            name=str(result[0][1])
            brand=str(result[0][2])
            qty=str(result[0][3])
            print("Details of Medicine with Id : "+id)
            print("Name of the Medicine : "+name)
            print("Brand of the Medicine : "+brand)
            print("Quantity available : "+qty)
        except:
            print("Invalid Search ID")
    if task==3:
        id=str(input("Enter The Cloth Id : "))
        a.execute("select * from inventory where id="+id+";")
        result=a.fetchall()
        name=str(result[0][1])
        bname=str(result[0][2])
        qty=str(result[0][3])
        print("Details of Medicine with Id : "+id)
        print("Name of the Medicine : "+name)
        print("Brand of the Medicine : "+bname)
        print("Quantity available : "+qty)
        
        namen=str(input("New Name of Medicine : "))
        brandn = str(input("Enter New Brand Name of the Medicine: "))
        qtyn = str(input("Enter New Quantity of Medicine: "))
        confirm=(str(input("Confirm edit (Y/N) : ")))
        if confirm=="y":
           a.execute("update inventory set name = '"+namen+"' where id="+id)
           a.execute("update inventory set brand = '"+brandn+"' where id="+id)
           a.execute("update inventory set qty = "+qtyn+" where id="+id)
           print("Updated Entry "+id+" Successfully.")
    if task==4:
        
        id=str(input("Enter The Medicine Id : "))
        c=str(input("confirm delete (y"+"\\"+"n) : "))
        if c=="y":
            a.execute("delete from inventory where id="+id+";")
            print("Medicine with Id Number "+id+" deleted sucessfully")
        else:
            pass
    if task==5:
        xaxis=[]
        a.execute("select name from inventory")
        result=a.fetchall()
        for i in result:
           for j in i:
              xaxis.append(j)
        values=[]
        a.execute("select qty from inventory")
        resultv=a.fetchall()
        for i in resultv:
           for j in i:
              values.append(j)
        x=np.arange(len(xaxis))
        plt.xticks(x,xaxis)
        plt.bar(xaxis,values,label='Medicine')
        plt.legend()
        plt.show()
    if task==6:
        print("Thank You for using PHARMACY MANAGEMENT SYSTEM")
        print("--------------------------------------------------")
        break
    print("--------------------------------------------------")
    link.commit()
# THE END OF PROGRAM
