import mysql.connector
from Quiz_Book_proj.my_packs import search_user
from time import sleep
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql123",
    auth_plugin='mysql_native_password'
)

point = mydb.cursor()
point.execute("use quiz_book;")

def admin_home_start(id):
    query = "select user_id from admin_tab where admin_id = %s"
    val = (id,)
    point.execute(query,val)
    record = point.fetchall()
    for data in record:
        u_id = data[0]
    user_id = (u_id,)
    query = "select name from user_tab where user_id = %s"
    point.execute(query, user_id)
    record = point.fetchall()
    for data in record:
        name = data[0]
    print("\n")
    print("--------------------------------------")
    print("|  Welcome", name , "as Administrator  |")
    print("--------------------------------------")
    features()

def features():
    print("\nSelect Operation you want to Perform, ")
    print("1. User Operations          2. Quiz Operations")
    print("3. Logout")
    try:
        choice = int(input("=> "))
        if choice == 1:
            user_operations()
        elif choice == 2:
            quiz_operations()
        elif choice == 3:
            exit()
        else:
            print("Please select valid operation.")
            sleep(3)
            features()
    except ValueError:
        print("Please select valid operation.")
        sleep(3)
        features()

def user_operations():
    print("\n")
    print("|||| User Operations ||||")
    print("1. View all Users        2. Search User         3. Add User")
    print("4. Modify User           5. Delete User         6. Back")
    try:
        choice = int(input("=> "))
        if choice == 1:
            view_users()
        elif choice == 2:
            search_user.search_type()
            user_operations()
        elif choice == 3:
            add_user()
        elif choice == 4:
            modify_user()
        elif choice == 5:
            delete_user()
        elif choice == 6:
            features()
        else:
            print("Please select valid operation.")
            sleep(3)
            user_operations()
    except ValueError:
        print("Please select valid operation.")
        sleep(3)
        user_operations()


def quiz_operations():
    print("\n")
    print("|||| Quiz Operations ||||")
    print("\n")
    print("1. View all Quiz        2. View quiz by Difficulty        3. Search Quiz")
    print("4. Add Quiz             5. Modify Quiz                    6. Delete Quiz")
    print("7. Back")
    try:
        choice = int(input("=> "))
        if choice == 1:
            view_all_ques()
        elif choice == 2:
            view_ques_by_diff()
        elif choice == 3:
            search_ques()
        elif choice == 4:
            add_ques()
        elif choice == 5:
            modify_ques()
        elif choice == 6:
            delete_ques()
        elif choice == 7:
            features()
        else:
            print("Please select valid operation.")
            sleep(3)
            quiz_operations()
    except ValueError:
        print("Please select valid operation.")
        sleep(3)
        quiz_operations()

def view_users():
    print("\n")
    print("|||| View All Users ||||")
    print("\n Retrieving Data....")
    sleep(1)
    query = "select * from user_tab;"
    point.execute(query)
    record = point.fetchall()
    print(len(record), "Records Found...")
    sleep(1.5)
    for data in record  :
        print("-------------------------------------")
        print("User ID: ", data[0])
        print("Username: ", data[1])
        print("Name: ", data[3])
        print("Mobile number: ", data[4])
        print("Email address: ", data[5])
        print("User Level: ", data[6])
        print("Current points: ", data[7])
        print("User password: ", data[2])
    print("\n Returning to User Operations...")
    sleep(3)
    user_operations()

def add_user():
    print("\n")
    print("|||| Add new User ||||")
    print("\n  Fillup below information to Create new Account.")
    user_name = input("User name: ")
    name = input("Name: ")
    password = input("Password: ")
    re_type = input("Re-type Password: ")
    mobile = input("Mobile: ")
    mail = input("Mail address: ")
    user_level = 1
    points = 0
    try:
        print("\nConfirm to Create new account with above information?")
        print("       1. Confirm      2. Reset     3. Back")
        ch = int(input("=> "))
        if ch == 1:
            if password == re_type:
                point.execute("select max(user_id) from user_tab")
                value = point.fetchall()
                for i in value:
                    max_id = i[0] + 1
                user_id = max_id
                query = "insert into user_tab (`user_id`,`user_name`,`password`,`name`,`mobile`,`mail`,`user_level`, `points`) Values(%s,%s,%s,%s,%s,%s,%s,%s);"
                in_values = (user_id, user_name, password, name, mobile, mail, user_level, points)
                point.execute(query, in_values)
                mydb.commit()
                print("User ID created successfully. Please share User ID with the user.")
                print("New User ID:", user_id)
                sleep(3)
                print("Press any button to go to back.")
                dummy = input("...")
                features()
            else:
                print("Passowrd mismatch!")
                sleep(2)
                print("1. Try again    2. Back")
                choice = int(input("=> "))
                if choice == 1:
                    add_user()
                elif choice == 2:
                    user_operations()
                else:
                    print("Invalid option. Returning back...")
                    sleep(2)
                    user_operations()
        elif ch == 2:
            print("Resettings data...")
            sleep(3)
            add_user()
        elif ch == 3:
            print("redirecting to Homepage...")
            sleep(2)
            features()
    except ValueError:
        print("Please Select Valid Option!")
        features()

