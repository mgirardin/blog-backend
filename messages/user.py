class User(object):
    login: str
    passwd: str
    salt: str

    def __init__(self, login: str, passwd: str, salt: str) -> None:
        self.login = login
        self.passwd = passwd
        self.salt = salt
