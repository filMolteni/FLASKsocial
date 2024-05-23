from flask import Flask
from DatabaseManager import DatabaseManager
from PageManager import PageManager
import os

def create_app():
    app = Flask(__name__)

    
    secret_key = os.urandom(24).hex()

    
    app.config['SECRET_KEY'] = secret_key
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'db_social'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    
    db_manager = DatabaseManager(app)

    
    page_manager = PageManager(app, db_manager)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
