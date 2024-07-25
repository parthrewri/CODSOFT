class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts):
                print(f"{idx + 1}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                found = True
        if not found:
            print("No matching contact found.")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                new_name = input(f"Enter new name for {contact.name}: ")
                new_phone = input(f"Enter new phone number for {contact.name}: ")
                new_email = input(f"Enter new email for {contact.name}: ")
                new_address = input(f"Enter new address for {contact.name}: ")

                contact.name = new_name if new_name else contact.name
                contact.phone = new_phone if new_phone else contact.phone
                contact.email = new_email if new_email else contact.email
                contact.address = new_address if new_address else contact.address
                print("Contact updated successfully.")
                return
        print("No matching contact found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("No matching contact found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.display_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number of contact to update: ")
            contact_book.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number of contact to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

