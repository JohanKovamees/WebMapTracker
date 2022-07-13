import functools
import sqlalchemy as dbase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from db.set_up_db import Users

bp = Blueprint('login', __name__, url_prefix='/login')