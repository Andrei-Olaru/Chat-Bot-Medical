from flask import Flask, render_template, request, jsonify, url_for, redirect, flash
from bardapi import Bard
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from user_manager import UserManager
from uuid import uuid4

app = Flask(__name__)
app.config['SECRET_KEY'] = 'o_cheie_secreta'
login_manager = LoginManager(app)

# Inițializează UserManager
user_manager = UserManager()


# Configurează LoginManager pentru a încărca utilizatorii:
@login_manager.user_loader
def load_user(user_id):
    user = user_manager.get_user(user_id)
    return user

# # Token-ul pentru API-ul Bard
# BARD_TOKEN = 'fAi7DIgknbW1absUwzWFs3d5KReb5oCGhtbzkqAaBZb0-qsi2T999fCDwDRtIBtlJta6CA.'
#
# # Inițializarea obiectului Bard
# bard = Bard(token=BARD_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     user_input = request.json.get('user_input')
#
#     try:
#         # Trimite întrebarea la Bard folosind token-ul API
#         answer = bard.get_answer(str(user_input))['content']
#         bot_response = answer  # Ajustează în funcție de structura răspunsului obținut
#
#         # Poți face prelucrări suplimentare ale răspunsului aici, dacă este necesar
#
#     except Exception as e:
#         # Gestionează eventualele erori de la Bard
#         print("Eroare de la Bard:", e)
#         bot_response = "A apărut o eroare în timpul procesării cererii."
#
#     # Returnează răspunsul bot-ului către client
#     return jsonify({'bot_response': bot_response})

# Adauga rute pentru login si logout
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = user_manager.login_user(username, password)

        if user:
            print("User autentificat:", current_user.is_authenticated)  # Adăugat pentru depanare
            login_user(user)
            print("User autentificat după login:", current_user.is_authenticated)  # Adăugat pentru depanare
            flash('Autentificare reușită!', 'success')
            is_authenticated = current_user.is_authenticated
            return render_template('index.html', is_authenticated=is_authenticated)
        else:
            flash('Autentificare eșuată. Verificați username-ul și parola.', 'error')

    return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    if(current_user.is_authenticated == False):
        flash('Delogare reușită!', 'success')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = str(uuid4())
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Parolele nu se potrivesc!', 'error')
            return redirect(url_for('register'))

        if user_manager.register_user(user_id, username, password):
            flash('Înregistrare reușită!', 'success')
        else:
            flash('Utilizatorul există deja!', 'error')

        # Adaugă aceste linii pentru a afișa informații în consolă
        print(f"User ID: {user_id}")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Confirm Password: {confirm_password}")

        return redirect(url_for('index'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
