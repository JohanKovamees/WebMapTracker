#!/usr/bin/env python3
import os
import sqlalchemy as db

engine = db.create_engine('sqlite:///tables.db')

#connection = engine.connect()
meta = db.MetaData() 

countries = db.Table(
	'countries', meta,
	db.Column('id', db.String, primary_key = True),
	db.Column('name', db.String)
)

users = db.Table(
	'users', meta,
	db.Column('id', db.String, primary_key = True),
	db.Column('name', db.String)
)

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()



Base = db.declarative_base()

class Countries(Base):
	id = db.Column(db.String, primary_key = True)
	name = db.Column(db.String)

data = Load_Data(countries.csv)

for i in data:
	record = 

meta.create_all(engine)


