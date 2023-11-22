import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# membuat instance aplikasi Connexion
connex_app = connexion.App(__name__, specification_dir=basedir)

# mencari aplikasi turunan flask
app = connex_app.app

# konfigurasi sql alchemy untuk driver yang akan digunakan (disesuaikan dengan database yang digunakan)
app.config["SQLALCHEMY_ECHO"] = True
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://username:password@localhost/python-milestone"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# membuat variable untuk database alchemy

db = SQLAlchemy(app)

# inisialisasi marsmallow

ma = Marshmallow(app)
