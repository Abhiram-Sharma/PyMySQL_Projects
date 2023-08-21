# import neseccary libraries
import pymysql # for connecting python with mysql
import matplotlib.pyplot as plt # for plotting graph
from password import pwd as pwd # fetch password for connecting to mysql
import numpy as np

# connect to mysql
link=pymysql.connect(host="localhost",user="root",password=pwd)
a=link.cursor()


try: # try to create database
    a.execute("create database Electronics_management_system")
    a.execute("use Electronics_management_system")
    a.execute("create table inventory (id int primary key, cname varchar(50), brand varchar(20), qty int, price int)")
    a.execute("create table sales (saleid int primary key, scname varchar(50), sbrand varchar(20), qty int, amt int)")
except: # if database aleardy exists
    a.execute("use Electronics_management_system")

while True: # repeat task
    print("WELCOME TO Electronics STORE MANAGEMENT SYSTEM")
    print("--------------------------------------------------")
    print("CHOOSE ONE OF THE BELOW TASKS TO PERFORM ")
    print("1. Add Electronics")
    print("2. Search Electronics")
    print("3. Edit Electronics")
    print("4. Delete Electronics")
    print("5. Sale")
    print("6. Sale Analysis")
    print("7. Quit")
    task=int(input("ENTER A TASK NUMBER: "))
    if task==1:
        print("Enter details of the Electronics")
        eid = int(input("Enter Electronics id: "))
        cname=str(input("Electronics Name : "))
        brand = input("Enter Brand of Electronics : ")
        qty = int(input("Enter Quantity of Electronics : "))
        price = int(input("Enter Price of Electronics: "))
        addv = 'insert into inventory values('+str(eid)+",'"+cname+"','"+str(brand)+"',"+str(qty)+','+str(price)+')'
        a.execute(addv)
        print('Successfully Inserted '+str(cname))
    if task==2:
        print("Enter details of Electronics")
        eid = str(input("Enter Electronics id: "))
        searv="select * from inventory where id="+eid+";"
        a.execute(searv)
        result=a.fetchall()
        try:
            name=str(result[0][1])
            brand=str(result[0][2])
            qty=str(result[0][3])
            price=str(result[0][4])
            print("Details of Electronics with Id : "+eid)
            print("Name of the Electronics : "+name)
            print("Name of the Brand : "+brand)
            print("Quantity Available : "+qty)
            print("Price : "+price)
        except:
            print("Invalid Search ID")
    if task==3:
        eid=str(input("Enter The Electronics Id : "))
        a.execute("select * from inventory where id="+eid+";")
        result=a.fetchall()
        name=str(result[0][1])
        brand=str(result[0][2])
        qty=str(result[0][3])
        price=str(result[0][4])
        print("Details of Electronics with Id : "+eid)
        print("Name of the Electronics : "+name)
        print("Name of the Brand : "+brand)
        print("Quantity Available : "+qty)
        print("Price : "+price)
          
        cname=str(input("New Type of Electronics : "))
        brand = str(input("Enter New Brand of the Electronics: "))
        qty = str(input("Enter New Quantity of Electronics: "))
        price = str(input("Enter New Price of the Electronics: "))
        confirm=(str(input("Confirm edit (Y/N) : ")))
        if confirm=="y":
           a.execute("update inventory set cname = '"+cname+"' where id="+eid)
           a.execute("update inventory set brand = '"+brand+"' where id="+eid)
           a.execute("update inventory set qty = "+qty+" where id="+eid)
           a.execute("update inventory set price = "+price+" where id="+eid)
           print("Updated Entry "+eid+" Successfully.")
    if task==4:
        
        eid=str(input("Enter The Electronics Id : "))
        c=str(input("confirm delete (y"+"\\"+"n) : "))
        if c=="y":
            a.execute("delete from inventory where id="+eid+";")
            print("Electronics with Id Number "+eid+" deleted sucessfully")
        else:
            pass
      
    if task==5:
        saleid=str(input("Enter Sale Id : "))
        eid=str(input("Enter Electronics Id : "))
        qty=int(input("Enter Electronics Quantity : "))
        a.execute("select qty from inventory where id="+eid+";")
        aqty=a.fetchone()
        try:
            if qty<=aqty[0]:
                a.execute("select * from inventory where id="+eid+";")# fetch details of each item
                details=a.fetchone()
                price=details[4]
                cname=details[1]
                brand=details[2]
                billamt=price*qty
                a.execute('insert into sales values('+str(saleid)+",'"+cname+"','"+str(brand)+"',"+str(qty)+','+str(billamt)+')')# add sale into database 
                nqty=aqty[0]-qty
                a.execute("update inventory set qty = "+str(nqty)+" where id="+eid)
                print("Total Bill Amount to be paid is "+str(billamt)+"  ,Sale has been Registered")
                print("Thank You for Shopping")
            else:
                print("Invalid Purchase")
        except:
            print("Invalid Purchase")
    if task==6:
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
        plt.bar(xaxis,values,label='Electronicss')
        plt.legend()
        plt.show()
    if task==7:
        print("Thank You for using Electronics STORE MANAGEMENT SYSTEM")
        print("--------------------------------------------------")
        break
    link.commit()
# THE END OF PROGRAM