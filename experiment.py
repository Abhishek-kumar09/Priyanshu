import mysql.connector              # mysql connectivity
from random import randrange        # for random inputs
from time import sleep              # for syncing and fetching data
import datetime                     # for date and time usage



# ______________________________________
db = mysql.connector.connect(user='root',
                             password='priyanshu',
                             host='localhost',
                             database='python')
cursor = db.cursor()

print("\t\t\t\t-------------------------\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-"
      "---------------------------"
      "\n\t\t\t\t|\t\t\t\t\t\t🙏!🙏🏼WELCOME TO RAILWAY MANAGEMENT SYSTEM🙏🏼!🙏\t\t\t\t\t\t\t|"
      "\n\t\t\t\t|\t\t\t\t\t\t\t\t\t  _🚆NEW DELHI🚆_\t\t\t\t\t\t\t\t\t\t\t|"
      "\n\t\t\t\t-------------------------\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-"
      "---------------------------\n")
# ___________________________________________________________________________________________________________________________________________________________

def selection():
    def selection1():
        print("🔰1. PASSENGER MANAGEMENT SYSTEM.")
        print("🔰2. STAFF AND EMPLOYEE MANAGEMENT SYSTEM.")
        print("🔰3. STATION MANAGEMENT SYSTEM.")
        print("🔰4. TRAIN MANAGEMENT SYSTEM.")
        print("🔰5. EXIT")
        print("____________________________________________________________________________________________"
              "________________________________________________________________")

    selection1()
    choice = int(input("\n📌Enter Your Choice\t\t\t\t:-"))
    print("_____________________________________________________________________________"
          "______________________________________________________________________________")

# ___________________________________________________________________________________________________________________________________________________________

    def choice1():
        print("You Can Perform The Following Operations.. \n")
        print("👉🏻 A. DATA OF A SPECIFIC PASSENGER.")
        print("👉🏻 B. NEW RESERVATION.")
        print("👉🏻 C. CANCEL EXISTING RESERVATION.")
        print("👉🏻 D. UPDATE DATA OF PASSENGER.")
        print("👉🏻 E. DATA OF ALL PASSENGERS.")
        print("👉🏻 F. BACK.\n")

        x = input("📌Enter Your Choice\t\t\t\t:-")
        if x == 'a' or x == 'A':
            view1()
            print("More Passenger's Data:-")
            print("Yes or No")
            ch=input("____")
            if ch =='yes' or ch=='Yes' or ch=='YES':
                view1()
            else:
                choice1()
        elif x == 'b' or x == 'B':
            print("📍Please Provide All The Necessary Information..")
            insert1()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD_❌_❌")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA_❌_❌")
            sleep(1)
            display1()
            print("More Passenger's Data to Be Inserted:-")
            print("Yes or No")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                insert1()
            else:
                choice1()
        elif x == 'c' or x == 'C':
            delete1()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_PLEASE WAIT WHILE INFORMATION IS DELETED❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display1()
            print("More Passenger's Data To Be Deleted:-")
            print("Yes or No")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                delete1()
            else:
                choice1()
        elif x == 'd' or x == 'D':
            update1()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display1()
            print("More Passenger's Data to Update:-")
            print("Yes or No")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                update1()
            else:
                choice1()
        elif x == 'e' or x == 'E':
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t📍HERE IS THE DATA OF ALL PASSENGERS📍")
            print("_________________________________________________________________________________"
                  "___________________________________________________________________________")
            display1()
            print("\nReturning to Menu Page...")
            choice1()
        elif x == 'f' or x == 'F':
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tRETURNED TO MAIN PAGE\n")
            selection()
        else:
            print("Enter Correct Choice..!")
            choice1()

# ___________________________________________________________________________________________________________________________________________________________

    def choice2():
        print("You Can Perform The Following Operations..")
        print("👉🏻A. DATA OF SPECIFIC EMPLOYEE.")
        print("👉🏻B. NEW EMPLOYEE/STAFF.")
        print("👉🏻C. UPDATE EMPLOYEE/STAFF DETAILS.")
        print("👉🏻D. DELETE EXISTING EMPLOYEE/STAFF's DATA.")
        print("👉🏻E. DATA OF ALL EMPLOYEES.")
        print("👉🏻F. BACK.")

        y = input("\n📌Enter your choice:-")
        if y == 'A' or y == 'a':
            view2()
            print("More Employee's Data")
            ch = input("Yes or No..")
            if ch == 'yes' or ch == 'YES' or ch == 'Yes':
                view2()
            elif ch == 'no' or ch == 'NO':
                choice2()
        elif y == 'B' or y == 'b':
            print("📍Please Provide All The Necessary Information.")
            insert2()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD_❌_❌")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA_❌_❌")
            sleep(1)
            display2()
            print("More Employee's Data To be Inserted.")
            ch = input("Yes or No..")
            if ch == 'yes' or ch == 'YES' or ch == 'Yes':
                insert2()
            elif ch == 'no' or ch == 'NO':
                choice2()
        elif y == 'C' or y == 'c':
            update2()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display2()
            print("More Employee's Data to Update:-")
            print("Yes or No")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                update2()
            else:
                choice2()
        elif y == 'D' or y == 'd':
            delete2()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display2()
            print("More Employee's Data To Be Deleted:-")
            print("Yes or No")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                delete2()
            else:
                choice2()
        elif y == "E" or y == 'e':
            print("HERE IS THE DATA OF ALL EMPLOYEES..")
            display2()
            print("Returning to Menu Page.")
            choice2()
        elif y == 'F' or y == 'f':
            print("RETURNED TO MAIN PAGE")
            selection()
        else:
            print("Enter choice correctly!!")
            selection()

