from flask_mysqldb import MySQL

class DatabaseManager:
    def __init__(self, app):
        self.mysql = MySQL(app)

    def get_user_by_username(self, username):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM utenti WHERE username = %s", [username])
        user = cur.fetchone()
        cur.close()
        return user

    def get_all_users_with_photos(self):
        cur = self.mysql.connection.cursor()
        query = """
        SELECT u.ID as user_id, u.username, u.email, u.descrizione as user_descrizione, 
               f.ID as photo_id, f.path, f.descrizione as photo_descrizione, f.isProfileImg
        FROM utenti u
        LEFT JOIN foto f ON u.ID = f.idUtente
        """
        cur.execute(query)
        users = {}
        for row in cur.fetchall():
            user_id = row['user_id']
            if user_id not in users:
                users[user_id] = {
                    'username': row['username'],
                    'email': row['email'],
                    'descrizione': row['user_descrizione'],
                    'photos': []
                }
            if row['photo_id']:
                users[user_id]['photos'].append({
                    'id': row['photo_id'],
                    'path': row['path'],
                    'descrizione': row['photo_descrizione'],
                    'isProfileImg': row['isProfileImg']
                })
        cur.close()
        return users

    def get_user_with_photos(self, username):
        cur = self.mysql.connection.cursor()
        query = """
        SELECT u.ID as user_id, u.username, u.email, u.descrizione as user_descrizione,
               f.ID as photo_id, f.path, f.descrizione as photo_descrizione, f.isProfileImg
        FROM utenti u
        LEFT JOIN foto f ON u.ID = f.idUtente
        WHERE u.username = %s
        """
        cur.execute(query, [username])
        user = None
        photos = []
        for row in cur.fetchall():
            if user is None:
                user = {
                    'user_id': row['user_id'],
                    'username': row['username'],
                    'email': row['email'],
                    'descrizione': row['user_descrizione'],
                    'photos': []
                }
            if row['photo_id']:
                photos.append({
                    'id': row['photo_id'],
                    'path': row['path'],
                    'descrizione': row['photo_descrizione'],
                    'isProfileImg': row['isProfileImg']
                })
        if user:
            user['photos'] = photos
        cur.close()
        return user
