import os
from crud import get_all_countries, get_country, get_user, add_country_to_user, remove_country_from_user, check_if_visited
from markupsafe import escape
from flask import Flask
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

        '''@app.route('/<user_id>')
        def show_user_profile(user_id):
            # show the user id for that user
            return f'User {escape(user_id)}'''

        @app.route('/login')
        def login():
            #app.register_blueprint(login.bp)      
            return "this is under construction" 

        @app.route('/countries')
        def get_countries():
            all_countries_string = get_all_countries(s)
            return all_countries_string
        
        @app.route('/country/<country>')
        def get_single_country(country):
            country_string = get_country(country,s)
            return country_string.name
        
        @app.route('/user/<user>')
        def get_a_user(user):
            user_string = get_user(user,s)
            return user_string.name

        @app.route('/user/<user>/<abb>')
        def add_country(user, abb):
            check = check_if_visited(user, abb, s)
            if check == True:
                remove_country_from_user(user, abb, s)
                return "Removed " + abb + " from " + user
            else:
                add_country_to_user(user, abb, s)
                return "Added " + abb + " to " + user
        
        return app