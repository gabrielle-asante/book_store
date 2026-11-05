from lib.user import User

class UserRepository: 
    def __init__(self, connection):
        self._connection = connection

    def find_by_username(self, username):
        user_details = self._connection.execute(
        'SELECT * FROM users WHERE username = %s', [username]
    )[0]
        return User(user_details['email'], user_details['username'], user_details['password'], user_details['id'])

    def create(self, user):
        self._connection.execute(
            'INSERT INTO users (email, username, password) VALUES (%s, %s, %s)',
            [user.email, user.username, user.password]
        )
        return None

        