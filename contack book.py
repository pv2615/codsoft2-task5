class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __repr__(self):
        return f"Store Name: {self.store_name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"

contacts = []

def add_contact():
    store_name = input("Enter store name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(store_name, phone_number, email, address)
    contacts.append(contact)
    print(f"\nContact for {store_name} added successfully.\n")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for contact in contacts:
            print(contact)
    else:
        print("\nNo contacts found.\n")

def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if query in contact.store_name.lower() or query in contact.phone_number]
    if results:
        print("\nSearch Results:")
        for result in results:
            print(result)
    else:
        print("\nNo contacts found matching the query.\n")

def update_contact():
    store_name = input("Enter store name to update: ")
    for contact in contacts:
        if contact.store_name == store_name:
            print(f"Current details:\n{contact}")
            phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            if phone_number:
                contact.phone_number = phone_number
            if email:
                contact.email = email
            if address:
                contact.address = address
            print(f"\nContact for {store_name} updated successfully.\n")
            return
    print(f"\nContact for {store_name} not found.\n")

def delete_contact():
    store_name = input("Enter store name to delete: ")
    global contacts
    contacts = [contact for contact in contacts if contact.store_name != store_name]
    print(f"\nContact for {store_name} deleted successfully.\n")

def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("\nInvalid choice, please try again.\n")

if __name__ == "__main__":
    main()
