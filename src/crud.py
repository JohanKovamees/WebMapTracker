from ast import Break

from sqlalchemy import true
from models import Countries, Users

def get_all_countries(s):
    country_list = s.query(Countries).all()
    str:c = ""
    for i in country_list:
        c += i.name + "|" + i.abb + ", "
    return c

def get_country(abb, s):
    country_obj = s.query(Countries).get(abb)
    return country_obj

def get_user(username, s):
    try:
        user = s.query(Users).get(username)
    except:
        print("Couldn't get user")
    return user

def add_user(username, hashed_pass, s):
    temp_user = Users(name = username, passwd = hashed_pass)
    try:
        s.add(temp_user)
    except:
        print("User already exists")
    s.commit()

def add_country_to_user(username, abb, s):
    user_t = get_user(username,s)
    country_t = get_country(abb,s)
    try:
        user_t.countries.append(country_t)
    finally:
        s.commit()

def remove_country_from_user(username, abb, s): 
    user = get_user(username, s)
    temp_list = user.countries
    temp_list = [c for c in temp_list if c.abb != abb]
    user.countries = temp_list
    s.add(user)
    s.commit()

def check_if_visited(username, abb, s):
    user = get_user(username, s)
    list_of_visited_countries = user.countries
    for c in list_of_visited_countries:
        if c.abb == abb:
            return True
        else:
            return False


if __name__ == "__main__":
    pass