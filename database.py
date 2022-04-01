import sqlite3
from sqlite3 import Error


# begin sql connection
def sql_connection():
    try:
        conDatabase = sqlite3.connect('data_app.db')
        return conDatabase

    except:
        print(Error)


# def create_appointment(date,start_time,end_time)

conDatabase = sql_connection()