def modify_user():
    print("\n")
    print("|||| Modify User ||||")
    print("\n")
    try:
        print("What data you want to Modify?")
        print("1. Username          2. Password                3. Name")
        print("4. Mobile            5. E-Mail address          6. Complete User Modification")
        print("7. Back    ")
        choice = int(input("=> "))
        if choice == 1:
            try:
                id = int(input("Enter ID: "))
                name = input("Enter correct Username: ")
                query = "update user_tab set user_name = %s where user_id = '%s'"
                values = (name, id)
                point.execute(query, values)
                mydb.commit()
                print("Record updated Successfully.")
                sleep(0.5)
                print("Returning back...")
                sleep(1)
                user_operations()
            except:
                mydb.rollback()
                print("Something went wrong. Record may not be updated.")
                sleep(0.5)
                print("Please view record for changes.")
                sleep(2)
                user_operations()
        elif choice == 2:
            try:
                id = int(input("Enter ID: "))
                ps = input("Enter new Password: ")
                query = "update user_tab set password = %s where user_id = '%s'"
                values = (ps, id)
                point.execute(query, values)
                mydb.commit()
                print("Record updated Successfully.")
                sleep(0.5)
                print("Returning back...")
                sleep(1)
                user_operations()
            except:
                mydb.rollback()
                print("Something went wrong. Record may not be updated.")
                sleep(0.5)
                print("Please view record for changes.")
                sleep(2)
                user_operations()
        elif choice == 3:
            try:
                id = int(input("Enter ID: "))
                name = input("Enter correct Name: ")
                query = "update user_tab set name = %s where user_id = '%s'"
                values = (name, id)
                point.execute(query, values)
                mydb.commit()
                print("Record updated Successfully.")
                sleep(0.5)
                print("Returning back...")
                sleep(1)
                user_operations()
            except:
                mydb.rollback()
                print("Something went wrong. Record may not be updated.")
                sleep(0.5)
                print("Please view record for changes.")
                sleep(2)
                user_operations()
        elif choice == 4:
            try:
                id = int(input("Enter ID: "))
                mobile = input("Enter correct Mobile number: ")
                query = "update user_tab set mobile = %s where user_id = '%s'"
                values = (mobile, id)
                point.execute(query, values)
                mydb.commit()
                print("Record updated Successfully.")
                sleep(0.5)
                print("Returning back...")
                sleep(1)
                user_operations()
            except:
                mydb.rollback()
                print("Something went wrong. Record may not be updated.")
                sleep(0.5)
                print("Please view record for changes.")
                sleep(2)
                user_operations()
        elif choice == 5:
            try:
                id = int(input("Enter ID: "))
                mail = input("Enter correct E-Mail address: ")
                query = "update user_tab set mail = %s where user_id = '%s'"
                values = (mail, id)
                point.execute(query, values)
                mydb.commit()
                print("Record updated Successfully.")
                sleep(0.5)
                print("Returning back...")
                sleep(1)
                user_operations()
            except:
                mydb.rollback()
                print("Something went wrong. Record may not be updated.")
                sleep(0.5)
                print("Please view record for changes.")
                sleep(2)
                user_operations()
        elif choice == 6:
            try:
                id = int(input("User ID: "))
                u_name = input("Username: ")
                name = input("Correct Name: ")
                mobile = input("Mobile No: ")
                mail = input("Correct E-Mail address: ")
                ps = input("New Password: ")
                print("Do you confirm to Modify this user with above information?")
                print("            1. Confirm           2. Cancel")
                ch = int(input("=> "))
                if ch == 1:
                    query = "update user_tab set user_name = %s, password = %s, name = %s, mobile = %s, mail = %s where user_id = '%s'"
                    values = (u_name, ps, name, mobile, mail, id)
                    point.execute(query, values)
                    mydb.commit()
                    print("Record updated Successfully.")
                    sleep(0.5)
                    print("Returning back...")
                    sleep(1)
                    user_operations()
                elif ch == 2:
                    print("Operation cancelled...")
                    sleep(0.5)
                    print("Returning back...")
                    sleep(1)
                    user_operations()
                else:
                    print("Invalid option. Please try again...")
                    sleep(2)
                    modify_user()
            except:
                mydb.rollback()
                print("Something went wrong. Record may not be updated.")
                sleep(0.5)
                print("Please view record for changes.")
                sleep(2)
                user_operations()
        elif  choice == 7:
            print("Returning Back...")
            sleep(2)
            user_operations()
    except ValueError:
        print("Please select valid option!")
        sleep(2)
        modify_user()

