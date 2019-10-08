# coding=utf-8

# Original date: 4-Oct-2019
# Last Updated: 8-Oct-2019 * File will be updated Weekly
# Maintainer: Zamran Ali
# Github: https://www.github.com/iam-smza/
#
# OBJECTIVE ->
# Use a Dummy API with rich user data and download data (GET AND POST methods)
# to a database
#
# API: JSONPLACEHOLDER, DATABASE TECHNOLOGY: SQLITE v.3
#
# What's Working:
# 1.GET method works and the user data is loaded and feeded off into the db

# What's not Working:
# 1. POST method which needs a server that can send and receive data
#
# Plans for Next Iteration:
# 1. Create a custom server to use the POST method to make changes in the db
# 2. Make it so that it uses Protocol Oriented Capabilities provided by Python
#

import json
import sqlite3

import requests


def set_up_database(db_name, val_var):
    db = sqlite3.connect(f'{db_name}.sqlite')
    handle = db.cursor()

    handle.execute(f'DROP TABLE IF EXISTS {db_name.title()}')
    handle.execute(f'CREATE TABLE {db_name.title()} {val_var}')
    return db, handle


def add_data_in_database(db, handle, db_name, data_tuple):
    handle.execute(f'INSERT INTO {db_name.title()} VALUES (?, ?, ?, ?)',
                   data_tuple)
    db.commit()


def show_data_in_database(handle, db_name):
    handle.execute(f'SELECT no, uid, title, body FROM {db_name.title()}')
    print('---DATABASE START---')
    for row in handle:
        print(row)
    print('---DATABASE END---')


def get_js_response(uri):
    response = requests.get(uri)
    data_obj = json.loads(response.text)
    return data_obj


# setting up the databse name and type of values
my_db_name = 'users'
type_of_values = '(no INTEGER, uid INTEGER, title TEXT, body TEXT)'

# passing the name and values to make databse
db_conn, db_handle = set_up_database(my_db_name, type_of_values)

# getting the data from the jsonplaceholder and saving it into a container
URI = 'https://jsonplaceholder.typicode.com/posts'
posts = get_js_response(URI)

# looping through the data in the container to get values
for user in posts:
    uid = user['userId']
    no = user['id']
    title = user['title']
    body = user['body']
    # making a tuple so that the data values can be passed to database
    user_tuple = (uid, no, title, body)
    add_data_in_database(db_conn, db_handle, my_db_name, user_tuple)

# confirming the user data is indeed added into the database
show_data_in_database(db_handle, my_db_name)

# closing the database
db_conn.close()
