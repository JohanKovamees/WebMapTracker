from flask import request
from werkzeug.security import generate_password_hash
from models import Users
from crud import get_user, add_user, check_user_exist

#bp = Blueprint('login', __name__, url_prefix='/login')

#@bp.route('/register', methods=('GET', 'POST'))
def register(s):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exist_cond = check_user_exist(username, s)

        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif exist_cond:
            error = "User already exists"
        if error is None:
                add_user(username,generate_password_hash(password))

                '''error = f"User {username} is already registered."
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')'''

#@bp.route('/login', methods=('GET', 'POST'))
def login(s):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exist_cond = check_user_exist(username, s)
        alleged_user = Users(name = username, passwd = generate_password_hash(password))
        if exist_cond:
            real_user = get_user(username, s)
        if real_user == alleged_user:
            return True
        else:
            return False


        
        

        #return redirect(url_for('index'))
    #return render_template('auth/login.html')