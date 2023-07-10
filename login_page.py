import mysql.connector
from my_packs import add_user_page
from my_packs import admin_home
from my_packs import user_home
from time import sleep


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql123",
    auth_plugin='mysql_native_password'
)


def welcome_page():
    point = mydb.cursor()
    point.execute("use quiz_book;")
    '''
    point.execute("show tables;")
    tables = point.fetchall()
    print(tables)'''
    print(" ------------------------")
    print("|  Welcome to Quiz Book  |")
    print(" ------------------------")
    try:
        print("1. Login as Admin      2. Login as User")
        print("3. Sign Up             4. Exit")
        choice = int(input("=> "))
        if choice == 1:
            print("Admin Login")
            try:
                val = int(input("Admin ID: "))
                password = input("Password: ")
                query = "select password from admin_tab where admin_id = %s"
                id = (val,)
                point.execute(query, id)
                record = point.fetchall()
                if len(record) <= 0:
                    print("No admin found with the entered admin ID. Please try again!\n\n")
                    welcome_page()
                else:
                    for values in record:
                        ps = values[0]
                        if password == ps:
                            print("Verification Successful. Logging you in...")
                            sleep(2)
                            admin_home.admin_home_start(val)
                        elif password != ps:
                            print("Password Incorrect. Please try again!\n\n")
                            welcome_page()
            except ValueError:
                print("Please enter valid Admin ID!")
                print("Returning Homepage...")
                sleep(2)
                welcome_page()
        elif choice == 2:
            print("User Login")
            val = int(input("User ID: "))
            password = input("Password: ")
            query = "select password from user_tab where user_id = %s"
            id = (val,)
            point.execute(query, id)
            record = point.fetchall()
            if len(record) <= 0:
                print("No User found with the entered User ID. Please try again!\n\n")
                welcome_page()
            else:
                for values in record:
                    ps = values[0]
                    if password == ps:
                        print("Verification Successful. Logging you in...")
                        sleep(2)
                        user_home.user_home_start(val)
                    else:
                        print("Password incorrect. Please try again!\n\n")
                        welcome_page()
        elif choice == 3:
            add_user_page.signup_fn()
            welcome_page()
        elif choice == 4:
            print("Quiting Program...")
            sleep(1)
            print("Thanks for Visiting!")
            sleep(2)
            exit()
        else:
            print("Please Select Valid option\n\n")
            welcome_page()
    except ValueError:
        print("Please enter valid Admin ID!")
        print("Returning Homepage in 3 seconds...")
        sleep(3)
        welcome_page()
welcome_page()



