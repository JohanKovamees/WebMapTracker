#from ast import Delete
import os
from crud import get_all_countries, get_country, get_user, add_country_to_user, remove_country_from_user, check_if_visited
#from markupsafe import escape
from flask import Flask, request
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

meta = MetaData()
dbase_path = 'sqlite:///' + os.getcwd() + '/tables.db'
engine = create_engine(dbase_path)

session = sessionmaker()
session.configure(bind=engine)

with session() as s:

    def create_app(test_config=None):
        # create and configure the app
        app = Flask(__name__, instance_relative_config=True)
        '''app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, '/db/tables.db'),
        )'''


        @app.route('/')
        def startpage():
            return '''Here there startpage will be. This is where login and account creation will be. 
            Make a simple login page with a quick way to create an account, probably generate account first.'''

        @app.route('/login')
        def login():
    
            return "this is under construction" 

        @app.route('/countries', methods=['GET'])
        def get_countries():
            all_countries_string = get_all_countries(s)
            return all_countries_string
        
        @app.route('/country/<country>', methods=['GET'])
        def get_single_country(country):
            country = get_country(country, s)
            return country.name
        
        @app.route('/user/<user>', methods=['GET'])
        def get_a_user(user):
            user_string = get_user(user,s)
            return user_string.name

        @app.route('/user/<user>/countries/<abb>', methods=['POST'])
        def add_country(user, abb):
            add_country_to_user(user, abb, s)
            return "Added " + abb + " to " + user

        @app.route('/user/<user>/countries/<abb>', methods=['DELETE'])
        def delete_country(user, abb):
            remove_country_from_user(user, abb, s)
            return "Removed " + abb + " from " + user
        
        return app