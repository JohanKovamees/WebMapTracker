#!/usr/bin/env python3

import sqlite3
from numpy import genfromtxt

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_db(db):
    with sqlite3.connect(db) as connection:
        connection.row_factory = dict_factory
        connection.text_factory = str

        cursor = connection.cursor()
        cursor.execute("CREATE TABLE [COUNTRIES] ([id] INTEGER PRIMARY KEY NOT NULL UNIQUE, [short] TEXT, [name] TEXT);")

def Add_Record(db, data):
    #Insert record into table
    with sqlite3.connect(db) as connection:
        connection.row_factory = dict_factory
        connection.text_factory = str

        cursor = connection.cursor()

        cursor.execute("INSERT INTO COUNTRIES({cols}) VALUES({vals});".format(cols = str(data.keys()).strip('[]'), 
                    vals=str([data[i] for i in data]).strip('[]')
                    ))


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', converters={0: lambda s: str(s)})
    return data.tolist()


db = 'tables.db'
file_name = "countries.csv"

data = Load_Data(file_name)

create_db(db) #Create DB

    #For every record, format and insert to table
for i in data:
    record = {
            'short' : i[0],
            'name' : i[1]
            }
Add_Record(db, record)