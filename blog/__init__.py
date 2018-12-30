from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db?check_same_thread=False'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # for login_manager to know where login is located
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'da32.domeny.com'  # 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USR_TLS'] = True
app.config['MAIL_USERNAME'] = 'mariusz@artemlux.com'  # os.environ.get('EMAIL_USER')

file = open("oauth.txt", "r")
id = file.read()
file.close()

app.config['MAIL_PASSWORD'] = id  # os.environ.get('EMAIL_PASS')
mail = Mail(app)

from blog import routes
