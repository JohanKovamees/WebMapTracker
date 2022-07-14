from calendar import c
import os
#from select import select
import sqlalchemy as dbase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
dbase_path = 'sqlite:///' + os.getcwd() + '/tables.db'


class Countries(Base):
	__tablename__ = 'countries'
	abb = dbase.Column(dbase.String)
	name = dbase.Column(dbase.String, primary_key = True)

class Users(Base):
	__tablename__ = 'users'
	name = dbase.Column(dbase.String, primary_key = True)
	passwd = dbase.Column(dbase.String)

def get_all_countries():
    meta = dbase.MetaData()
    engine = dbase.create_engine(dbase_path)
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    country_list = s.query(Countries).all()
    c = ""
    s.close()
    for i in country_list:
        c += i.name + "|" + i.abb + ", "
    return c

def get_country(country_name):
    meta = dbase.MetaData()
    engine = dbase.create_engine(dbase_path)
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    country = s.query(Countries).get(country_name)
    c = "" + country.name
    s.close()
    return c

if __name__ == "__main__":
    pass