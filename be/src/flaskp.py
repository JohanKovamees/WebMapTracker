import os
from crud import get_all_countries, get_country, get_user, add_country_to_user, remove_country_from_user
from flask import Flask, request
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from login import login, register

meta = MetaData()
dbase_path = 'sqlite:///' + os.getcwd() + '/tables.db'
engine = create_engine(dbase_path)

session = sessionmaker()
session.configure(bind=engine)

with session() as s:

    def create_app(test_config=None):
        app = Flask(__name__, instance_relative_config=True)

        @app.route('/')
        def startpage():
            return 'StartPage'

        @app.route('/api/login', methods=['POST'])
        def login_web():

            user_json = request.json
            username = user_json["Username"]
            password = user_json["Password"]

            login_successful = login(username, password, s)
            if login_successful:
                return {
                    "Response" : "Login successful"
                }
            else:
                return {
                    "Response" : "Login unsuccessful"
                }

        @app.route('/api/register', methods=['POST'])
        def register_web():
            user_json = request.json
            username = user_json["username"]
            password = user_json["password"]

            register_successful = register(username, password, s)
            if register_successful:
                return {
                    "Response" : "Registration successful"
                }
            else:
                return {
                    "Response" : "Registration unsuccessful"
                }

        @app.route('/api/countries', methods=['GET'])
        def get_countries():
            all_countries_string = get_all_countries(s)
            return all_countries_string
        
        @app.route('/api/country/<country>', methods=['GET'])
        def get_single_country(country):
            country = get_country(country, s)
            return country.name
        
        @app.route('/api/user/<user>', methods=['GET'])
        def get_a_user(user):
            user_string = get_user(user,s)
            return user_string.name

        @app.route('/api/user/<user>/countries/<abb>', methods=['POST'])
        def add_country(user, abb):
            dict = request.json
            abb = dict["Country"]
            user = dict["User"]
            successful_add = add_country_to_user(user, abb, s)
            if successful_add:
                return {
                    "Response" : f"{abb} added to {user}"
                }
            else:
                return {
                    "Response" : "Failed to add"
                }

        '''@app.route('/user/<user>/countries', methods=['POST'])
        def add_country2(user):
            abb = "US"
            print(request.json)
            add_country_to_user(user, abb, s)
            return "Added " + abb + " to " + user'''

        @app.route('/api/user/<user>/countries/<abb>', methods=['DELETE'])
        def delete_country(user, abb):
            dict = request.json
            abb = dict["Country"]
            user = dict["User"]
            successful_remove = remove_country_from_user(user, abb, s)
            if successful_remove:
                return {
                    "Response" : f"{abb} removed from {user}"
                }
            else:
                return {
                    "Response" : "Failed to remove"
                }
        
        return app