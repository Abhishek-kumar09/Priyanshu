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

    z=input("Enter your choice(g-h):-")
    print("\nInitially details are..")
    display3()
    if z=='g':
        update2()
        print("\nModified details are..")
        display3()
    elif z=='h':
        insert3()
        print("\nModified details are..")
        display3()
    else:
        print("enter your choice correctly!!")
elif choice==4:
    print("\nWELCOME TO TRAIN MANAGEMNET SYSTEM")
    print("i.ADD NEW TRAINS TO THE STATION.")
    print("j.UPDATE EXISTING TRAINS OF THE STATION.")
    print("k.REMOVE EXISTING TRAINS FROM THE STATION.")
    print("l.UPDATE TRAIN RELATED INFORMATION.")
    q=input("enter your choice(i-l):-")
    print("\nInitially the details are..")
    display4()
    if q=='i':
        insert4()
        print("\nModified details are..")
        display4()
    elif q=='j':
        update()
        print("\nModified details are..")
        display4()
    elif q=='k':
        delete4()
        print("\nModified details are..")
        display4()
    elif q=='l':
        insert4()
        print("\nModified details are..")
        display4()
    else:
        print("enter choice correctly!!")


def insert1():
    pname=input("Enter Passenger Name:-")
    p_age=int(input("Enter Passenger Age:-"))
    to=input("Enter Destination Station:-")
    dte=input("Enter Date of Journey:-")
    phn=int(input("Enter Passenger Phone Number:-"))
    city=input("Enter Passenger's city")
    db=mysql.connector.connect(user='root',password='MYSQL',host='localhost',database='python')
    cursor=db.cursor()
    sql="insert into passenger(pname,p_age,to,dte,phn,city)VALUES('%s','%d','%s','%s','%d','%s')"%(pname,p_age,to,dte,phn,city)
    try:
        cursor.execute(mysqldb.commit())
    except:
        db.rollback()
        sb.close()#insert
def display1()
    try:
    db = mysql.connector.connect(user='root', password='MYSQL', host='localhost', database='python')
    cursor=db.cursor()
    sql="select * from passenger"
    cursor.execute.fetchall()
    results=cursor.fetchall()
    # change 1
