import os
from models import get_all_countries, get_country
from markupsafe import escape
from flask import Flask




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
        all_countries_string = get_all_countries()
        return all_countries_string
    
    @app.route('/<country>')
    def get_single_country(country):
        country_string = get_country(country)
        return country_string
    
    return app