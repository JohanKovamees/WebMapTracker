import os
import ssl
from crud import get_all_countries, get_country, get_user, add_country_to_user, remove_country_from_user
from flask import Flask, request, jsonify
from sqlalchemy import MetaData, create_engine
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from login import login, register
from flask_cors import CORS

@contextmanager
def create_session():
    session = sessionmaker(bind=engine)()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()



meta = MetaData()
dbase_path = 'sqlite:///' + os.getcwd() + '/tables.db'
engine = create_engine(dbase_path)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    @app.route('/')
    def startpage():
        return 'StartPage'

    @app.route('/api/login', methods=['POST'])
    def login_web():
        print("Inside login")
        user_json = request.json
        username = user_json["username"]
        password = user_json["password"]

        with create_session() as session:
            login_successful = login(username, password, session)
        
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
        print("Inside register")
        user_json = request.json
        username = user_json["username"]
        password = user_json["password"]

        with create_session() as session:
            register_successful = register(username, password, session)
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
        with create_session() as session:
            all_countries_string = get_all_countries(session)
        return all_countries_string
    
    @app.route('/api/country/<country>', methods=['GET'])
    def get_single_country(country):
        with create_session() as session:
            country = get_country(country, session)
        return country.name
    
    @app.route('/api/user/<user>', methods=['GET'])
    def get_a_user(user):
        print("Inside get_a_user")
        with create_session() as session:
            user_string = get_user(user, session)
        return user_string.name

    @app.route('/api/user/<user>/countries/<abb>', methods=['POST'])
    def add_country(user, abb):
        print("Inside add_country")
        dict = request.json
        abb = dict["Country"]
        user = dict["User"]
        with create_session() as session:
            successful_add = add_country_to_user(user, abb, session)
        if successful_add:
            return {
                "Response" : f"{abb} added to {user}"
            }
        else:
            return {
                "Response" : "Failed to add"
            }


    @app.route('/api/map-data', methods=['GET'])
    def map_data():
        print("Inside map-data")
        username = request.args.get('username')
        if not username:
            return jsonify({"Error": "Missing username parameter"}), 400

        with create_session() as session:
            user = get_user(username, session)
        if not user:
            return jsonify({"Error": "User not found"}), 404

        visited_countries = [country.abb for country in user.countries]
        return jsonify({"visitedCountries": visited_countries})

    @app.route('/api/user/<user>/countries/<abb>', methods=['DELETE'])
    def delete_country(user, abb):
        print("Inside delete_country")
        dict = request.json
        abb = dict["Country"]
        user = dict["User"]
        with create_session() as session:
            successful_remove = remove_country_from_user(user, abb, session)
        if successful_remove:
            return {
                "Response" : f"{abb} removed from {user}"
            }
        else:
            return {
                "Response" : "Failed to remove"
            }
    
    return app

if __name__ == '__main__':
    app = create_app()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    app.run(host='0.0.0.0', port=5000, ssl_context=context)