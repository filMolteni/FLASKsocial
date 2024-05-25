# Flask Social Network

Un'applicazione di social network basata su Flask che consente agli utenti di registrarsi, effettuare il login, visualizzare i profili, caricare foto e eliminarle.

## Requisiti

- Python 3.x
- Flask
- Flask-MySQLdb
- Flask-WTF
- MySQL

## Installazione

1. Clona il repository:
    ```sh
    git clone https://github.com/tuo-username/flask-social-network.git
    cd flask-social-network
    ```

2. Crea un ambiente virtuale e attivalo:
    ```sh
    python -m venv env
    source env/bin/activate  # Su Windows usa `env\Scripts\activate`
    ```

3. Installa le dipendenze:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura il database MySQL:
    ```
    importa il database dal repository
    ```
   

## Utilizzo

1. Esegui l'applicazione:
    ```sh
    flask run
    ```

2. Apri il browser e vai a `http://127.0.0.1:5000`.

3. Registra un nuovo utente e accedi.

4. Visualizza e aggiorna il profilo, carica nuove foto e elimina quelle esistenti.

## Struttura del Progetto

- `app/__init__.py`: Inizializza l'app Flask e configura il database.
- `app/DatabaseManager.py`: Gestisce tutte le operazioni del database.
- `app/PageManager.py`: Gestisce le route e la logica delle pagine.
- `templates/`: Contiene i template HTML.
- `static/css/styles.css`: Contiene gli stili CSS.
- `static/images/`: Contiene le immagini caricate dagli utenti.


