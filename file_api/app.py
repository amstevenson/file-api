from flask import Flask
import sqlite3

# register_logging()
app = Flask(__name__)
app.config.from_pyfile("config.py")
