#!/usr/bin/env python3
from enum import unique
import os
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from numpy import genfromtxt
import csv
from collections import Counter

meta = db.MetaData() 

engine = db.create_engine('sqlite:///tables.db')
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
	name = db.Column(db.String, unique = True)
	passwd = db.Column(db.String)

Base.metadata.create_all(engine)

try:
	with open('countries.csv') as countries_file:
		read_file = csv.reader(countries_file)
		header = []
		header = next(read_file)

		rows = []
		for row in read_file:
			record = Countries(id = row[0], name = row[1])
			rows.append(record)
		
		counts = Counter([c.id for c in rows])
		s.bulk_save_objects(rows)

finally:
	s.commit()
	s.close()
