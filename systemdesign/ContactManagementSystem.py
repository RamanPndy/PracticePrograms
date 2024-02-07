import json

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManagementSystem:
    def __init__(self, data_file="contacts.json"):
        self.data_file = data_file
        self.contacts = []

    def load_contacts(self):
        try:
            with open(self.data_file, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.data_file, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self.contacts.append(vars(contact))
        self.save_contacts()
        print(f"Contact {name} added successfully.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]
        self.save_contacts()
        print(f"Contact {name} deleted successfully.")

    def search_contact(self, name):
        results = [contact for contact in self.contacts if contact['name'] == name]
        return results

    def list_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}")

# Example usage
if __name__ == "__main__":
    cms = ContactManagementSystem()

    # Load contacts from file
    cms.load_contacts()

    # Add contacts
    cms.add_contact("Alice", "1234567890", "alice@example.com")
    cms.add_contact("Bob", "9876543210", "bob@example.com")

    # List all contacts
    print("\nAll Contacts:")
    cms.list_all_contacts()

    # Search contact
    print("\nSearch Results for Alice:")
    search_results = cms.search_contact("Alice")
    if search_results:
        for result in search_results:
            print(f"Name: {result['name']}, Phone Number: {result['phone_number']}, Email: {result['email']}")
    else:
        print("No results found.")

    # Delete contact
    cms.delete_contact("Bob")

    # List all contacts after deletion
    print("\nAll Contacts after Deletion:")
    cms.list_all_contacts()
