import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sql123",
    auth_plugin='mysql_native_password'
)

point = mydb.cursor()
point.execute("use quiz_book;")

def signup():
    user_name = input("User name: ")
    name = input("Name: ")
    password = input("Password: ")
    re_type = input("Re-type Password: ")
    mobile = input("Mobile: ")
    mail = input("Mail address: ")
    user_level = 1
    if password == re_type:
        point.execute("select max(user_id) from user_tab")
        value = point.fetchall()
        for i in value:
            max_id = i[0]
        user_id = max_id
    query = "insert into user_tab (`user_id`,`user_name`,`password`,`name`,`mobile`,`mail`,`user_level`) Values(%s,%s,%s,%s,%s,%s,%s);"
    in_values = (user_id, user_name, password, name, mobile, mail, user_level)
    point.execute(query, in_values)


