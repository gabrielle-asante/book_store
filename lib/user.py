class User:
    def __init__(self, email, username, password, id = None):
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        