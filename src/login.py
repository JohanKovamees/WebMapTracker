import functools
import os
import sqlalchemy as dbase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .models import Users

bp = Blueprint('login', __name__, url_prefix='/login')
Base = declarative_base()

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        temp_u = Users(name = username, passwd = generate_password_hash(password))
    	
        dbase_path = 'sqlite:///' + os.getcwd() + '/db/tables.db'
        meta = dbase.MetaData()
        engine = dbase.create_engine(dbase_path)
	
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                s.add(temp_u)
                s.commit()
                s.close()
            except dbase.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
       
        alleged_u = Users(name = username, passwd = generate_password_hash(password))
    	
        dbase_path = 'sqlite:///' + os.getcwd() + '/db/tables.db'
        meta = dbase.MetaData()
        engine = dbase.create_engine(dbase_path)
	
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()

        try:
            s.get(alleged_u)
        except:
            pass
        finally:
            return redirect(url_for('index'))

    return render_template('auth/login.html')