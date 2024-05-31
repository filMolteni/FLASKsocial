from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, validators
import os



class PageManager:
    def __init__(self, app, db_manager):
        self.app = app
        self.db_manager = db_manager
        

        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            form = LoginForm()
            if request.method == 'POST' and form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                user = self.db_manager.get_user_by_username(username)

                if user and user['password'] == password:
                    session['username'] = username
                    flash('Login effettuato con successo!', 'success')
                    return redirect(url_for('profile'))
                else:
                    flash('Username o password non corretti', 'danger')

            return render_template('login.html', form=form)

        @self.app.route('/profile', methods=['GET', 'POST'])
        def profile():
            if 'username' not in session:
                flash('Devi essere loggato per vedere questa pagina', 'danger')
                return redirect(url_for('login'))

            username = session['username']
            user = self.db_manager.get_user_with_photos(username)

            if request.method == 'POST':
                if 'delete' in request.form:
                    photo_id = request.form['delete']
                    self.db_manager.delete_photo(photo_id)
                    flash('Foto eliminata con successo!', 'success')
                    return redirect(url_for('profile'))

                # Gestisci il caricamento della foto
                descrizione = request.form['descrizione']
                isProfileImg = 'isProfileImg' in request.form
                file = request.files['file']
                if file:
                    filename = file.filename
                    save_path = os.path.join(self.app.root_path, 'static', 'image', filename)
                    
                    # Crea la directory se non esiste
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)

                    file.save(save_path)
                    self.db_manager.add_photo(username, filename, descrizione, isProfileImg)
                    flash('Foto caricata con successo!', 'success')
                    return redirect(url_for('profile'))

            return render_template('profile.html', user=user)

        @self.app.route('/logout')
        def logout():
            session.pop('username', None)
            flash('Logout effettuato con successo', 'success')
            return redirect(url_for('login'))

        @self.app.route('/')
        def index():
            users = self.db_manager.get_all_users_with_photos()
            return render_template('index.html', users=users)
        
        @self.app.route('/register', methods=['GET', 'POST'])
        def register():
            form = RegistrationForm()
            if request.method == 'POST' and form.validate_on_submit():
                username = form.username.data
                email = form.email.data
                password = form.password.data

                existing_user = self.db_manager.get_user_by_username(username)
                if existing_user:
                    flash('Il nome utente è già in uso', 'danger')
                else:
                    self.db_manager.create_user(username, email, password)
                    flash('Registrazione avvenuta con successo! Puoi effettuare il login.', 'success')
                    return redirect(url_for('login'))

            return render_template('register.html', form=form)
        
        @self.app.route('/search', methods=['GET', 'POST'])
        def search_user():
            user = None
            if request.method == 'POST':
                search_query = request.form.get('username')
                user = self.db_manager.get_user_with_photos(search_query)
                if not user:
                    flash('User not found', 'danger')
            return render_template('search.html', user=user)

        
       




class LoginForm(FlaskForm):
            username = StringField('Username', [validators.Length(min=1, max=50)])
            password = PasswordField('Password', [validators.DataRequired()])


class RegistrationForm(FlaskForm):
            username = StringField('Username', [validators.Length(min=1, max=50), validators.DataRequired()])
            email = StringField('Email', [validators.Length(min=1, max=50), validators.DataRequired()])
            password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
            confirm_password = PasswordField('Conferma Password', [validators.EqualTo('password', message='Le password devono coincidere'), validators.DataRequired()])

class UpdateDescriptionForm(FlaskForm):
    description = TextAreaField('Descrizione', [validators.Length(min=1, max=500)])
