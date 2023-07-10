import random
import mysql.connector
from time import sleep
from Quiz_Book_proj.my_packs import take_quiz
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql123",
    auth_plugin='mysql_native_password'
)

point = mydb.cursor()
point.execute("use quiz_book;")


def quiz_home(id):
    print("\n")
    print("|||| Quiz Home ||||")
    print("\n")

    user_id = (id,)
    query = "select user_level from user_tab where user_id = %s"
    point.execute(query, user_id)
    rec = point.fetchall()
    # print(rec)
    for x in rec:
        user_lvl = x[0]
    sleep(1)
    print("1. Start Quiz for your Level.  (Recommended)")
    print("2. Start Quiz by Difficulty.")
    print("3. Back")
    try:
        ch = int(input("=> "))
        if ch == 1:
            take_quiz.quiz_begin(user_lvl, user_id)
        elif ch == 2:
            print("---- Select Difficulty ----")
            print("1. Beginner             2. Amateur          3. Comfortable")
            print("4. Professional         5. Master")
            choice = int(input("=> "))
            if (choice >= 1) and (choice <= 5):
                take_quiz.quiz_begin(choice, user_id)
            else:
                print("Invalid option.")
                sleep(1)
                print("Returning back...")
                sleep(1)
                quiz_home(id)
        elif ch == 3:
            print("Returning Home...")
            sleep(2)
        else:
            print("Please select Valid option!")
            sleep(1)
            quiz_home(id)
    except ValueError:
        print("Please select Valid option!")
        sleep(2)
        quiz_home(id)

