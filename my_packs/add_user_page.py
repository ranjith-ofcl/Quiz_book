import mysql.connector
from time import sleep
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sql123",
    auth_plugin='mysql_native_password'
)

point = mydb.cursor()
point.execute("use quiz_book;")

def signup_fn():
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
        print("       1. Confirm      2. Reset     3. Login")
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
                print("User ID created successfully. Please make a note of your User ID")
                print("Here is your User ID :", user_id)
                sleep(3)
                print("Press any button to go to Login page.")
                dummy = input("...")
            else:
                print("Passowrd mismatch. Please try again!")
                sleep(2)
                signup_fn()
        elif ch == 2:
            print("Resettings data...")
            sleep(3)
            signup_fn()
        elif ch == 3:
            print("redirecting to Signin page...")
            sleep(2)
    except ValueError:
        print("Please Select Valid Option!")

#signup_fn()

