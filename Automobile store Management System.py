# import neseccary libraries
import pymysql # for connecting python with mysql
import matplotlib.pyplot as plt # for plotting graph
from credentials import pwd as pwd # fetch password for connecting to mysql
import numpy as np

# connect to mysql
link=pymysql.connect(host="localhost",user="root",password=pwd)
a=link.cursor()


try: # try to create database
    a.execute("create database Automobile_management_system")
    a.execute("use Automobile_management_system")
    a.execute("create table inventory (id int primary key, cname varchar(50), brand varchar(20), qty int, price int)")
    a.execute("create table sales (saleid int primary key, scname varchar(50), sbrand varchar(20), qty int, amt int)")
except: # if database aleardy exists
    a.execute("use Automobile_management_system")

while True: # repeat task
    print("WELCOME TO AUTOMOBILE STORE MANAGEMENT SYSTEM")
    print("--------------------------------------------------")
    print("CHOOSE ONE OF THE BELOW TASKS TO PERFORM ")
    print("1. Add Automobile")
    print("2. Search Automobile")
    print("3. Edit Automobile")
    print("4. Delete Automobile")
    print("5. Sale")
    print("6. Sale Analysis")
    print("7. Quit")
    task=int(input("ENTER A TASK NUMBER: "))
    if task==1:
        print("Enter details of the Automobile")
        cid = int(input("Enter Automobile id: "))
        cname=str(input("Automobile Name : "))
        brand = input("Enter Brand of Automobile : ")
        qty = int(input("Enter Quantity of Automobile : "))
        price = int(input("Enter Price of Automobile: "))
        addv = 'insert into inventory values('+str(cid)+",'"+cname+"','"+str(brand)+"',"+str(qty)+','+str(price)+')'
        a.execute(addv)
        print('Successfully Inserted '+str(cname))
    if task==2:
        print("Enter details of Automobile")
        cid = str(input("Enter Automobile id: "))
        searv="select * from inventory where id="+cid+";"
        a.execute(searv)
        result=a.fetchall()
        try:
            name=str(result[0][1])
            brand=str(result[0][2])
            qty=str(result[0][3])
            price=str(result[0][4])
            print("Details of Automobile with Id : "+cid)
            print("Name of the Automobile : "+name)
            print("Name of the Brand : "+brand)
            print("Quantity Available : "+qty)
            print("Price : "+price)
        except:
            print("Invalid Search ID")
    if task==3:
        cid=str(input("Enter The Automobile Id : "))
        a.execute("select * from inventory where id="+cid+";")
        result=a.fetchall()
        name=str(result[0][1])
        brand=str(result[0][2])
        qty=str(result[0][3])
        price=str(result[0][4])
        print("Details of Automobile with Id : "+cid)
        print("Name of the Automobile : "+name)
        print("Name of the Brand : "+brand)
        print("Quantity Available : "+qty)
        print("Price : "+price)
          
        cname=str(input("New Type of Automobile : "))
        brand = str(input("Enter New Brand of the Automobile: "))
        qty = str(input("Enter New Quantity of Automobile: "))
        price = str(input("Enter New Price of the Automobile: "))
        confirm=(str(input("Confirm edit (Y/N) : ")))
        if confirm=="y":
           a.execute("update inventory set cname = '"+cname+"' where id="+cid)
           a.execute("update inventory set brand = '"+brand+"' where id="+cid)
           a.execute("update inventory set qty = "+qty+" where id="+cid)
           a.execute("update inventory set price = "+price+" where id="+cid)
           print("Updated Entry "+cid+" Successfully.")
    if task==4:
        
        cid=str(input("Enter The Automobile Id : "))
        c=str(input("confirm delete (y"+"\\"+"n) : "))
        if c=="y":
            a.execute("delete from inventory where id="+cid+";")
            print("Automobile with Id Number "+cid+" deleted sucessfully")
        else:
            pass
      
    if task==5:
        saleid=str(input("Enter Sale Id : "))
        cid=str(input("Enter Automobile Id : "))
        qty=int(input("Enter Automobile Quantity : "))
        a.execute("select qty from inventory where id="+cid+";")
        aqty=a.fetchone()
        try:
            if qty<=aqty[0]:
                a.execute("select * from inventory where id="+cid+";")# fetch details of each item
                details=a.fetchone()
                price=details[4]
                cname=details[1]
                brand=details[2]
                billamt=price*qty
                a.execute('insert into sales values('+str(saleid)+",'"+cname+"','"+str(brand)+"',"+str(qty)+','+str(billamt)+')')# add sale into database 
                nqty=aqty[0]-qty
                a.execute("update inventory set qty = "+str(nqty)+" where id="+cid)
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
        plt.bar(xaxis,values,label='Automobiles')
        plt.legend()
        plt.show()
    if task==7:
        print("Thank You for using AUTOMOBILE STORE MANAGEMENT SYSTEM")
        print("--------------------------------------------------")
        break
    link.commit()
# THE END OF PROGRAM