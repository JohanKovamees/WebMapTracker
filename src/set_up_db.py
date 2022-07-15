#!/usr/bin/env python3
import os
from sqlalchemy import Column, String, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv
from collections import Counter
from models import Countries,Users,Association,Base




if __name__ == '__main__':
	meta = MetaData()
	dbase_path = 'sqlite:///' + os.getcwd() + '/tables.db'
	engine = create_engine(dbase_path)
	
	session = sessionmaker()
	session.configure(bind=engine)
	s = session()

	Base.metadata.create_all(engine)
	file_path = os.getcwd() + '/countries.csv'

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
	except:
		#s.rollback()
		pass

	finally:
		s.commit()
		s.close()
