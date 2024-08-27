import logging
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_username = os.environ.get("DB_USERNAME", "postgres")
db_password = os.environ.get("DB_PASSWORD", "postgres")
db_host = os.environ.get("DB_HOST", "host.docker.internal")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "mydb")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

db = SQLAlchemy(app)

app.logger.setLevel(logging.DEBUG)