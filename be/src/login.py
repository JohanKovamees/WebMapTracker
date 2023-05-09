from werkzeug.security import generate_password_hash, check_password_hash
from crud import get_user, add_user, check_user_exist


def register(username, password, s):
    exist_cond = check_user_exist(username, s)
    if exist_cond == True:
        print("Can't Register existing user")
        return False
    else:
        add_user(username, generate_password_hash(password), s)
        print("Added User")
        return True


def login(username, password, s):
    real_user = get_user(username, s)

    if real_user is None:
        print(f"User {username} not found.")
        return False

    check_password = check_password_hash(real_user.password, password)

    if check_password == True:
        print("Login successful")
        return True
    else:
        return False
