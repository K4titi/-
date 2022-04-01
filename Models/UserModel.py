from database import *


def create_user(fname, lname, mobile, city, email):
    user_data = [fname, lname, mobile, city, email]
    conDatabase.execute('INSERT INTO customers(fname,lname,mobile,city,email) VALUES (?,?,?,?,?)', user_data)
    conDatabase.commit()
