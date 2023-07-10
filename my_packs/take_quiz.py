import mysql.connector
from Quiz_Book_proj.my_packs import quiz_homepage
from time import sleep
import random
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql123",
    auth_plugin='mysql_native_password'
)
point = mydb.cursor()
point.execute("use quiz_book;")


def get_ans():
    ur_answer1 = int(input("Select your Option => "))
    if (ur_answer1 >= 1) and (ur_answer1 <= 4):
        # print("inside function ur ans: ", ur_answer1)
        return int(ur_answer1)
    else:
        print("Please select valid option!")
        get_ans()


def quiz_begin(choice, user_id):
    print(user_id)
    # print(choice)
    q_lvl = (choice,)
    query = "select q_id from quiz where q_lvl = %s"
    point.execute(query, q_lvl)
    record = point.fetchall()
    list2 = []
    for x in record:
        list2.append(x[0])
    random_list = random.sample(list2, 11)
    q_list = []
    opt_list = []
    # print(list2)
    for x in range(10):
        q_id = ((random_list[x]),)
        query = "select q_ques from quiz where q_id = %s"
        point.execute(query, q_id)
        rec = point.fetchall()
        q_list.append(rec)
        quer = "select q_opt1, q_opt2, q_opt3, q_opt4 from quiz where q_id = %s"
        point.execute(quer, q_id)
        opt_record = point.fetchall()
        opt_list.append(opt_record)
    # print(q_list)
    # print(opt_list)
    ans_list = []
    for x in range(10):
        query = "select q_ans from quiz where q_id = %s"
        q_id = ((random_list[x]),)
        point.execute(query, q_id)
        rec = point.fetchall()
        for x in rec:
            ans_list.append(x[0])
    # print(ans_list)
    count = 0
    ur_ans_list = []
    for y in q_list:
        z = y[0]
        count = count + 1
        print("\n", count, ". Question: ", z[0])
        for a in opt_list[count - 1]:
            # z = a[0]
            print("\n Option 1: ", a[0], "\n Option 2: ", a[1], "\n Option 3: ", a[2], "\n Option 4: ", a[3])
            ur_answer = int(input("Select your Option => "))
            if (ur_answer >= 1) and (ur_answer <= 4):
                ur_ans_list.append(a[ur_answer - 1])
            else:
                print("Please select valid option!", get_ans())
                # get_ans()
                ur_answer = get_ans()

                # print(ur_answer)
                ur_ans_list.append(a[ur_answer - 1])
    # print(ur_ans_list)
    # print(ans_list)
    print("Calcultaing Result...")
    sleep(1)
    mark = 0
    for x in range(10):
        if ur_ans_list[x] == ans_list[x]:
            print("\n   Question ", x + 1)
            print("Selected Answer: ", ur_ans_list[x])
            print("Correct Answer : ", ans_list[x])
            print("Marks Earned   : 10")
            mark = mark + 10
        else:
            print("\n   Question ", x + 1)
            print("Selected Answer: ", ur_ans_list[x])
            print("Correct Answer : ", ans_list[x])
            print("Marks Earned   : 0")
    print(mark)
    if mark >= 70:
        print("\n\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!! Congratulations, You have passed !!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("\n\nTotal Questions: 10")
        print("Answered Correctly : ", mark // 10)
        print("Mistaken           : ", (100 - mark) // 10)
        print("Total Marks        : ", mark)
        print("\n\n Overall points earned: ", choice)
        # user_id = (user_id,)
        query = "select points from user_tab where user_id = %s"
        point.execute(query, user_id)
        record = point.fetchall()
        for values in record:
            rec = (values[0] + choice)
            print("Current Profile Points: ", rec)
        p = (rec,)
        q = "update user_tab set points = %s where user_id = %s "
        values = (p[0], user_id[0])
        point.execute(q, values)
        mydb.commit()
        if (rec >= 0) and (rec <= 20):
            q1 = "update user_tab set user_level = 1 where user_id = %s"
            point.execute(q1, user_id)
            mydb.commit()
        elif (rec >= 21) and (rec <= 40):
            q1 = "update user_tab set user_level = 2 where user_id = %s"
            point.execute(q1, user_id)
            mydb.commit()
        elif (rec >= 41) and (rec <= 60):
            q1 = "update user_tab set user_level = 3 where user_id = %s"
            point.execute(q1, user_id)
            mydb.commit()
        elif (rec >= 61) and (rec <= 80):
            q1 = "update user_tab set user_level = 4 where user_id = %s"
            point.execute(q1, user_id)
            mydb.commit()
        elif (rec >= 81) and (rec <= 100):
            q1 = "update user_tab set user_level = 5 where user_id = %s"
            point.execute(q1, user_id)
            mydb.commit()
        elif (rec > 100):
            q1 = "update user_tab set user_level = 6 where user_id = %s"
            point.execute(q1, user_id)
            mydb.commit()

        sleep(4)

        print("1. Take another Quiz    2. Back")
        ch = int(input("=> "))
        if ch == 1:
            quiz_homepage.quiz_home(id)
        elif ch == 2:
            print("Returning Back...")
            sleep(3)
        else:
            print("Invalid option. Returning back to Homepage...")
            sleep(3)
    else:
        print("\n|||| You have failed the Quiz. Please try again... |||")
        print("\n\nTotal Questions: 10")
        print("Answered Correctly : ", mark // 10)
        print("Mistaken           : ", (100 - mark) // 10)
        print("Total Marks        : ", mark)
        print("\n Overall points earned: 0")
        sleep(3)
        print("1. Take another Quiz    2. Back")
        ch = int(input("=> "))
        if ch == 1:
            quiz_homepage.quiz_home(id)
        elif ch == 2:
            print("Returning Back...")
            sleep(3)
        else:
            print("Invalid option. Returning back to Homepage...")
            sleep(3)



