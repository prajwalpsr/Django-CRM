import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    auth_plugin='mysql_native_password'
)

cursor_obj = database.cursor()

cursor_obj.execute("create database elderco")

print("successful!!!")