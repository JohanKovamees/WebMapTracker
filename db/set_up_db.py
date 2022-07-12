#!/usr/bin/env python3
import os
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from numpy import genfromtxt

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



Base = declarative_base()
session = sessionmaker()
session.configure(bind=engine)
s = session()

class Countries(Base):
	__tablename__ = 'countries'
	id = db.Column(db.String, primary_key = True)
	name = db.Column(db.String)

class Users(Base):
	__tablename__ = 'users'
	id = db.Column(db.String, primary_key = True)
	name = db.Column(db.String)

try:
	data = Load_Data(countries.csv)

	for i in data:
		record = Countries(**{
			'id' : i[0],
			'name' : i[1]
		})
		s.add(record)
finally:
	s.close()

meta.create_all(engine)