# ___________________________________________________________________________________________________________________________________________________________

    def choice3():
        print("You Can Perform The Following Operations.")
        print("👉🏻A. DATA OF SPECIFIC STATION.")
        print("👉🏻B. ADD NEW STATION .")
        print("👉🏻C. UPDATE STATION INFORMATION.")
        print("👉🏻D. DELETE STATION INFO AND REINSERT IT.")
        print("👉🏻E. DATA OF ALL THE STATIONS.")
        print("👉🏻F. BACK.")

        z = input("\n📌Enter your choice:-")
        if z == 'A' or 'a':
            view3()
            print("More Station's Data")
            ch = input("yes or no..")
            if ch == 'yes' or ch == 'YES' or ch == 'Yes':
                view3()
            elif ch == 'no' or ch == 'NO':
                choice3()
        elif z == 'B' or z == 'b':
            print("Please Provide All The Information.")
            insert3()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display3()
            print("More Station's Data To be Inserted.")
            ch = input("yes or no..")
            if ch == 'yes' or ch == 'YES' or ch == 'Yes':
                insert3()
            elif ch == 'no' or ch == 'NO':
                choice3()
        elif z == 'C' or z == 'c':
            update3()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display3()
            print("More Station's Data to Update:-")
            print("yes or no")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                update3()
            else:
                choice3()
        elif z == 'D' or z == 'd':
            delete3()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display3()
            print("More Station's Data To Be Deleted:-")
            print("yes or no")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                delete3()
            else:
                choice3()
        elif z == 'E' or z == 'e':
            print("Here's All The Data.")
            display3()
            choice3()
        elif z == 'F' or z == 'f':
            print("RETURNED TO MAIN PAGE.")
            selection()
        else:
            print("Enter your choice correctly!!")
            selection()

# ___________________________________________________________________________________________________________________________________________________________

    def choice4():
        print("You Can Perform The Following Operations.")
        print("👉🏻A. DATA OF SPECIFIC TRAIN.")
        print("👉🏻B. ADD NEW TRAINS .")
        print("👉🏻C. UPDATE EXISTING TRAIN.")
        print("👉🏻D. REMOVE EXISTING TRAIN.")
        print("👉🏻E. DATA OF ALL THE TRAINS.")
        print("👉🏻F. BACK")
        q = input("\n📌Enter your choice;-:-")
        if q == 'A' or q == 'a':
            print("Here's The Data.")
            view4()
            print("More Train's Data")
            ch = input("yes or no..")
            if ch == 'yes' or ch == 'YES' or ch == 'Yes':
                view4()
            elif ch == 'no' or ch == 'NO':
                choice4()
        elif q == 'B' or q == 'b':
            print("Please Provide All The Information.")
            insert4()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display4()
            print("More Train's Data To be Inserted.")
            ch = input("yes or no..")
            if ch == 'yes' or ch == 'YES' or ch == 'Yes':
                insert4()
            elif ch == 'no' or ch == 'NO':
                choice4()
        elif q == 'C' or q == 'c':
            update4()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display4()
            print("More Train's Data to Update:-")
            print("yes or no")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                update4()
            else:
                choice4()
            selection()
        elif q == 'D' or q == 'd':
            delete4()
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_UPLOADING YOUR DATA TO CLOUD❌_❌_")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_FETCHING YOUR DATA❌_❌_")
            display4()
            print("More Train's Data To Be Deleted:-")
            print("yes or no")
            ch = input("____")
            if ch == 'yes' or ch == 'Yes' or ch == 'YES':
                delete4()
            else:
                choice4()
        elif q == 'E' or q == 'e':
            print("Here's All The Data.")
            display4()
            choice4()
        elif q == 'F' or q == 'G':
            print("RETURNED TO MAIN PAGE.")
            selection()
        else:
            print("Enter choice correctly!!")
            selection()


