from flask import Flask
from DatabaseManager import DatabaseManager
from PageManager import PageManager
import os

def create_app():
    app = Flask(__name__)

    # Genera una chiave segreta casuale e sicura
    secret_key = os.urandom(24).hex()

    # Configurazione dell'applicazione, inclusa la chiave segreta
    app.config['SECRET_KEY'] = secret_key
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'db_social'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    # Inizializzazione del gestore del database
    db_manager = DatabaseManager(app)

    # Inizializzazione del gestore delle pagine
    page_manager = PageManager(app, db_manager)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
