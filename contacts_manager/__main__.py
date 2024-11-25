import sys
from unittest import expectedFailure

from contacts_manager.contact import Contact
from contacts_manager.data import Data

if __name__ == "__main__":
    data = Data()

    while True:
        print("\nMenu:")
        print("1. Aggiungi contatto")
        print("2. Visualizza contatti")
        print("3. Modifica contatto")
        print("4. Elimina contatto")
        print("5. Cerca contatto")
        print("6. Esci")
        try:
            option_selected = int(input("Scegli un'opzione: "))
        except ValueError:
            option_selected = 0

        if option_selected == 0 or option_selected > 6:
            print("valore non ammesso!")

        if option_selected == 1:
            name = input("Nome: ")
            surname = input("Cognome: ")
            telephone = input("Telefono: ")
            email = input("Email: ")
            new_contact = Contact(name, surname, telephone, email)
            data.add_contact(new_contact)
            data.save_contacts()

        if option_selected == 2:
            data.list_contacts()

        if option_selected == 3:
            try:
                id_contact = int(input("ID Contatto: "))
                data.edit_contact(id_contact)
                data.save_contacts()
            except ValueError:
                print("valore non ammesso!")

        if option_selected == 4:
            try:
                id_contact = int(input("ID Contatto: "))
                data.delete_contact(id_contact)
                data.save_contacts()
            except ValueError:
                print("valore non ammesso!")

        if option_selected == 5:
            name_or_surname = input("Nome o Cognome:")
            contacts = data.search_contact(name_or_surname)
            if len(contacts) == 0:
                print("contatto non trovato!")
            else:
                print(f"contatti trovati: {len(contacts)}")
                for i, contact in enumerate(contacts):
                    print(f"Contatto {i + 1}:")
                    print(contact)

        if option_selected == 6:
            print("bye bye!")
            sys.exit()
