from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
import os

class PageManager:
    def __init__(self, app, db_manager):
        self.app = app
        self.db_manager = db_manager

        class LoginForm(FlaskForm):
            username = StringField('Username', [validators.Length(min=1, max=50)])
            password = PasswordField('Password', [validators.DataRequired()])

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

               
                descrizione = request.form['descrizione']
                isProfileImg = 'isProfileImg' in request.form
                file = request.files['file']
                if file:
                    filename = file.filename
                    file.save(os.path.join(self.app.static_folder, 'images', filename))
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
