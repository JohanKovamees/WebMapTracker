import os
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
dbase_path = "sqlite:///" + os.getcwd() + "/tables.db"

user_visited_countries = Table(
    "user_visited_countries",
    Base.metadata,
    Column("users_name", ForeignKey("users.name"), primary_key=True),
    Column("countries_abb", ForeignKey("countries.abb"), primary_key=True),
)


class Countries(Base):
    __tablename__ = "countries"
    abb = Column(String, primary_key=True)
    name = Column(String)

    users = relationship(
        "Users", secondary=user_visited_countries, back_populates="countries"
    )


class Users(Base):
    __tablename__ = "users"
    name = Column(String, primary_key=True)
    password = Column(String)

    countries = relationship(
        "Countries", secondary=user_visited_countries, back_populates="users"
    )
