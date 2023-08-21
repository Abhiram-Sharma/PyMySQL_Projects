# import libraries
import pymysql # for connecting python with mysql
import matplotlib.pyplot as plt # for plotting graph
from password import pwd as pwd # fetch password for connecting to mysql
import numpy as np

# connect to mysql
link=pymysql.connect(host="localhost",user="root",password=pwd)
a=link.cursor()

try: # try to create database
    a.execute("create database Zoo_management_system")
    a.execute("use Zoo_management_system")
    a.execute("create table inventory (id int primary key, name varchar(50), breed varchar(20), qty int)")
except: # if database aleardy exists
    a.execute("use Zoo_management_system")

while True: # repeat tasks
    print("WELCOME TO ZOO MANAGEMENT SYSTEM")
    print("CHOOSE ONE OF THE BELLOW TASKS TO PERFORM ")
    print("1. Add Animal")
    print("2. Search Animal")
    print("3. Edit Animal")
    print("4. Delete Animal")
    print("5. Animal Quantity Analysis")
    print("6. Exit")
    task=int(input("ENTER A TASK NUMBER: "))
    if task==1:
        print("Enter details of the Animal")
        id = int(input("Enter Animal id: "))
        name=str(input("Animal Name : "))
        breed = str(input("breed of Animal : "))
        qty = int(input("Enter Quantity of Animal : "))
        insertvalue = 'insert into inventory values('+str(id)+",'"+name+"','"+str(breed)+"',"+str(qty)+')'
        a.execute(insertvalue)
        print('Successfully Inserted '+str(name))
    if task==2:
        print("Enter details of the Animal")
        id = str(input("Enter Animal id: "))
        search="select * from inventory where id="+id+";"
        a.execute(search)
        result=a.fetchall()
        try:
            name=str(result[0][1])
            breed=str(result[0][2])
            qty=str(result[0][3])
            print("Details of Animal with Id : "+id)
            print("Name of the Animal : "+name)
            print("breed of the Animal : "+breed)
            print("Quantity available : "+qty)
        except:
            print("Invalid Search ID")
    if task==3:
        id=str(input("Enter The Animal Id : "))
        a.execute("select * from inventory where id="+id+";")
        result=a.fetchall()
        name=str(result[0][1])
        bname=str(result[0][2])
        qty=str(result[0][3])
        print("Details of Animal with Id : "+id)
        print("Name of the Animal : "+name)
        print("breed of the Animal : "+bname)
        print("Quantity available : "+qty)
        
        namen=str(input("New Name of Animal : "))
        breedn = str(input("Enter New breed Name of the Animal: "))
        qtyn = str(input("Enter New Quantity of Animal: "))
        confirm=(str(input("Confirm edit (Y/N) : ")))
        if confirm=="y":
           a.execute("update inventory set name = '"+namen+"' where id="+id)
           a.execute("update inventory set breed = '"+breedn+"' where id="+id)
           a.execute("update inventory set qty = "+qtyn+" where id="+id)
           print("Updated Entry "+id+" Successfully.")
    if task==4:
        
        id=str(input("Enter The Animal Id : "))
        c=str(input("confirm delete (y"+"\\"+"n) : "))
        if c=="y":
            a.execute("delete from inventory where id="+id+";")
            print("Animal with Id Number "+id+" deleted sucessfully")
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
        plt.bar(xaxis,values,label='Animal')
        plt.legend()
        plt.show()
    if task==6:
        print("Thank You for using ZOO MANAGEMENT SYSTEM")
        print("--------------------------------------------------")
        break
    print("--------------------------------------------------")
    link.commit()
# THE END OF PROGRAM
