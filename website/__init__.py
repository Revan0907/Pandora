from flask import Flask
from flask_login import LoginManager
from flask_gtts import gtts

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret test key' 
gtts(app)

login_manager = LoginManager()
login_manager.init_app(app)

from website import routes
