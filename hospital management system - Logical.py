import pymysql
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pwd import pwd as pwd

link=pymysql.connect(host="localhost",user="root",password=pwd)
a=link.cursor()
try:
   a.execute('create database hospital_management_system')
   a.execute ('use hospital_management_system')
   a.execute ('create table patient (id int primary key, name varchar (50), phno varchar (10), disease varchar (100))')
   a.execute ('create table doctor(id int primary key, name varchar (50), phno varchar (10),Tdisease varchar(100))')
   
except:
   a.execute ('use hospital_management_system')

def addvp(table_name ):
   idno=str(input("Enter ID of the patient : "))
   name=str(input("Enter name of the patient : "))
   phno=str(input("Enter phno of the patient : "))
   disease=str(input("Enter disease  of the patient : ")).lower()
   try:
      a.execute('insert into '+table_name+' values ('+idno+",'"+name+"','"+phno+"','"+disease+"')")
      print('Sucessfully added patient with ID '+idno)
   except:
      print('invalid id')
   return
def searchvp(table_name ):
   idno=str(input("Enter ID of the patient : "))
   a.execute("select * from "+ table_name+" where id="+idno)
   result =a.fetchone()
 
   if result==None:
      print('invalid ID')
      result=[" "," "," "," "]

   return result
def editvp(table_name ):
   idno=str(input("Enter ID of the patient : "))
   a.execute("select * from "+ table_name+" where id="+idno)
   result =a.fetchone()
   if result==None:
      print('invalid ID')
      result=[" "," "," "," "]
   name=str(result[1])
   phno=str(result[2])
   disease=str(result[3]).lower()
   print("Patient ID : "+idno)
   print("Patient Name : "+name)
   print("Patient Phone Number : "+phno)
   print("Patient's Disease : "+disease)
   name=str(input("Enter New name of the patient : "))
   phno=str(input("Enter New phno of the patient : "))
   disease=str(input("Enter New disease  of the patient : ")).lower()
   c=str(input("Confirm Update (y/n): "))
   if c=="y":
      a.execute("update "+table_name+" set name = '"+name+"' where id="+idno)
      a.execute("update "+table_name+" set phno = '"+phno+"' where id="+idno)
      a.execute("update "+table_name+" set disease = '"+disease+"' where id="+idno)
      print("Updated ID "+idno+" Successfully")
   else:
      print("ID "+idno+" has not been Updated")
   return
def deletevp(table_name ):
   idno=str(input("Enter ID of the patient : "))
   c=str(input('Confirm delete (y/n)  : '))
   if c=='y':
      a.execute("delete from "+table_name+" where id="+idno+";") 
      print('Patient with ID '+idno+' has been deleted sucessfully ')
   else:
      print('Patient with ID '+idno+' has not been deleted')
   return

def addvdo(table_name ):
   idno=str(input("Enter ID of the doctor : "))
   name=str(input("Enter name of the doctor : "))
   phno=str(input("Enter phno of the doctor : "))
   Tdisease=str(input("Enter Disease Treated by doctor : ")).lower()
   try:
      a.execute('insert into '+table_name+' values ('+idno+",'"+name+"','"+phno+"','"+Tdisease+"')")
      print('Sucessfully added doctor with ID '+idno)
   except:
      print('invalid id')
   return
def searchvdo(table_name ):
   idno=str(input("Enter ID of the doctor : "))
   a.execute("select * from "+ table_name+" where id="+idno)
   result =a.fetchone()
   if result==None:
      print('invalid ID')
      result=[" "," "," "," "]
   return result
def editvdo(table_name ):
   idno=str(input("Enter ID of the Doctor : "))
   a.execute("select * from "+ table_name+" where id="+idno)
   result =a.fetchone()
   if result==None:
      print('invalid ID')
      result=[" "," "," "," "]
   name=str(result[1])
   phno=str(result[2])
   Tdisease=str(result[3]).lower()
   print("Doctor ID : "+idno)
   print("Doctor Name : "+name)
   print("Doctor Phone Number : "+phno)
   print("Treating Disease : "+Tdisease)
   name=str(input("Enter New name of the Doctor : "))
   phno=str(input("Enter New phno of the Doctor : "))
   Tdisease=str(input("Enter New Disease treated by the Doctor : ")).lower()
   c=str(input("Confirm Update (y/n): "))
   if c=="y":
      a.execute("update "+table_name+" set name = '"+name+"' where id="+idno)
      a.execute("update "+table_name+" set phno = '"+phno+"' where id="+idno)
      a.execute("update "+table_name+" set Tdisease = '"+Tdisease+"' where id="+idno)
      print("Updated ID "+idno+" Successfully")
   else:
      print("ID "+idno+" has not been Updated")
   return
def deletevdo(table_name ):
   idno=str(input("Enter ID of the doctor : "))
   c=str(input('Confirm delete (y/n)  : '))
   if c=='y':
      a.execute("delete from "+table_name+" where id="+idno+";")
      print('Doctor with ID '+idno+' has been deleted sucessfully ')
   else:
      print('Doctor with ID '+idno+' has not been deleted')
   return

