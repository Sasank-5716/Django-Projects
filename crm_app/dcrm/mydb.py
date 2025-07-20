import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sasank07",
    database="sasank"
)

# prepare a cursor object using the cursor() method
cursorObject = database.cursor()

#create database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS sasank")


print("Database created successfully")