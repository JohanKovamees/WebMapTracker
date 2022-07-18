from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from models import Users
from crud import get_country, get_user, add_user

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:

                add_user(username,generate_password_hash(password))
                error = f"User {username} is already registered."
                return redirect(url_for("auth.login"))
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        alleged_u = Users(name = username, passwd = generate_password_hash(password))


        return redirect(url_for('index'))

    return render_template('auth/login.html')