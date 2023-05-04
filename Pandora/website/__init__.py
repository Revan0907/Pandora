from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret test key' 

login_manager = LoginManager()
login_manager.init_app(app)

from website import routes
