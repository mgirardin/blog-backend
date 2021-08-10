class Contact(object):
    first_name: str
    last_name: str
    email: str
    number: str
    message: str
    
    def __init__(self, first_name: str, last_name: str, email: str, number: str, message: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.number = number
        self.message = message
