# import libraries
import pymysql # connect python with mysql
import matplotlib.pyplot as plt # plotting graph
from credentials import password as pwd # password for connecting to mysql
import numpy as np

# connect to mysql
link=pymysql.connect(host="localhost",user="root",password=pwd)
a=link.cursor()

try: # try to create database
    a.execute("create database GroceryStore_management_system")
    a.execute("use GroceryStore_management_system")
    a.execute("create table inventory (id int primary key, gname varchar(50), qty int, price int)")
    a.execute("create table sales (saleid int primary key, sgname varchar(50), qty int, amt int)")
except: # if database aleardy exists
    a.execute("use GroceryStore_management_system")

while True: # repeat task
    print("WELCOME TO GROCERY STORE MANAGEMENT SYSTEM")
    print("--------------------------------------------------")
    print("CHOOSE ONE OF THE BELLOW TASKS TO PERFORM :")
    print("1. Add Grocery to Inventory")
    print("2. Search Grocery from Inventory")
    print("3. Edit Grocery Details")
    print("4. Delete Groceries")
    print("5. Sale of Groceries")
    print("6. Sale Analysis")
    print("7. Quit")

    task=int(input("ENTER A TASK : "))

    if task==1:
        print("Enter details of the Grocery")
        gid = int(input("Enter Grocery id: "))
        gname=str(input("Type of Grocery : "))
        qty = int(input("Enter quantity of Grocery: "))
        price = int(input("Enter price of the Grocery: "))
        addv = 'insert into inventory values('+str(gid)+",'"+gname+"',"+str(qty)+','+str(price)+')'
        a.execute(addv)
        print('Successfully Inserted '+str(gname))
    
    if task==2:
        print("Enter details of the Grocery")
        gid = str(input("Enter Grocery id: "))
        searv="select * from inventory where id="+gid+";"
        a.execute(searv)
        result=a.fetchall()
        try:
            name=str(result[0][1])
            qty=str(result[0][2])
            price=str(result[0][3])
            print("Details of Grocery with Id : "+gid)
            print("Name of the Grocery : "+name)
            print("Quantity available : "+qty)
            print("Price : "+price)
        except:
            print("Invalid Search ID")
    
    if task==3:
        gid=str(input("Enter The Grocery Id : "))
        a.execute("select * from inventory where id="+gid+";")
        result=a.fetchall()
        name=str(result[0][1])
        qty=str(result[0][2])
        price=str(result[0][3])
        print("Details of Grocery with Id : "+gid)
        print("Name of the Grocery : "+name)
        print("Quantity available : "+qty)
        print("Price : "+price)
          
        gname=str(input("New Type of Grocery : "))
        qty = str(input("Enter New quantity of Grocery: "))
        price = str(input("Enter New price of the Grocery: "))
        confirm=(str(input("Confirm edit (Y/N) : ")))
        if confirm=="y":
           a.execute("update inventory set gname = '"+gname+"' where id="+gid)
           a.execute("update inventory set qty = "+qty+" where id="+gid)
           a.execute("update inventory set price = "+price+" where id="+gid)
           print("Updated Entry "+gid+" Successfully.")
    if task==4:
        
        gid=str(input("Enter The Grocery Id : "))
        c=str(input("confirm delete (y"+"\\"+"n) : "))
        if c=="y":
            a.execute("delete from inventory where id="+gid+";")
            print("Grocery with Id Number "+gid+" deleted sucessfully")
        else:
            pass
      
    if task==5:
        saleid=str(input("Enter Sale Id : "))
        gid=str(input("Enter Grocery Id : "))
        qty=int(input("Enter Grocery Quantity : "))
        a.execute("select qty from inventory where id="+gid+";")
        aqty=a.fetchone()
        try:
            if qty<=aqty[0]:
                a.execute("select * from inventory where id="+gid+";")# fetch details of each item
                details=a.fetchone()
                price=details[3]
                gname=details[1]
                billamt=price*qty
                a.execute('insert into sales values('+str(saleid)+",'"+gname+"',"+str(qty)+','+str(billamt)+')')# add sale into database 
                nqty=aqty[0]-qty
                a.execute("update inventory set qty = "+str(nqty)+" where id="+gid)
                print("Total Bill Amount to be paid is "+str(billamt))
                print("Thank You for Shopping")
            else:
                print("Invalid Purchase")
        except:
            print("Invalid Purchase")
    if task==6:
        xaxis=[]
        a.execute("select sgname from sales")
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
        plt.bar(xaxis,values,label='Groceries')
        plt.legend()
        plt.show()
    if task==7:
        print("Thank You for using GROCERY STORE MANAGEMENT SYSTEM")
        print("--------------------------------------------------")
        break
    link.commit()
# THE END OF PROGRAM
