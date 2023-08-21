# import neseccary libraries
import pymysql # for connecting python with mysql
import matplotlib.pyplot as plt # for plotting graph
from password import pwd as pwd # fetch password for connecting to mysql
import numpy as np

# connect to mysql
link=pymysql.connect(host="localhost",user="root",password=pwd)
a=link.cursor()

try: # try to create database
    a.execute("create database BMS")
    a.execute("use BMS")
    a.execute("create table accounts (accno int primary key, name varchar(50), phno varchar(20), balnc int)")
    a.execute("create table transactions (id int primary key, accno int, Ttype varchar(20), amt int,date date)")
except: # if database aleardy exists
    a.execute("use BMS")

while True: # repeat task
    print("WELCOME TO BANK MANAGEMENT SYSTEM")
    print("--------------------------------------------------")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Edit Account Details")
    print("4. Delete Account")
    print("5. Deposit or Withdraw")
    print("6. Analyse Transactions")
    print("7. Close")
    task=int(input("ENTER A TASK NUMBER : "))
    if task==1: # create account
        print("Enter Details of Account Holder")
        accno = int(input("Enter Account Number : "))
        name=str(input("Enter Name : "))
        phno = str(input("Enter Phone Number : "))
        balnc = int(input("Enter Initial Balance : "))
        addv = 'insert into accounts values('+str(accno)+",'"+name+"','"+str(phno)+"',"+str(balnc)+')'
        a.execute(addv)
        print('Successfully Created Account with Account Number '+str(accno))
    if task==2: # check balance
        print("Enter Account Details")
        accno = str(input("Enter Account Number : "))
        searv="select * from accounts where accno="+accno+";"
        a.execute(searv)
        result=a.fetchall()
        try:
            name=str(result[0][1])
            phno=str(result[0][2])
            balnc=str(result[0][3])
            print("Details of Account with Account Number : "+accno)
            print("Name of the Account Holder : "+name)
            print("Phone Number of Account Holder : "+phno)
            print("Account Balance : "+balnc)
        except:
            print("Invalid Search ID")
    if task==3: # Edit Account Details
        print("Enter Account Details")
        accno = str(input("Enter Account Number : "))
        searv="select * from accounts where accno="+accno+";"
        a.execute(searv)
        result=a.fetchall()
        try:
            name=str(result[0][1])
            phno=str(result[0][2])
            balnc=str(result[0][3])
            print("Details of Account with Account Number : "+accno)
            print("Name of the Account Holder : "+name)
            print("Phone Number of Account Holder : "+phno)
            print("Account Balance : "+balnc)
            nname=str(input("Enter New Name : "))
            nphno = str(input("Enter New Phone Number : "))
            nbalnc = int(input("Enter New Initial Balance : "))
            confirm=(str(input("Confirm edit (Y/N) : ")))
            if confirm=="y":
                a.execute("update accounts set name = '"+nname+"' where accno="+accno)
                a.execute("update accounts set phno = '"+nphno+"' where accno="+accno)
                a.execute("update accounts set balnc = "+nbalnc+" where accno="+accno)
                print("Updated Account "+accno+" Successfully.")
        except:
            print("Invalid Search ID")
          
    if task==4: # Delete Account
        
        accno=str(input("Enter The Account Number : "))
        c=str(input("confirm delete (y"+"\\"+"n) : "))
        if c=="y":
            a.execute("delete from accounts where accno="+accno+";")
            print("Account with Account Number "+accno+" deleted sucessfully")
        else:
            pass
      
    if task==5: # Deposit / Withdraw
        transid=str(input("Enter Transaction Id : "))
        accno=str(input("Enter Account Number : "))
        date=str(input("Enter Transaction Date (YYYY-MM-DD) : "))
        Ttype=str(input("Deposit / Withdraw : "))
        amt=str(input("Enter Amount for Transaction : "))
        try:
            accounts=[]
            a.execute("select accno from accounts")
            result=a.fetchall()
            for i in result:
                for j in i:
                    accounts.append(j)
            if accno in accounts:
                a.execute("insert into transactions values("+transid+","+accno+",'"+Ttype+"',"+amt+",'"+date+"')")
                searv="select * from accounts where accno="+accno+";"
                a.execute(searv)
                result=a.fetchall()
                balnc=str(result[0][3])
                if Ttype.lower()=="deposit":    
                    nbalnc=balnc+amt
                    a.execute("update accounts set balnc = "+nbalnc+" where accno="+accno)
                    print("Deposit of Amount "+amt+" from Account Number "+accno+" is Successful")
                elif amt<=balnc:
                    nbalnc=balnc-amt
                    a.execute("update accounts set balnc = "+nbalnc+" where accno="+accno)
                    print("Withdrawal of Amount "+amt+" from Account Number "+accno+" is Successful")
                else:
                    print("Invalid Transaction")
                
            else:
                print("Invalid Purchase")
        except:
            print("Invalid Purchase")
    if task==6: # Analyse Transactions
        xaxis=[]
        a.execute("select date from transactions")
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
        plt.bar(x,xaxis,values,label='Deposit')
        plt.bar(x+0.2,xaxis,values,label='Withdrawal')
        plt.legend()
        plt.show()
    if task==7:
        print("Thank You for using BANK MANAGEMENT SYSTEM")
        print("--------------------------------------------------")
        break
    link.commit()
# THE END OF PROGRAM