# ___________________________________________________________________________________________________________________________________________________________

    if choice == 1:
        print("\n\t\t\t\t\t\t\t\t\t\t\t👨🏻‍WELCOME TO PASSENGER MANAGEMENT SYSTEM👨🏻‍\n")
        choice1()

# ___________________________________________________________________________________________________________________________________________________________

    elif choice == 2:
        print("\n\t\t\t\t\t\t\t\t\t\t\t👮🏻‍WELCOME TO EMPLOYEE MANAGEMENT SYSTEM👮🏻‍\n")
        choice2()

# ___________________________________________________________________________________________________________________________________________________________

    elif choice == 3:
        print("\n\t\t\t\t\t\t\t\t\t\t\t🚧WELCOME TO STATION MANAGEMENT SYSTEM🚧\n")
        choice3()
# ___________________________________________________________________________________________________________________________________________________________

    elif choice == 4:
        print("\n\t\t\t\t\t\t\t\t\t\t\t🚅WELCOME TO TRAIN MANAGEMENT SYSTEM🚅\n")
        choice4()
# ___________________________________________________________________________________________________________________________________________________________

    elif choice == 5:
        print("\t\t\t\t\t\t\t\t\t\t..........................Thank You.......................... ")

# ___________________________________________________________________________________________________________________________________________________________

    else:
        print("Enter Choice Correctly.")
        selection1()
# ..........................................................................................................................................................

def insert1():
    p_name = input("Enter passenger's name:-")
    p_name=p_name.upper()
    p_age = int(input("Enter passenger's age:-"))
    empty = []
    while True:
        pnr = randrange(9000000000, 9999999999)
        if pnr not in empty:
            empty.append(pnr)
        else:
            pass
        if len(empty) == 1000:
            break
    frm = input("Enter boarding station:-")
    frm=frm.upper()
    too = input("Enter de boarding station:-:")
    too=too.upper()
    phn = input("Enter mobile.no:-")
    if len(phn) == 10:
        phn = '+91_'+ phn[0:4]+'_' + phn[4:6] +'_'+ phn[6:10]
    elif len(phn) < 10:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t!!ERROR!!\nPhone Number Too Short.")
        print("Re Enter All the Data AGAIN..")
        insert1()

    else:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t!!ERROR!!\nPhone Number Too Long.")
        print("Re Enter All the Data AGAIN")
        insert1()
    train = input("Enter Train.:-")
    train=train.upper()
    date = int(input("Enter year"))
    month=int(input("Enter Month:-"))
    day=int(input("Enter Day:-"))
    now = datetime.datetime(date, month, day)
    sql = "insert into passenger( p_name, p_age, pnr, frm, too, phn, train,dte)  " \
          "values('%s','%d','%s','%s','%s','%s','%s','%s')" % \
          (p_name, p_age, pnr, frm, too, phn, train, now)
    try:
        cursor.execute(sql)
        db.commit()

    except:
        db.close()

# ..........................................................................................................................................................

def insert2():
    emp_name = input("Enter Employee's Name:-")
    emp_name=emp_name.upper()
    empty = []
    while True:
        emp_id = randrange(10000, 99999)
        if emp_id not in empty:
            empty.append(emp_id)
        else:
            pass
        if len(empty) == 1000:
            break
    emp_age = int(input("Enter Employee's Age:-"))
    emp_salry = int(input("Enter Employee's Salary:-"))
    emp_dept = input("Enter Employee's Department:-")
    emp_dept=emp_dept.upper()
    emp_phn = input("Enter Employee's Mobile Number:-")
    if len(emp_phn) == 10:
        emp_phn = '+91_'+ emp_phn[0:4]+'_' + emp_phn[4:6] +'_'+ emp_phn[6:10]
    elif len(emp_phn) < 10:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t!!ERROR!!\nPhone Number Too Short.")
        print("Re Enter All the Data AGAIN..")
        insert2()
    sql = "insert into employee(emp_name,emp_id,emp_age,emp_salry,emp_dept,emp_phn) " \
          "values('%s','%d','%d','%d','%s','%s')" % \
          (emp_name, emp_id, emp_age, emp_salry, emp_dept, emp_phn)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.close()

# ..........................................................................................................................................................

def insert3():
    s_name = input("Enter Station Name:-")
    s_name=s_name.upper()
    notrains = int(input("Enter Number of Trains to the Station:-"))
    nopltfrm = int(input("Enter number of Platforms:-:"))
    no_employees = int(input("Enter Number. of Employees:-"))
    no_counter = int(input("Enter Number of Counters to the Station:-"))
    station_code = input("Enter code:-")
    station_code=station_code.upper()
    sql = "insert into statn(s_name, notrains, nopltfrm, no_employees, no_counter, station_code)  " \
          "values('%s','%d','%d','%d','%d','%s')" \
          % (s_name, notrains, nopltfrm, no_employees, no_counter, station_code)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.close()

