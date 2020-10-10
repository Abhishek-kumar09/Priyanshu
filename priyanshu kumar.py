import random
import mysql.connector

def selection():
    db=mysql.connector.connect(user='root',password='MYSQL',host='localhost',database='python')
    cursor=db.cursor()
    print("...............\tWELCOME TO RAILWAY MANAGEMENT SYSTEM\t....................")
    print("1.PASSENGER MANAGEMENT.")
    print("2.STAFF AND EMPLOYEE MANAGEMENT.")
    print("3.STATION MANAGEMENT.")
    print("4.TRAIN MANAGEMENT.")

choice=int(input("\nEnter your choice(1-4):-"))
if choice==1:
    print("\nWELCOME TO PASSENGER MANAGEMENT SYSTEM\n")
    print("a.NEW RESERVATION.")
    print("b.CANCEL RESERVATION.")
    print("c.UPDATE EXISTSING DETAILS")

    x=input("Enter your choice(a-c):-")
    print("\ninitially the details are:-")
    display1()
    if x=='a':
        insert1()
        print("\n Modified details are..")
        display1()
    elif x=='b':
        delete1()
        print("\nModified details are.")
        display1()
    elif x=='c':
        update1()
        print("\nModified details are.")
        display1()
    else:
        print("enter correct choice..!")
elif choice==2:
    print("\nWELCOME TO EMPLOYEE MANAGEMENT SYSTEM")
    print("d.NEW EMPLOYEE/STAFF.")
    print("e.UPDATE EMPLOYEE/STAFF DETAILS.")
    print("f.DELETE EMPLOYEE/STAFF")

    y=input("Enter your choice(d-f):-")
    print("\ninitially deatails are..")
    display2()
    if y=='d':
        insert1()
        print("\nModified details are..")
        display2()
    elif y=='e':
        update2()
        print("\nModified details are..")
        display2()
    elif y=='f':
        delete2()
        print("\nModified details are..")
        display2()
    else:
        print("Enter choice correctly!!")
elif choice==3:
    print("\nWELCOME TO STATION MANAGEMENT SYSTEM")
    print("g.UPDATE STATION PLATFORM")
    print("h.ADD NEW TRAINS TO THE STATION")
    print("i")
