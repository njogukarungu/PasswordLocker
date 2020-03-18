class User:
    users = []
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def saveUser(self):
        User.users.append(self)
    @classmethod
    def displayUsers(cls):
        return cls.users