# ..........................................................................................................................................................

def insert4():
    t_name = input("Enter train name:-")
    t_name=t_name.upper()
    t_no = int(input("Enter train number:-"))
    frm = input("Enter from:-")
    frm=frm.upper()
    too = input("Enter  to:-")
    too=too.upper()
    noboggy = int(input("Enter noboggy:-:"))
    type = input("Enter type:-")
    type=type.upper()
    speed = int(input("Enter speed:-"))
    sql = "insert into train(t_name,t_no,frm,too,noboggy,type,speed)  values('%s','%d','%s','%s','%d','%s','%d')" \
          % (t_name, t_no, frm, too, noboggy, type, speed)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.close()


# ..........................................................................................................................................................
# ..........................................................................................................................................................


def view1():
    sql1="select pnr from passenger"
    cursor.execute(sql1)
    res=cursor.fetchall()
    for d in res:
        print(d, end='')
    temps = input("\nEnter PNR Number Of The Passenger Which Is To Be Shown. ")
    sql = "select * from passenger where pnr='%s'" % temps
    cursor.execute(sql)
    results = cursor.fetchall()
    print("_______________________________________________________________________________________________________________________________________")
    for c in results:
        s_no = c[0]
        p_name = c[1]
        p_age = c[2]
        pnr = c[3]
        frm = c[4]
        too = c[5]
        phn = c[6]
        train = c[7]

        print("S.no\t\t\t\t : %d\nPassenger's Name\t : %s\nPassenger's Age \t : %d"
              "\nPNR\t\t\t\t\t : %s\nFrom\t\t\t\t : %s\nTo\t\t\t\t\t : %s"
              "\nMobile No.\t\t\t : %s\nTrain\t\t\t\t : %s"
              "\n_________________________________________________________________________________"
              "___________________________________________________________________________" %
              (s_no, p_name, p_age, pnr, frm, too, phn, train))

# ___________________________________________________________________________________________________________________________________________________________

def view2():
    tempst = int(input("Enter Employee ID Which Is To Be Shown.."))
    sql = "select * from employee where emp_id='%d'" % tempst
    cursor.execute(sql)
    results = cursor.fetchall()
    for c in results:
        s_no = c[0]
        emp_name = c[1]
        emp_id = c[2]
        emp_age = c[3]
        emp_salry = c[4]
        emp_dept = c[5]
        emp_phn = c[6]
        print("\n____________________________________"
              "\nS.no : %d\nEmployee's Name : %s\nEmployee's ID : %d\nEmployee's Age : %d"
              "\nEmployee's Salary : %d\nEmployee's Department : %s\nEmployee's Phone Number : %s"
              "\n_____________________________________" %
              (s_no, emp_name, emp_id, emp_age, emp_salry, emp_dept, emp_phn))

# ___________________________________________________________________________________________________________________________________________________________

def view3():
    tempst=input("Enter Station Code Which Is To Be Shown.")
    sql = "select * from statn where station_code='%s'" % tempst
    cursor.execute(sql)
    results = cursor.fetchall()
    for c in results:
        s_no = c[0]
        s_name = c[1]
        notrain = c[2]
        nopltfrm = c[3]
        no_employees = c[4]
        no_counter = c[5]
        station_code = c[6]
        print("\n____________________________________"
              "\nS.no : %d\nStation Name : %s\nNumber of Trains to the Station : %d"
              "\nNumber of Platforms of the Station : %d\nNumber of Employees of the Station : %d"
              "\nNumber of Counters of the Station : %d\nStation Code : %s"
              "\n_____________________________________" %
              (s_no, s_name, notrain, nopltfrm, no_employees, no_counter, station_code))

# ___________________________________________________________________________________________________________________________________________________________

def view4():
    tempst=int(input("Enter Train Number Which Is To Be Shown.."))
    sql = "select * from train where t_no='%d'" % tempst
    cursor.execute(sql)
    results = cursor.fetchall()
    for c in results:
        s_no = c[0]
        t_name = c[1]
        t_no = c[2]
        frm = c[3]
        too = c[4]
        noboggy = c[5]
        type = c[6]
        speed = c[7]

        print(
            "\n____________________________________"
            "S.no : %d\nTrain Name : %s\nTrain Number : %d\nFrom : %s\nTo : %s\nNumber of Boggies : %d"
            "\nTrain Type : %s\nSpeed : %d\n_____________________________________" %
            (s_no, t_name, t_no, frm, too, noboggy, type, speed)
        )

