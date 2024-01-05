from flask_bcrypt import Bcrypt
from flask_login import UserMixin

bcrypt = Bcrypt()


class User(UserMixin):
    def __init__(self, user_id, username, password_hash):
        self.id = user_id
        self.username = username
        self.password_hash = password_hash

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, username, password):
        if username in self.users:
            return False  # Utilizatorul există deja

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Adaugă utilizatorul în dicționar
        self.users[username] = User(user_id, username, hashed_password)

        return True  # Înregistrare reușită

    def login_user(self, username, password):
        user = self.users.get(username)

        if user and user.check_password(password):
            # print(f"User found: {user.id}")
            return user
        else:
            # print("User not found or password incorrect.")
            return None

    def get_user(self, username):
        return self.users.get(username)
