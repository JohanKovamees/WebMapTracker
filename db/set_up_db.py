#!/usr/bin/env python3
import os
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from numpy import genfromtxt
import csv

meta = db.MetaData() 

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()


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
	name = db.Column(db.String)

Base.metadata.create_all(engine)

#r = Countries(id = 'sv', name = 'Sweden')
#s.add(r)


try:	
	'''file_name = 'countries.csv'
	data = Load_Data(file_name)'''

	file = open('countries.csv')
	read_file = csv.reader(file)
	header = []
	header = next(read_file)

	rows = []
	for row in read_file:
		record = Countries(id = row[0], name = row[1])
		rows.append(record)
	
	from collections import Counter
	counts = Counter([c.id for c in rows])
	#print(counts)
	s.bulk_save_objects(rows)
	file.close()

finally:
	
	s.commit()
	s.close()



