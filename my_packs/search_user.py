import mysql.connector
from time import sleep

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql123",
    auth_plugin='mysql_native_password'
)

point = mydb.cursor()
point.execute("use quiz_book;")


def search_type():
    print("\n")
    print("|||| Search User ||||")
    print("1. Search by User ID          2. Search by Username")
    print("3. Search by Name             4. Search by Level")
    print("5. Back                       ")
    try:
        choice = int(input("=> "))
        if choice == 1:
            search_id()
        elif choice == 2:
            search_username()
        elif choice == 3:
            search_name()
        elif choice == 4:
            search_level()
        elif choice == 5:
            back()
        else:
            print("Please select valid operation.")
            sleep(3)
            search_type()
    except ValueError:
        print("Please select valid operation.")
        sleep(3)
        search_type()

def search_id():
    print("\n")
    print("|||| Search by ID ||||\n")
    val = int(input("User ID: "))
    id = (val,)
    query = "select * from user_tab where user_id like '%s%'"
    point.execute(query,id)
    record = point.fetchall()
    print("Retriving Data...")
    sleep(1)
    print(len(record), " Users found!")
    sleep(1)
    for data in record:
        print("-------------------------------------")
        print("User ID: ", data[0])
        print("Username: ", data[1])
        print("Name: ", data[3])
        print("Mobile number: ", data[4])
        print("Email address: ", data[5])
        print("User Level: ", data[6])
        print("Current points: ", data[7])
        print("User password: ", data[2])
    print("Returning...")
    sleep(2)
    search_type()




def search_username():
    print("|||| Search by Username ||||\n")
    val = input("Username: ")
    name = (val,)
    query = "select * from user_tab where user_name like %s"
    point.execute(query, name)
    record = point.fetchall()
    print("Retriving Data...")
    sleep(1)
    print(len(record), " Users found!")
    sleep(1)
    for data in record:
        print("-------------------------------------")
        print("User ID: ", data[0])
        print("Username: ", data[1])
        print("Name: ", data[3])
        print("Mobile number: ", data[4])
        print("Email address: ", data[5])
        print("User Level: ", data[6])
        print("Current points: ", data[7])
        print("User password: ", data[2])
    print("Returning...")
    sleep(2)
    search_type()


def search_name():
    print("|||| Search by Name ||||\n")
    val = input("Name: ")
    name = (val,)
    query = "select * from user_tab where name like %s"
    point.execute(query, name)
    record = point.fetchall()
    print("Retriving Data...")
    sleep(1)
    print(len(record), " Users found!")
    sleep(1)
    for data in record:
        print("-------------------------------------")
        print("User ID: ", data[0])
        print("Username: ", data[1])
        print("Name: ", data[3])
        print("Mobile number: ", data[4])
        print("Email address: ", data[5])
        print("User Level: ", data[6])
        print("Current points: ", data[7])
        print("User password: ", data[2])
    print("Returning...")
    sleep(2)
    search_type()

def search_level():
    print("|||| Search by Level ||||\n")
    val = input("Level: ")
    lvl = (val,)
    query = "select * from user_tab where user_level = %s"
    point.execute(query, lvl)
    record = point.fetchall()
    print("Retriving Data...")
    sleep(1)
    print(len(record), " Users found!")
    sleep(1)
    for data in record:
        print("-------------------------------------")
        print("User ID: ", data[0])
        print("Username: ", data[1])
        print("Name: ", data[3])
        print("Mobile number: ", data[4])
        print("Email address: ", data[5])
        print("User Level: ", data[6])
        print("Current points: ", data[7])
        print("User password: ", data[2])
    print("Returning...")
    sleep(2)
    search_type()


def back():
    print("Returning back...")
    sleep(1)




