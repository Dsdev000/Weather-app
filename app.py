from datetime import datetime
import requests
import json
from flask import Flask , render_template ,flash , redirect , url_for , session , request ,logging , abort ,jsonify , make_response , Response
from flask_wtf.file import FileField , FileAllowed , FileRequired 
from wtforms import Form , StringField , TextAreaField , PasswordField , validators
from passlib.hash import sha256_crypt


app=Flask(__name__)


# app.config.from_pyfile('config.py')

from views import *

if __name__=='__main__':
    app.run(debug = True)
