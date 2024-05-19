import pandas as pd
import time
import sys
#import asyncio
import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",password="Root1234",database="railway")
global s
if conn.is_connected():
 print()
 print("____________________________________________________________________________________________________")
 
 print("              <------------------------WELCOME TO FAST RAILLINE----------------------->")
 print("____________________________________________________________________________________________________")
 print()
passwd=input("Enter strong password:")
if len(passwd)>=8 :
 try:
     print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _logged in successfully _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
 except:
     print("_ _ _ _ _ _ _ _ _ _ _ _ _ _Enter strong password(must be 8 characters)__ _ _ _ _ _ _ _ _ _ _ _")
def make_it_flash(text):
 for i in reversed(range(36)):
     sys.stdout.write('\r')
     sys.stdout.write(text if i % 2 else ' '*len(text))
     sys.stdout.flush()
     time.sleep(0.5) 
def menu():
 print()
 print()
 print("1. Create table Passenger")
 print("2. Add new passenger detail ")
 print("3. Create table traindetail")
 print("4. Add new in train detail")
 print("5. Show all from train detail")
 print("6. show all from passenger table") 
 print("7. Show pnr no")
 print("8. Reservation of ticket")
 print("9. cancellation of reservation")
menu()
def create_passenger():
 c1=conn.cursor()
 c1.execute("create table if not exists passengers(pname varchar(30),age varchar(25),trainno varchar(30),no_of_pass varchar(25),cls varchar (25),destination varchar(30),amount int(20),status varchar(25),pnr_no varchar(25))")
 print(" passengers table created--------------")
def add_passengers():
 c1=conn.cursor()
 L=[]
 pname=input("Enter Name:")
 L.append(pname)
 age=input("Enter Age:")
 L.append(age)
 trainno=input("Enter Train no:")
 L.append(trainno)
 no_of_pass=input("Enter no of passengers:")
 L.append(no_of_pass)
 cls=input("Enter CLASS:")
 L.append(cls)
 Destination=input("Enter Destination:")
 L.append(Destination)
 amount=int(input("Enter Fare:"))
 L.append(amount)
 status=input("Enter Status:")
 L.append(status)
 pnr_no=input("Enter pnrno:")
 L.append(pnr_no)
 pas=(L)
 sql="insert into passengers(pname,age,trainno,no_of_pass,cls,destination,amount,status,pnr_no)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
 c1.execute(sql,pas)
 conn.commit()
 print("Record of passengers inserted successfully")
 df=pd.read_sql("select*from passengers",conn)
 print(df)
def create_traindetail():
 c1=conn.cursor()
 c1.execute("create table if not exists train_details(t_name varchar(30),t_num varchar (25),source varchar(30),destination varchar(30),fare varchar(10),Ac1 varchar(25),Ac2 varchar(30),sleeper varchar(25))")
 print("Table of Traindetail created")
def add_traindetail():
 c1=conn.cursor()
 df=pd.read_sql("select *from train_details",conn)
 print(df)
 L=[]
 t_name=input("Enter train name:")
 L.append(t_name)
 t_num=input("Enter train number:")
 L.append(t_num)
 source=input("Enter source of train:")
 L.append(source)
 destination=input("Enter destination of train:")
 L.append(destination)
 fare=input("Enter fare of station:")
 L.append(fare)
 Ac1=input("Enter no of seats for Ac1")
 L.append(Ac1)
 Ac2=input("Enter no ot seats for Ac2")
 L.append(Ac2)
 sleeper=input("Enter no of seats for sleeper:")
 L.append(sleeper)
 f=(L)
 sql=" insert into train_details(t_name ,t_num ,source ,destination ,fare ,Ac1 ,Ac2 ,sleeper) values(%s,%s,%s,%s,%s,%s,%s,%s)"
 c1.execute(sql,f)
 conn.commit()
 print("Record inserted in traindeatail-------------------")
def showtrain_details():
 print("All trains detail")
 df=pd.read_sql("select *from train_details",conn)
 print(df)
def showpassengers():
 print("All passengers detail")
 df=pd.read_sql("select* from passengers",conn)
 print(df)
def disp_pnrno():
 print("pnr status window-----------------------")
 a=(input("Enter Train no:"))
 qry="select pname,status from passengers where trainno =%s;"%(a,)
 df=pd.read_sql(qry,conn)
 print(df)
def ticketreservation():
 global s
 print("WE HAVE THE FOLLOWING SEAT TYPES FOR YOU")
 print("TNAME IN 1 FOR GOA EXPRESS FROM DELHI : TNAME IN 3 FOR CHENNAI EXPRESS FROM DELHI :")
 print()
 print("- - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
 print("1.FIRST class AC Rs 600o per person 1.FIRST class AC Rs 600o per person")
 print("2.SECOND class AC Rs 5000 per person 2.SECOND class AC Rs 5000 per person")
 print("3.THIRD class AC Rs 400o per person 3.THIRD class AC Rs 400o per person")
 print("4.for SLEEPERclass AC Rs 300o per person 4.for SLEEPERclass AC Rs 300o per person")
 print("- - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
 print("Tname is 2 for JAMMU EXPRESS from NEW DELHI:- Tname is 4 for MUMBAI from NEW DELHI:")
 print("- - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
 print("1.FIRST class AC Rs 1000o per person 1.FIRST class AC Rs 1000o per person")
 print("2.SECOND class AC Rs 900o per person 2.SECOND class AC Rs 900o per person")
 print("3.THIRD class AC Rs 800o per personn 3.THIRD class AC Rs 800o per person")
 print("4.for SLEEPER class AC Rs 700o per person 4.for SLEEPER class AC Rs 700o per person")
 tname=input("Enter your choice of Train name: ")
 print(tname)
 x=input("Enter your choice of ticket:")
 n=int(input("How many tickets you need:"))
 if(x==1):
     print("you have chosen first class AC ticket")
     s=6000*n
 elif (x==2):
     print("you have chosen second class AC ticket")
     s=5000*n
 elif (x==3):
     print("you have chosen third class AC ticket")
     s=4000*n
 elif (x==4):
     print("you have chosen sleeper ticket")
     s=3000*n
 else:
     print("invalid option")
     print("please choose a train")
     print("your total ticket price is =",2000*n,"\n")
def cancel():
    print("before any changes in the status")
    df=pd.read_sql("select *from passengers",conn)
    print(df)
    mc=conn.cursor()
    a=input("Enter pnr no:")
    mc.execute("update passengers set status='cancelled' where pnr_no=%s;"%(a,))
 #conn.commit()
    df=pd.read_sql("select* from passengers",conn)
    print(df) 
opt=""
opt=int(input(" Enter yor choice:"))
if opt==1:
 create_passenger()
elif opt==2:
 add_passengers()
elif opt==3:
 create_traindetail()
elif opt==4:
 add_traindetail()
elif opt==5:
 showtrain_details()
elif opt==6:
 showpassengers()
elif opt==7:
 disp_pnrno()
elif opt==8:
 ticketreservation()
 print("-------------------------------------------Loading------------------------------------------------------")
 make_it_flash(".")
 print("***********************YOUR TICKET IS CONFIRMED*********************")
elif opt==9:
 cancel()
else:
 print("SERVER DOWN---------------------------------------------") 