# ___________________________________________________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________________________________________________

def display1():
    try:
        sql = "select * from passenger order by s_no"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            p_name = c[1]
            p_age = c[2]
            pnr = c[3]
            frm = c[4]
            too = c[5]
            phn = c[6]
            train = c[7]
            dte = c[8]

            print("S.no\t\t\t\t : %d\nPassenger's Name\t : %s\nPassenger's Age \t : %d"
                  "\nPNR\t\t\t\t\t : %s\nFrom\t\t\t\t : %s\nTo\t\t\t\t\t : %s"
                  "\nMobile No.\t\t\t : %s\nTrain\t\t\t\t : %s\nDate\t\t\t\t : %s"
                  "\n_________________________________________________________________________________"
                  "___________________________________________________________________________" %
                  (s_no, p_name, p_age, pnr, frm, too, phn, train, dte))
    except:
        print("ERROR!! Unable to Fetch Data..")
        db.close()

# ..........................................................................................................................................................

def display2():
    try:
        sql = "select * from employee "
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            emp_name = c[1]
            emp_id = c[2]
            emp_age = c[3]
            emp_salry = c[4]
            emp_dept = c[5]
            emp_phn = c[6]

            print(
                "\nS.no : %d\nEmployee's Name : %s\nEmployee's ID : %d\nEmployee's Age : %d\n"
                "Employee's Salary : %d\nEmployee's Department : %s\n"
                "Employee's Phone Number : %s\n_____________________________________" %
                (s_no, emp_name, emp_id, emp_age, emp_salry, emp_dept, emp_phn))
    except:
        print("ERROR!! Unable to Fetch dData..")
        db.close()

# ..........................................................................................................................................................

def display3():
    try:
        sql = "select * from statn order by s_no"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            s_name = c[1]
            notrain = c[2]
            nopltfrm = c[3]
            no_employees = c[4]
            no_counter = c[5]
            station_code = c[6]
            print("s.no : %d\nStation's Name : %s\nNo. of Trains in the station : %d\n"
                  "No. of Platform in the station : %d\nNumber of Employees in the Station : %d"
                  "\nNo. of Ticket Counters in the Station : %d\n station code : %s"
                  "\n_____________________________________" %
                  (s_no, s_name, notrain, nopltfrm, no_employees, no_counter, station_code))
    except:
        print("ERROR!! Unable to Fetch Data..")
        db.close()

# ..........................................................................................................................................................

def display4():
    try:
        sql = "select * from train order by s_no"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            t_name = c[1]
            t_no = c[2]
            frm = c[3]
            too = c[4]
            noboggy = c[5]
            type = c[6]
            speed = c[7]
            print("s.no : %d\nTrain Name : %s\nTrain Number : %d\nFrom : %s\nTo : %s\nNo. of Boggy : %d"
                  "\nType : %s\nSpeed : %d km/h\n_____________________________________" %
                  (s_no, t_name, t_no, frm, too, noboggy, type, speed))
    except:
        print("ERROR!! Unable to Fetch Data..")
        db.close()

# ..........................................................................................................................................................
# ..........................................................................................................................................................

def update1():
    tempst = input("Enter PNR Number Associated with Passenger:-")

    def modified1():
        sql = "select * from passenger where pnr='%s'" % tempst
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            p_name = c[1]
            p_age = c[2]
            pnr = c[3]
            frm = c[4]
            too = c[5]
            phn = c[6]
            train = c[7]

            print("S.no\t\t\t\t : %d\nPassenger's Name\t : %s\nPassenger's Age \t : %d"
                  "\nPNR\t\t\t\t\t : %s\nFrom\t\t\t\t : %s\nTo\t\t\t\t\t : %s"
                  "\nMobile No.\t\t\t : %s\nTrain\t\t\t\t : %s"
                  "\n_________________________________________________________________________________"
                  "___________________________________________________________________________" %
                  (s_no, p_name, p_age, pnr, frm, too, phn, train))

    modified1()

    try:
        print("From Which Section You Want to Update>> ")
        print("1. Serial Number")
        print("2. Passenger's Name.")
        print("3. Passenger's Age.")
        print("4. Passenger's PNR Number.")
        print("5. Passenger's Boarding Station.")
        print("6. Passenger's De Boarding Station.")
        print("7. Passenger's Phone Number.")
        print("8. Passenger's Train.")
        print("9. Exit.")

        choice2 = int(input("Enter Desired Section :-"))
        if choice2 == 1:
            sub2 = int(input("Enter New Serial Number:-"))
            sql1 = "update passenger set s_no='%d' where pnr ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 2:
            sub2 = input("Enter New Passenger's Name:-")
            sql1 = "update passenger set p_name='%s' where pnr ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 3:
            sub2 = int(input("Enter New Passenger's Age:-"))
            sql1 = "update passenger set p_age='%d' where pnr ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 4:
            sub2 = input("Enter New PNR Number:-")
            sql1 = "update passenger set pnr='%s' where pnr ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 5:
            sub2 = input("Enter New Boarding's Station:-")
            sql1 = "update passenger set frm='%s' where pnr ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 6:
            sub2 = input("Enter New De Boarding Station:-")
            sql1 = "update passenger set too='%s' where pnr ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 7:
            sub2 = input("Enter New Passenger's Phone Number:-")
            sql1 = "update passenger set phn='%s' where pnr ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 8:
            sub2 = input("Enter New Passenger's Train:-")
            sql1 = "update passenger set train='%s' where pnr ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.close()
        elif choice2 == 9:
            print("Nothing Updated!!")
        else:
            print("Enter choice correctly!!")

        print("Updated Data is :")
        modified1()
        # calling modified again for updated data
        print("a.Update some more stuff:")
        print("b.Update Completed:")
        choice3 = input("Enter What You Want to Do. :")
        if choice3 == 'a':
            update1()
            print("Data After Updating from Table..")
            modified1()
        elif choice3 == 'b':
            print("Update Completed..")

    except:
        print("ERROR!! Unable to Fetch Data..")

