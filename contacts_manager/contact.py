class Contact:
    """class that manages the contact"""

    def __init__(self, name, surname, telephone, email):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"Nome: {self.name}\nCognome: {self.surname}\nTelefono: {self.telephone}\nEmail: {self.email}"
