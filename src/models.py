import os
from sqlalchemy import Column, String, MetaData, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
dbase_path = 'sqlite:///' + os.getcwd() + '/tables.db'

'''class Association(Base):
    __tablename__ = 'association'
    Column("countries_id", ForeignKey("countries.id"), primary_key=True)
    Column("users_id", ForeignKey("users.id"), primary_key=True)
    extra_data = Column(String(5))
    countries = relationship("Countries", back_populates="users")
    users = relationship("Users", back_populates="countries")'''

relation = Table('relation', Base.metadata,
    Column('users_name', ForeignKey('users.name'), primary_key=True),
    Column('countries_abb', ForeignKey('countries.abb'), primary_key=True)
)

class Countries(Base):
    __tablename__ = 'countries'
    abb = Column(String, primary_key = True)
    name = Column(String)
    #users = relationship("Association", back_populates="countries")

    keywords = relationship('users',
        secondary=relation,
        back_populates='countries')

class Users(Base):
    __tablename__ = 'users'
    name = Column(String, primary_key = True)
    passwd = Column(String)
    #countries = relationship("Association", backref="users")
    keywords = relationship('countries',
        secondary=relation,
        back_populates='users')



def get_all_countries():
    meta = MetaData()
    engine = create_engine(dbase_path)
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
    meta = MetaData()
    engine = create_engine(dbase_path)
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    country_obj = s.query(Countries).get(country_name)
    country = "" + country_obj.name
    s.close()
    return country

def get_user(username):
    meta = MetaData()
    engine = create_engine(dbase_path)
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    user = s.query(Users).get(username)
    s.close()
    return user

def add_user(username,hashed_pass):
    meta = MetaData()
    engine = create_engine(dbase_path)
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    temp_user = Users(name = username, passwd = hashed_pass)
    try:
        s.query(Users).add(temp_user)
    except:
        print("User already exits")
        s.rollback()
    finally:
        s.commit()
        s.close()
    

if __name__ == "__main__":
    pass