def delete_user():
    print("\n")
    id = int(input("User ID: "))
    print("Are you confirm to delete user?")
    print("1. Confirm      2. Cancel")
    try:
        choice = int(input("=> "))
        if choice == 1:
            try:
                u_id = (id,)
                query = "delete from user_tab where user_id = %s"
                point.execute(query, u_id)
                mydb.commit()
                print("Record deleted successfully.")
                sleep(0.5)
                print("Returning back...")
                sleep(1)
                user_operations()
            except:
                mydb.rollback()
        elif choice==2:
            print("Operation cancelled...")
            sleep(1)
            user_operations()
        else:
            print("Please Enter valid option! ")
            sleep(1)
            delete_user()
    except ValueError:
        print("Please Enter valid option! ")
        sleep(1)
        delete_user()

def view_all_ques():
    print("|||| View All Quiz ||||")
    print("\n Retrieving Data...")
    sleep(2)
    query = "select * from quiz"
    point.execute(query)
    record = point.fetchall()
    print(len(record), " Records Found")
    sleep(1)
    for data in record:
        print("---------------------------------------------------")
        print("Question: ", data[1])
        print("Options: ", end="  ")
        print(data[3], " | ", data[4], " | ", data[5], " | ", data[6])
        print("Answer: ", data[7])
        print("Quiz ID: ", data[0])
        print("Quiz Level: ", data[2])
        print("Points from Quiz: ", data[2])
    print("\nReturning to Quiz Operations...")
    sleep(3)
    quiz_operations()

def view_ques_by_diff():
    print("\n")
    try:
        diff = int(input("Enter Difficuty: "))
        dif = (diff, )
        query = "select * from quiz where q_lvl = %s;"
        point.execute(query, dif)
        record = point.fetchall()
        print(len(record), " Records Found")
        sleep(1)
        for data in record:
            print("---------------------------------------------------")
            print("Question: ", data[1])
            print("Options: ", end="  ")
            print(data[3], " | ", data[4], " | ", data[5], " | ", data[6])
            print("Answer: ", data[7])
            print("Quiz ID: ", data[0])
            print("Quiz Level: ", data[2])
            print("Points from Quiz: ", data[2])
        print("\nReturning to Quiz Operations...")
        sleep(3)
        quiz_operations()
    except ValueError:
        print("Please Enter valid Difficulty from 1 to 5: ")
        sleep(2)
        view_ques_by_diff()

def search_ques():
    print("\n")
    try:
        diff = input("Quiz ID: ")
        id = (diff,)
        query = "select * from quiz where q_id = %s;"
        point.execute(query, id)
        record = point.fetchall()
        print(len(record), "Records Found")
        sleep(1)
        for data in record:
            print("---------------------------------------------------")
            print("Question: ", data[1])
            print("Options: ", end="  ")
            print(data[3], " | ", data[4], " | ", data[5], " | ", data[6])
            print("Answer: ", data[7])
            print("Quiz ID: ", data[0])
            print("Quiz Level: ", data[2])
            print("Points from Quiz: ", data[2])
        print("\nReturning to Quiz Operations...")
        sleep(3)
        quiz_operations()
    except ValueError:
        print("Please Enter valid Quiz ID. ")
        sleep(1)
        search_ques()




