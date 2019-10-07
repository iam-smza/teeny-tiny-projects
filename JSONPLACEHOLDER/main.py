# coding=utf-8

# Original date: 4-Oct-2019
# Last Updated: 7-Oct-2019 * File will be updated Weekly
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
# 2. Make it so it uses Protocol Oriented Capabilities as provided by Python
#

import json
import sqlite3

import requests

# initialize connection with the database
db = sqlite3.connect('user.sqlite')
handle = db.cursor()

# make a table in the database
handle.execute('DROP TABLE IF EXISTS Users')
handle.execute(
    'CREATE TABLE Users (no INTEGER, id INTEGER, title TEXT,body TEXT)')

# connect to the JSONPLACEHOLDER API and get a response object
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# parse the response object from the JSONPLACEHOLDER API using methods
posts = json.loads(response.text)

# we get a list of dictionaries of user_data from the API
# we need to extract the data from the lists and dictionaries

for user in posts:
    uid = user['userId']
    no = user['id']
    title = user['title']
    body = user['body']
    handle.execute(
        'INSERT INTO Users (no, id, title, body) VALUES (?, ?, ?, ?)',
        (uid, no, title, body))
    db.commit()

print('...')
print('User data copied to the database.')
print('...')

# showing the contents of the database by selecting the required fields
handle.execute('SELECT no, id, title, body FROM Users')
print('---DATABASE START---')
for row in handle:
    print(row)
print('---DATABASE END---')

# closing the database
db.close()
