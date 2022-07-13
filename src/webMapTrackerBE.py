import sqlalchemy as db 
import random
import string
from db.set_up_db import Users

def genId():
    r = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(32)])
    return r

def addUser(userName):
    id = genId()
    temp_user = Users(id = genId(), name = userName)