def patient_management():
   while True :
      print('---------------------------------------------------------------')
      print('1. Add new patient ')
      print('2. Search patient ')
      print('3. Edit patient ')
      print('4. Delete patient ')
      print('5. Show All Patients')
      print('6. Back to main menu ')
      op=int(input('Enter task number : '))
      if op==1:
         addvp('patient')
      if op==2:
         result=searchvp('patient')
         idno=str(result[0])
         name=str(result[1])
         phno=str(result[2])
         disease=str(result[3])
         print("Patient ID : "+idno)
         print("Patient Name : "+name)
         print("Patient Phone Number : "+phno)
         print("Patient's Disease : "+disease)
      if op==3:
         editvp('patient')
      if op==4:
         deletevp('patient')
      if op==5:
         # Show all Patients
         a.execute("select id from patient")
         m=a.fetchall()
         pid=[]
         for i in m:
            pid.append (i[0])

         a.execute("select name from patient")
         m=a.fetchall()
         pname=[]
         for i in m:
            pname.append (i[0])

         a.execute("select disease from patient")
         m=a.fetchall()
         pdis=[]
         for i in m:
            pdis.append (i[0])

         a.execute("select phno from patient")
         m=a.fetchall()
         pno=[]
         for i in m:
            pno.append (i[0])
         allpatients={"ID":pid,"Name":pname,"Phone Number":pno,"Disease":pdis}
         dfpatient=pd.DataFrame(allpatients)
         print(dfpatient)
         pass
      if op==6:
         print('Returing back to main menu \nThank you for using patient management system ')
         break
      else:
         pass
      link.commit()
   return   

def doctor_management():
   while True :
      print('---------------------------------------------------------------')
      print('1. Add new doctor ')
      print('2. Search doctor ')
      print('3. Edit doctor ')
      print('4. Delete doctor ')
      print("5. Show all Doctors")
      print('6. Doctors Analysis')
      print('7. Back to main menu ')
      od=int(input('Enter task number : '))
      if od==1:
         addvdo('doctor')
      if od==2:
         result=searchvdo('doctor')
         idno=str(result[0])
         name=str(result[1])
         phno=str(result[2])
         Tdisease=str(result[3]).lower()
         print("Doctor ID : "+idno)
         print("Doctor Name : "+name)
         print("Doctor Phone Number : "+phno)
         print("Treats Disease : "+Tdisease)
      if od==3:
         editvdo('doctor')
      if od==4:
         deletevdo('doctor')
      if od==5:
         a.execute("select id from doctor")
         m=a.fetchall()
         pid=[]
         for i in m:
            pid.append (i[0])

         a.execute("select name from doctor")
         m=a.fetchall()
         pname=[]
         for i in m:
            pname.append (i[0])

         a.execute("select Tdisease from doctor")
         m=a.fetchall()
         pdis=[]
         for i in m:
            pdis.append (i[0])

         a.execute("select phno from doctor")
         m=a.fetchall()
         pno=[]
         for i in m:
            pno.append (i[0])
            
         alldoctors={"ID":pid,"Name":pname,"Phone Number":pno,"Disease":pdis}
         dfdoctor=pd.DataFrame(alldoctors)
         print(dfdoctor)

      if od==6:
         # Doctors per disease
         xaxis=[]
         no=[]
         a.execute("select Tdisease from doctor")
         diseases=a.fetchall()
         for e in diseases:
            for f in e:
               xaxis.append(f)
         
         for i in xaxis:
            a.execute("select count(*)from doctor where Tdisease='"+str(i)+"'")
            result=a.fetchone()
            for j in result:  
               no.append(j)
        
         plt.bar(xaxis,no,label='doctors')
         plt.legend()
         plt.show()
         
      if od==7:
         print('Returing back to main menu \nThank you for using doctor management system ')
         break
      else:
         pass
      link.commit()
   return

def disease_management():
   while True :
      print('---------------------------------------------------------------')
      print('1. Disease Analysis')
      print('2. Back to main menu ')
      od=int(input('Enter task number : '))
      if od==1:
         # Patients per disease
         xaxis=[]
         no=[]
         a.execute("select disease from patient")
         diseases=a.fetchall()
         for e in diseases:
            for f in e:
               xaxis.append(f)
         
         for i in xaxis:
            a.execute("select count(*)from patient where disease='"+str(i)+"'")
            result=a.fetchone()
            for j in result:  
               no.append(j)
        
         plt.bar(xaxis,no,label='patients')
         plt.legend()
         plt.show()
         
      if od==2:
         print('Returing back to main menu \nThank you for using disease management system ')
         break
      else:
         pass
      link.commit()
   return

while True:
   print('---------------------------------------------------------------')
   print('Welcome to hospital management system ')
   print('---------------------------------------------------------------')
   print('1. Patient management ')
   print('2. Doctor management ')
   print('3. Disease management ')
   print('4. Close ')
   o=int(input('Enter selection :  '))
   if o==1:
      patient_management()
   if o==2:
      doctor_management()
   if o==3:
      disease_management()
   if o==4:
      print('Thank you for using hospital management system')
      link.commit()
      break
   else :
      pass
   link.commit()
