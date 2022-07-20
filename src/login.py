from werkzeug.security import generate_password_hash, check_password_hash
from crud import get_user, add_user, check_user_exist

def register(username, password, s):
        exist_cond = check_user_exist(username, s)
        if exist_cond == True:
            print("Can't Register existing user")
            return False
        else:
            add_user(username,generate_password_hash(password), s)
            print("Added User")
            return True



def login(username, password, s):
    real_user = get_user(username, s)
    check_password = check_password_hash(real_user.passwd, password)

    if real_user is None:
        return False
    if check_password == True:
        print("Login Successful")
        return True
    else:
        return False
