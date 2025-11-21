from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, LoginManager

app = Flask(__name__)
app.secret_key = 'iqiwqu3e735ehwsnsio274687928dhgtu'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:anhthu@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"]=3

db = SQLAlchemy(app=app)
login = LoginManager(app=app)