#!/usr/bin/env python3
from enum import unique
import os
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from numpy import genfromtxt
import csv
from collections import Counter

Base = declarative_base()
class Countries(Base):
	__tablename__ = 'countries'
	abb = db.Column(db.String, primary_key = True)
	name = db.Column(db.String)

class Users(Base):
	__tablename__ = 'users'
	id = db.Column(db.String, primary_key = True)
	name = db.Column(db.String, unique = True)
	passwd = db.Column(db.String)

if __name__ == '__main__':
	meta = db.MetaData()
	db_path = 'sqlite:///' + os.getcwd() + '/db/tables.db'

	engine = db.create_engine(db_path)
	
	session = sessionmaker()
	session.configure(bind=engine)
	s = session()

	Base.metadata.create_all(engine)
	file_path = os.getcwd() + '/db/countries.csv'

	try:
		with open(file_path) as countries_file:
			read_file = csv.reader(countries_file)
			header = []
			header = next(read_file)

			rows = []
			for row in read_file:
				record = Countries(abb = row[0], name = row[1])
				rows.append(record)
			
			counts = Counter([c.abb for c in rows])
			s.bulk_save_objects(rows)
	#except:
	#	s.rollback()
	#	pass

	finally:
		s.commit()
		s.close()
