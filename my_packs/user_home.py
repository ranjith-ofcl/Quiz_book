import mysql.connector
from time import sleep
from Quiz_Book_proj.my_packs import quiz_homepage

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql123",
    auth_plugin='mysql_native_password'
)
point = mydb.cursor()
point.execute("use quiz_book;")

def user_home_start(id):
    query = "select name from user_tab where user_id = %s"
    user_id = (id,)
    point.execute(query, user_id)
    record = point.fetchall()
    for x in record:
        name = x[0]
    print("\n")
    print("---------------------")
    print("|  Welcome", name, " |")
    print("---------------------")
    features(id)


def features(id):
    print("\nSelect Operation you want to Perform, ")
    print("1. Profile          2. Take Quiz")
    print("3. Logout           4. Instructions")
    try:
        choice = int(input("=> "))
        if choice == 1:
            user_profile(id)
        elif choice == 2:
            quiz_homepage.quiz_home(id)
            features(id)
        elif choice == 3:
            mydb.close()
            exit()
        elif choice == 4:
            instructions()
        else:
            print("Please select valid operation.")
            sleep(3)
            features()
    except ValueError:
        print("Please select valid operation.")
        sleep(3)
        features(id)


def user_profile(id):
    print("\n")
    print("|||| Your Profile ||||")
    sleep(3)
    user_id = (id,)
    query = "select * from user_tab where user_id = %s;"
    point.execute(query, user_id)
    record = point.fetchall()
    for data in record:
        print("-------------------------------------")
        print("User ID: ", data[0])
        print("Username: ", data[1])
        print("Name: ", data[3])
        print("Mobile number: ", data[4])
        print("Email address: ", data[5])
        print("Level: ", data[6])
        print("Current points: ", data[7])
        print("password: ", data[2])
        print("-------------------------------------")
    print("\n Returning to User Operations...")
    sleep(2)
    features(id)


def instructions():
    print("\n")
    print("|||| Instructions ||||")
    print("\n")
    print("1. User Instructions    2. Quiz Instructions")
    try:
        choice = int(input("=> "))
        if choice == 1:
            user_ins()
        elif choice ==2 :
            quiz_ins()
        else    :
            print("Please select valid option.")
            sleep(2)
    except ValueError:
        print("Please select valid option.")
        sleep(2)

def user_ins():
    print("\n")
    print("|||| USER INSTRUCTIONS ||||")
    print("\n")
    print("1. User can visit their Profile to check their points, level and personal information.")
    print("2. Any changes if required in personal information, user should reach Administrator.")
    print("3. To update password, user should reach Administrator.")
    print("4. User will get 0 points at the beginning of the journey.")
    print("5. User will be at Level 1 at the beginning of the journey")
    print("6. Points can be obtained as below, ")
    print("           * Level 1 Quiz    -> 1 Point")
    print("           * Level 2 Quiz    -> 2 Point")
    print("           * Level 3 Quiz    -> 3 Point")
    print("           * Level 4 Quiz    -> 4 Point")
    print("           * Level 5 Quiz    -> 5 Point")
    print("7. Level can be obtained as below, ")
    print("           * Points  0-20   -> Level 1")
    print("           * Points 21-40   -> Level 2")
    print("           * Points 41-60   -> Level 3")
    print("           * Points 61-80   -> Level 4")
    print("           * Points 81-100  -> Level 5")
    print("           * Points 100 or above   -> Mastered")
    print("1. Back")
    try:
        ch = int(input("=> "))
        if ch == 1:
            print("Returning Home...")
            sleep(2)
            features(id)
        else:
            print("Invalid option. Returning home anyways...")
            sleep(2)
            features()
    except ValueError:
        print("Invalid option. Returning home anyways...")
        sleep(2)
        features()




def quiz_ins():
    print("\n")
    print("|||| QUIZ INSTRUCTIONS ||||")
    print("\n")
    print("1. There are five level of Quiz.")
    print("          * Level 1")
    print("          * Level 2")
    print("          * Level 3")
    print("          * Level 4")
    print("          * Level 5")
    print("2. Each level of Quiz will be harder as it increasing.")
    print("3. Quiz levels will be categorized as below in Quiz page.")
    print("          * Level 1   -> Beginner")
    print("          * Level 2   -> Amateur")
    print("          * Level 3   -> Comfortable")
    print("          * Level 4   -> Professional")
    print("          * Level 5   -> Master")
    print("4. Points can be obtained as below, ")
    print("          * Level 1 Quiz    -> 1 Point")
    print("          * Level 2 Quiz    -> 2 Point")
    print("          * Level 3 Quiz    -> 3 Point")
    print("          * Level 4 Quiz    -> 4 Point")
    print("          * Level 5 Quiz    -> 5 Point")
    print("5. Every Quiz will have 10 Questions.")
    print("6. Each Questions will take 10 marks, as the one total Quiz will have 100 marks.")
    print("7. Getting 70 or above mark is a Successful Quiz. ")
    print("8. Successfully Quiz will give you points to your profile, based on the Quiz Level.")
    print("1. Back")
    try:
        ch = int(input("=> "))
        if ch == 1:
            print("Returning Home...")
            sleep(2)
            features(id)
        else:
            print("Invalid option. Returning home anyways...")
            sleep(2)
            features()
    except ValueError:
        print("Invalid option. Returning home anyways...")
        sleep(2)
        features()




