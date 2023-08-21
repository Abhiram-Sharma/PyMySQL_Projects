# import neseccary libraries
import pymysql # for connecting python with mysql
import matplotlib.pyplot as plt # for plotting graph
from password import pwd as pwd # fetch password for connecting to mysql
import numpy as np
# connect to mysql


link=pymysql.connect(host="localhost",user="root",password=pwd)
a=link.cursor()


try: # try to create database
    a.execute("create database Stationery_Shop_management_system")
    a.execute("use Stationery_Shop_management_system")
    a.execute("create table inventory (id int primary key, cname varchar(50), bname varchar(20), qty int, price int)")
    a.execute("create table sales (saleid int primary key, scname varchar(50), sbname varchar(20), qty int, amt int)")
except: # if database aleardy exists
    a.execute("use Stationery_Shop_management_system")

while True: # repeat task
    print("Welcome To Stationery Shop Management System")
    print("--------------------------------------------------")
    print("CHOOSE ONE OF THE BELLOW TASKS TO PERFORM ")
    print("1. Add Stationery")
    print("2. Search Stationery")
    print("3. Edit Stationery")
    print("4. Delete Stationery")
    print("5. Billing")
    print("6. Analysis")
    print("7. Exit")
    task=int(input("ENTER A TASK NUMBER: "))

    if task==1: # Add New Stationery
        print("Enter details of the Stationery")
        cid = int(input("Enter Stationery id: "))
        typec=str(input("Stationery Name : "))
        brand = input("Enter brand of the Stationery : ")
        qty = int(input("Enter quantity of Stationery : "))
        price = int(input("Enter price of the Stationery: "))
        addv = 'insert into inventory values('+str(cid)+",'"+typec+"','"+str(brand)+"',"+str(qty)+','+str(price)+')'
        a.execute(addv)
        print('Successfully Inserted '+str(typec))

    if task==2: # Search for Stationery
        print("Enter details of the Stationery")
        cid = str(input("Enter Stationery id: "))
        searv="select * from inventory where id="+cid+";"
        a.execute(searv)
        result=a.fetchall()
        try:
            name=str(result[0][1])
            bname=str(result[0][2])
            qty=str(result[0][3])
            price=str(result[0][4])
            print("Details of Stationery with Id : "+cid)
            print("Name of the Stationery : "+name)
            print("Name of the Brand : "+bname)
            print("Quantity available : "+qty)
            print("Price : "+price)
        except:
            print("Invalid Search ID")

    if task==3: # Edit Stationery
        cid=str(input("Enter The Stationery Id : "))
        a.execute("select * from inventory where id="+cid+";")
        result=a.fetchall()
        try:
            name=str(result[0][1])
            bname=str(result[0][2])
            qty=str(result[0][3])
            price=str(result[0][4])
            print("Details of Stationery with Id : "+cid)
            print("Name of the Stationery : "+name)
            print("Name of the Brand : "+bname)
            print("Quantity available : "+qty)
            print("Price : "+price)
            
            typec=str(input("New Name of Stationery : "))
            brand = str(input("Enter New brand of the Stationery : "))
            qty = str(input("Enter New quantity of Stationery : "))
            price = str(input("Enter New price of the Stationery : "))
            confirm=(str(input("Confirm edit (Y/N) : ")))
            if confirm=="y":
                a.execute("update inventory set cname = '"+typec+"' where id="+cid)
                a.execute("update inventory set bname = '"+brand+"' where id="+cid)
                a.execute("update inventory set qty = "+qty+" where id="+cid)
                a.execute("update inventory set price = "+price+" where id="+cid)
                print("Updated Entry "+cid+" Successfully.")
        except:
            print("Invalid ID")

    if task==4: # Delete Stationery
        
        cid=str(input("Enter The Stationery Id : "))
        c=str(input("confirm delete (y"+"\\"+"n) : "))
        if c=="y":
            a.execute("delete from inventory where id="+cid+";")
            print("Stationery with Id Number "+cid+" deleted sucessfully")
        else:
            pass
      
    if task==5: # Billing of Stationery
        saleid=str(input("Enter Sale Id : "))
        cid=str(input("Enter Stationery Id : "))
        qty=int(input("Enter Stationery Quantity : "))
        a.execute("select qty from inventory where id="+cid+";")
        aqty=a.fetchone()
        try:
            if qty<=aqty[0]:
                a.execute("select * from inventory where id="+cid+";")# fetch details of each item
                details=a.fetchone()
                price=details[4]
                typec=details[1]
                brand=details[2]
                billamt=price*qty
                a.execute('insert into sales values('+str(saleid)+",'"+typec+"','"+str(brand)+"',"+str(qty)+','+str(billamt)+')')# add sale into database 
                nqty=aqty[0]-qty
                a.execute("update inventory set qty = "+str(nqty)+" where id="+cid)
                print("Bill Amount to be paid is "+str(billamt)+" , Sale Registered")
                print("Thank You for Shopping")
            else:
                print("Invalid Purchase")
        except:
            print("Invalid Purchase")

    if task==6: # Graphical Analysis
        xaxis=[]
        a.execute("select scname from sales")
        result=a.fetchall()
        for i in result:
           for j in i:
              xaxis.append(j)
        values=[]
        a.execute("select qty from sales")
        resultv=a.fetchall()
        for i in resultv:
           for j in i:
              values.append(j)
        x=np.arange(len(xaxis))
        plt.xticks(x,xaxis)
        plt.bar(xaxis,values,label='Stationery')
        plt.legend()
        plt.show()

    if task==7: # Close Program
        print("Thank You for using STATIONERY SHOP MANAGEMENT SYSTEM")
        print("--------------------------------------------------")
        break
    link.commit()

# THE END OF PROGRAM