# ..........................................................................................................................................................

def update2():
    tempst = int(input("Enter Employee's id You want to Update:-"))

    def modified2():
        sql = "select * from employee where emp_id='%d'" % tempst
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            emp_name = c[1]
            emp_id = c[2]
            emp_age = c[3]
            emp_salry = c[4]
            emp_dept = c[5]
            emp_phn = c[6]
            print("\n____________________________________"
                  "\nS.no : %d\nEmployee's Name : %s\nEmployee's ID : %d\nEmployee's Age : %d"
                  "\nEmployee's Salary : %d\nEmployee's Department : %s\nEmployee's Phone Number : %s"
                  "\n_____________________________________" %
                  (s_no, emp_name, emp_id, emp_age, emp_salry, emp_dept, emp_phn))

    modified2()

    try:
        print("From Which Section You Want To Update>>")
        print("1. Serial Number.")
        print("2. Employee's Name.")
        print("3. Employee's ID.")
        print("4. Employee's Age.")
        print("5. Employee's Salary.")
        print("6. Employee's Department.")
        print("7. Employee's Phone Number.")
        print("8. Exit.")

        choice2 = int(input("Enter Desired Section:-"))
        if choice2 == 1:
            sub2 = int(input("Enter New Serial Number:-"))
            sql1 = "update employee set s_no='%d' where emp_id ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 2:
            sub2 = input("Enter New Employee's Name:-")
            sql1 = "update employee set emp_name='%s' where emp_id ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 3:
            sub2 = int(input("Enter New Employee's ID:-"))
            sql1 = "update employee set emp_id='%d' where emp_id ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 4:
            sub2 = int(input("Enter New Employee's Age:-"))
            sql1 = "update employee set emp_age='%d' where emp_id ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 5:
            sub2 = int(input("Enter New Employee's Salary:-"))
            sql1 = "update employee set emp_salry='%d' where emp_id ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 6:
            sub2 = input("Enter New Employee's Department:-")
            sql1 = "update employee set emp_dept='%s' where emp_id ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 7:
            sub2 = input("Enter New Employee's Phone Number:-")
            sql1 = "update employee set emp_phn='%s' where emp_id ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 8:
            print("nothing updated")
            db.close()
        else:
            print("Enter choice correctly!!")

        print("Updated Data is :")
        modified2()
        # calling modified again for updated data
        print("a.Update some more stuff:")
        print("b.Update Completed:")
        choice3 = input("Enter What You Want to Do. :")
        if choice3 == 'a':
            update1()
            print("Data After Updating from Table..")
            modified2()
        elif choice3 == 'b':
            print("Update Completed..")

    except:
        print("ERROR!! Unable to Fetch Data..")

# ..........................................................................................................................................................

