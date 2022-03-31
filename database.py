import sqlite3
from sqlite3 import Error

#begin sql connection
def sql_connection():

    try:
        conDatabase = sqlite3.connect('data_app.db')
        return conDatabase

    except:
        print(Error)

#create 2 tables for customers and appointments
def sql_table(conDatabase):
    customer = conDatabase.cursor()
    customer.execute("CREATE TABLE IF NOT EXISTS customers("
                      "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                      "fname TEXT NOT NULL,"
                      "lname TEXT NOT NULL,"
                      "mobile INTEGER NOT NULL,"
                      "city TEXT,"
                      "email TEXT);")


    appointment = conDatabase.cursor()
    appointment.execute("CREATE TABLE IF NOT EXISTS appointments("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "time INTEGER NOT NULL,"
                        "day TEXT NOT NULL,"
                        "customer_id INTEGER,"
                        "FOREIGN KEY(customer_id) REFERENCES customers(id) ); ")
    conDatabase.commit()


def create_user(fname,lname,mobile,city,email):
    user_data=[fname, lname, mobile, city, email]
    conDatabase.execute('INSERT INTO customers(fname,lname,mobile,city,email) VALUES (?,?,?,?,?)', user_data)
    conDatabase.commit()

# def create_appointment(date,start_time,end_time)

conDatabase = sql_connection()
sql_table(conDatabase)
#insert_database(conDatabase)
