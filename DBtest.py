import mysql.connector
from mysql.connector import Error

try:
    conn=mysql.connector.connect(host="localhost",database="AttendanceDB",user="root",password="root")
    if conn.is_connected():
        print("Connected")
except Error as e:
    print("Error while connecting to MySQL", e)
