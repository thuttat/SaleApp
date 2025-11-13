from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'iqiwqu3e735ehwsnsio274687928u'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:anhthu@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)