def add_ques():
    print("|||| Add Quiz ||||")
    sleep(2)
    point.execute("select max(q_id) from quiz;")
    record = point.fetchall()
    for x in record:
        q_id = x[0]
    dum = int(q_id[-6:]) + 1
    new_qid = 'q0' + str(dum)
    print("\n")
    print("Quiz ID = ", new_qid)
    q_name = input("Quiz: ")
    q_lvl = int(input("Quiz Level: "))
    opt_1 = input("Option 1: ")
    opt_2 = input("Option 2: ")
    opt_3 = input("Option 3: ")
    opt_4 = input("Option 4: ")
    quiz_ans = input(" Answer: ")
    try :
        print("Do you confirm to add above Quiz?")
        print("1. Confirm 2. Reset 3. Cancel")
        choice = int(input("=> "))
        if choice == 1:
            query = "insert into quiz (`q_id`,`q_ques`,`q_lvl`,`q_opt1`,`q_opt2`,`q_opt3`,`q_opt4`,`q_ans`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
            values = (new_qid, q_name, q_lvl, opt_1, opt_2, opt_3, opt_4, quiz_ans)
            point.execute(query, values)
            mydb.commit()
            sleep(1)
            print("Quiz added Successfully. ")
            sleep(2)
            print("1. Add again 2. Back 3. Home")
            ch = int(input("=> "))
            if ch == 1:
                add_ques()
            elif ch == 2:
                print("Returning Back...")
                sleep(1)
                quiz_operations()
            elif ch == 3:
                features()
            else:
                print("Invalid option, returning to Home...")
                sleep(3)
                features()
        elif choice == 2:
            print("Entered details Erased...")
            sleep(1)
            add_ques()
        elif choice == 3:
            print("Process Cancelled...")
            sleep(1)
            quiz_operations()
    except ValueError:
        print("Invalid option, please try again.")
        sleep(2)
        add_ques()



def modify_ques():
    print("\n")
    try:
        id = input("Enter Quiz ID: ")
        val = (id,)
        qu = "select * from quiz where q_id = %s"
        point.execute(qu, val)
        record = point.fetchall()
        if len(record) == 1:
            print("1. Modify Options    2. Modify Answer    3. Modify Level")
            print("4. Back    ")
            try:
                ch = int(input("=> "))
                if ch == 1:
                    opt_1 = input("Option 1: ")
                    opt_2 = input("Option 2: ")
                    opt_3 = input("Option 3: ")
                    opt_4 = input("Option 4: ")
                    ans = input("Answer: ")
                    query = "update quiz set q_opt1 = %s, q_opt2 = %s, q_opt3 = %s, q_opt4 = %s, q_ans = %s where q_id = %s"
                    values = (opt_1, opt_2, opt_3, opt_4, ans, id)
                    point.execute(query, values)
                    mydb.commit()
                    print("Quiz updated Successfully.")
                    sleep(0.5)
                    print("Returning back...")
                    sleep(1)
                    quiz_operations()
                elif ch == 2:
                    ans = input("Answer: ")
                    query = "update quiz set  q_ans = %s where q_id = %s"
                    values = (ans, id)
                    point.execute(query, values)
                    mydb.commit()
                    print("Quiz updated Successfully.")
                    sleep(0.5)
                    print("Returning back...")
                    sleep(1)
                    quiz_operations()
                elif ch == 3:
                    lvl = int(input("New Level: "))
                    query = "update quiz set q_lvl = %s where q_id = %s"
                    values = (lvl, id)
                    point.execute(query, values)
                    mydb.commit()
                    print("Quiz updated Successfully.")
                    sleep(0.5)
                    print("Returning back...")
                    sleep(1)
                    quiz_operations()
                elif ch == 4:
                    print("Returning back...")
                    sleep(1)
                    quiz_operations()
                else:
                    print("Select Valid option.")
                    sleep(2)
            except ValueError:
                print("Select Valid option.")
                sleep(2)
                modify_ques()
        else:
            print("No Quiz found with the Entered ID. Please try again!...")
            sleep(2)
            modify_ques()
    except:
        mydb.rollback()
        print("Something went wrong. Record may not be updated.")
        sleep(0.5)
        print("Please view record for changes.")
        sleep(2)
        quiz_operations()


def delete_ques():
    print("\n")
    id = input("Quiz ID: ")
    q_id = (id,)
    qu = "select * from quiz where q_id = %s"
    point.execute(qu, q_id)
    rec = point.fetchall()
    print(len(rec))
    if len(rec) == 1:
        print("Are you confirm to delete user?")
        print("1. Confirm      2. Cancel")
        try:
            choice = int(input("=> "))
            if choice == 1:
                try:
                    query = "delete from quiz where q_id = %s"
                    point.execute(query, q_id)
                    mydb.commit()
                    print("Record deleted successfully.")
                    sleep(0.5)
                    print("Returning back...")
                    sleep(1)
                    quiz_operations()
                except:
                    mydb.rollback()
            elif choice == 2:
                print("Operation cancelled...")
                sleep(1)
                quiz_operations()
            else:
                print("Please Enter valid option! ")
                sleep(1)
                delete_ques()
        except ValueError:
            print("Please Enter valid option! ")
            sleep(1)
            delete_ques()
    else:
        print("No Record found to Delete.")
        print("Returning Back...")
        quiz_operations()


#user_operations()
#quiz_operations()

#admin_home_start(1)

