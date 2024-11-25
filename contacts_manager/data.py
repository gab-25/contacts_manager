import json

from contacts_manager.contact import Contact


class Data:
    contacts: list[Contact] = []

    def __init__(self, file="data.json"):
        self.file = file
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
                for contact_data in data:
                    self.contacts.append(Contact(**contact_data))
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open(self.file, 'w') as f:
            json.dump([vars(c) for c in self.contacts], f, indent=2)

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def list_contacts(self):
        print("\nRubrica")
        if (len(self.contacts) == 0):
            print("nessun contatto presente!")
            return
        for i, contact in enumerate(self.contacts):
            print(f"Contatto {i + 1}:")
            print(contact)

    def edit_contact(self, id_contact: int):
        try:
            contact = self.contacts[id_contact - 1]
            contact.name = input("Nome: ")
            contact.surname = input("Cognome: ")
            contact.telephone = input("Telefono: ")
            contact.email = input("Email: ")
            print("Contatto modificato")
        except IndexError:
            print("ID Contatto non esistente!")

    def delete_contact(self, id_contact: int):
        try:
            del self.contacts[id_contact - 1]
            print("Contatto eliminato")
        except IndexError:
            print("ID Contatto non esistente!")

    def search_contact(self, name_or_surname: str) -> list[Contact]:
        result = [contact for contact in self.contacts if
                  name_or_surname.lower() in contact.name.lower() or name_or_surname.lower() in contact.surname.lower()]
        return result
