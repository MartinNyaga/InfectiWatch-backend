import os
from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()



app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)


CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
rest_api = Api(app)
jwt = JWTManager()
jwt.init_app(app)

from api import models
from api import routes

rest_api.add_namespace(routes.ns)