#importing required libraries
from flask import Flask,Blueprint,session
from flask_session import Session
from flask import render_template,render_template_string
from flask import flash

from werkzeug.exceptions import abort

import os
import sys

from dotenv import load_dotenv
load_dotenv()

def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True)
   
    #configuration the session
    app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
    app.config['API_KEY']=os.getenv('API_KEY')
    app.config['SESSION_TYPE']=os.getenv('SESSION_TYPE')
    app.config['SESSION_PERMANENT']=os.getenv('SESSION_PERMANENT')

    if test_config is None:
        #load the instance config,if it exists,when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        #load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    os.makedirs(app.instance_path,exist_ok=True)

    #importing blueprint
    from api.iteration import iterBp
    #registering blueprint
    app.register_blueprint(iterBp)
    
    Session(app)
    return app