def update3():
    tempst = input("Enter Station Code You want to Update:-")

    def modified():
        sql = "select * from statn where station_code='%s'" % tempst
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            s_name = c[1]
            notrain = c[2]
            nopltfrm = c[3]
            no_employees = c[4]
            no_counter = c[5]
            station_code = c[6]
            print("\n____________________________________"
                  "\nS.no : %d\nStation Name : %s\nNumber of Trains to the Station : %d"
                  "\nNumber of Platforms of the Station : %d\nNumber of Employees of the Station : %d"
                  "\nNumber of Counters of the Station : %d\nStation Code : %s"
                  "\n_____________________________________" %
                  (s_no, s_name, notrain, nopltfrm, no_employees, no_counter, station_code))

    modified()

    try:
        print("From Which Section You Want To Update>>")
        print("1. Serial Number.")
        print("2. Station Name.")
        print("3. Number of Trains to the Station.")
        print("4. Number of Platforms of the Station.")
        print("5. Number of Employees of the Station.")
        print("6. Number of Counters of the Station.")
        print("7. Station Code.")
        print("8. Exit.")

        choice2 = int(input("Enter Desired Section:-"))
        if choice2 == 1:
            sub2 = int(input("Enter New Serial Number:-"))
            sql1 = "update statn set s_no='%d' where station_code ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 2:
            sub2 = input("Enter New Station Name:-")
            sql1 = "update statn set s_name='%s' where station_code ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 3:
            sub2 = int(input("Enter New No. of Trains of the Station:-"))
            sql1 = "update statn set notrains='%d' where station_code ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 4:
            sub2 = int(input("Enter New No. of Platforms of the Station:-"))
            sql1 = "update statn set nopltfrm='%d' where station_code ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 5:
            sub2 = int(input("Enter New No. of Employees of the Station:-"))
            sql1 = "update statn set no_employees='%d' where station_code ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 6:
            sub2 = int(input("Enter New No. of Counters of the Station:-"))
            sql1 = "update statn set no_counter='%s' where station_code ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 7:
            sub2 = input("Enter New Station Code:-")
            sql1 = "update statn set station_code ='%s' where station_code ='%s'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 8:
            print("nothing updated")
            db.close()
        else:
            print("Enter choice correctly!!")

        print("Updated Data is :")
        modified()
        # calling modified again for updated data
        print("a.Update some more stuff:")
        print("b.Update Completed:")
        choice3 = input("Enter What You Want to Do. :")
        if choice3 == 'a':
            update1()
            print("Data After Updating from Table..")
            modified()
        elif choice3 == 'b':
            print("Update Completed..")

    except:
        print("ERROR!! Unable to Fetch Data..")

# ..........................................................................................................................................................

def update4():
    tempst = int(input("Enter Train Number of the Train which You Want to update:-"))

    def modified():
        sql = "select * from train where t_no='%d'" % tempst
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            t_name = c[1]
            t_no = c[2]
            frm = c[3]
            too = c[4]
            noboggy = c[5]
            type = c[6]
            speed = c[7]

            print(
                "\n____________________________________"
                "S.no : %d\nTrain Name : %s\nTrain Number : %d\nFrom : %s\nTo : %s\nNumber of Boggies : %d"
                "\nTrain Type : %s\nSpeed : %d\n_____________________________________" %
                (s_no, t_name, t_no, frm, too, noboggy, type, speed)
            )

    modified()

    try:
        print("From Which Section You Want To Update>>")
        print("1. Serial Number.")
        print("2. Train Name.")
        print("3. Train Number.")
        print("4. Train Starting Station.")
        print("5. Train Final Station.")
        print("6. Number of Boggies of the Train.")
        print("7. Train Type.")
        print("8. Train Speed.")
        print("9. Exit.")

        choice2 = int(input("Enter Desired Section:-"))
        if choice2 == 1:
            sub2 = int(input("Enter New Serial Number:-"))
            sql1 = "update train set s_no='%d' where t_no ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 2:
            sub2 = input("Enter New Train Name:-")
            sql1 = "update train set t_name='%s' where t_no ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 3:
            sub2 = int(input("Enter New Train Number:-"))
            sql1 = "update train set t_no='%d' where t_no ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 4:
            sub2 = input("Enter New Train's starting Station:-")
            sql1 = "update train set frm='%s' where t_no ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 5:
            sub2 = input("Enter New Train's final Station:-")
            sql1 = "update train set too='%s' where t_no ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 6:
            sub2 = int(input("Enter Updated no.of Boggies of the Train:-"))
            sql1 = "update train set noboggy='%d' where t_no ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 7:
            sub2 = input("Enter New Train Type:-")
            sql1 = "update train set type='%s' where t_no ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.commit()
        elif choice2 == 8:
            sub2 = int(input("Enter New Train's Speed:-"))
            sql1 = "update Train set speed='%d' where t_no ='%d'" % (sub2, tempst)
            cursor.execute(sql1)
            db.close()
        elif choice2 == 9:
            print("Nothing Updated!!")
        else:
            print("Enter choice correctly!!")

        print("Updated Data is :")
        modified()
        # calling modified again for updated data
        print("a.Update some more stuff:")
        print("b.Update Completed:")
        choice3 = input("Enter What You Want to Do. :")
        if choice3 == 'a':
            update1()
            print("Data After Updating from Table..")
            modified()
        elif choice3 == 'b':
            print("Update Completed..")

    except:
        print("ERROR!! Unable to Fetch Data..")

