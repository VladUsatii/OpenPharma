from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.url_map.strict_slashes = False
	app.config['SECRET_KEY'] = '\x9d\xb641x\xf1\x11\x97\r\x80\xe3\x12"FW\x9ec,\xae7\xf9b\xc5g'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	from .models import User
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))


	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