# ..........................................................................................................................................................
# ..........................................................................................................................................................

def delete1():
    tempst = input("Enter Passenger's PNR Number Which is to be Deleted")

    def modified1():
        sql1 = "select * from passenger where pnr='%s'" % tempst
        cursor.execute(sql1)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            p_name = c[1]
            p_age = c[2]
            pnr = c[3]
            frm = c[4]
            too = c[5]
            phn = c[6]
            train = c[7]

            print("\n____________________________________"
                  "s.no : %d\nPassenger's Name : %s\nPassenger's Age : %d\nPNR : %s\nFrom : %s\nTo : %s"
                  "\nMobile No. : %s\nTrain : %s\n_____________________________________" %
                  (s_no, p_name, p_age, pnr, frm, too, phn, train))

    modified1()

    try:
        sql = "delete from passenger where pnr='%s'" % tempst
        ans = input("Are you sure want to delete the given entry(yes/no)")
        if ans == 'yes' or ans == 'Yes':
            cursor.execute(sql)
            db.commit()
    except:
        print("Execution Stopped!!!!")
        db.close()

# ..........................................................................................................................................................

def delete2():
    tempst = int(input("Enter Employee's id You want to Update:-"))

    def modified2():
        sql2 = "select * from employee where emp_id='%d'" % tempst
        cursor.execute(sql2)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            emp_name = c[1]
            emp_id = c[2]
            emp_age = c[3]
            emp_salry = c[4]
            emp_dept = c[5]
            emp_phn = c[6]
            print("\n____________________________________"
                  "\nS.no : %d\nEmployee's Name : %s\nEmployee's ID : %d\nEmployee's Age : %d"
                  "\nEmployee's Salary : %d\nEmployee's Department : %s\nEmployee's Phone Number : %s"
                  "\n_____________________________________" %
                  (s_no, emp_name, emp_id, emp_age, emp_salry, emp_dept, emp_phn))

    modified2()

    try:
        sql = "delete from employee where emp_id='%d'" % tempst
        ans = input("Are you sure want to delete the given entry(yes/no)")
        if ans == 'yes' or ans == 'Yes':
            cursor.execute(sql)
            db.commit()
    except:
        print("error")
        db.close()

# ..........................................................................................................................................................

def delete3():
    tempst = input("Enter Station Code You want to Delete:-")

    def modified():
        sql3 = "select * from statn where station_code='%s'" % tempst
        cursor.execute(sql3)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            s_name = c[1]
            notrain = c[2]
            nopltfrm = c[3]
            no_employees = c[4]
            no_counter = c[5]
            station_code = c[6]
            print("\n____________________________________"
                  "\nS.no : %d\nStation Name : %s\nNumber of Trains to the Station : %d"
                  "\nNumber of Platforms of the Station : %d\nNumber of Employees of the Station : %d"
                  "\nNumber of Counters of the Station : %d\nStation Code : %s"
                  "\n_____________________________________" %
                  (s_no, s_name, notrain, nopltfrm, no_employees, no_counter, station_code))

    modified()

    try:
        sql = "delete from statn where station_code='%s'" % tempst
        ans = input("Are you sure want to delete the given entry(yes/no)")
        if ans == 'yes' or ans == 'Yes':
            cursor.execute(sql)
            db.commit()
    except:
        print("error")
        db.close()

# ..........................................................................................................................................................

def delete4():
    tempst = int(input("Enter Train Number of the Train which You Want to update:-"))

    def modified():
        sql4 = "select * from train where t_no='%d'" % tempst
        cursor.execute(sql4)
        results = cursor.fetchall()
        for c in results:
            s_no = c[0]
            t_name = c[1]
            t_no = c[2]
            frm = c[3]
            too = c[4]
            noboggy = c[5]
            type = c[6]
            speed = c[7]

            print(
                "\n____________________________________"
                "S.no : %d\nTrain Name : %s\nTrain Number : %d\n"
                "From : %s\nTo : %s\nNumber of Boggies : %d"
                "\nTrain Type : %s\nSpeed : %d\n_____________________________________" %
                (s_no, t_name, t_no, frm, too, noboggy, type, speed)
            )

    modified()

    try:
        sql = "delete from train where t_no='%d'" % tempst
        ans = input("Are you sure want to delete the given entry(yes/no)")
        if ans == 'yes' or ans == 'Yes':
            cursor.execute(sql)
            db.commit()
    except:
        print("🚫🚫Error🚫🚫")
        db.close()

selection()
