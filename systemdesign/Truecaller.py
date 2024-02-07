import datetime

class User:
    def __init__(self, user_id, name, phone_number):
        self.user_id = user_id
        self.name = name
        self.phone_number = phone_number
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def remove_contact(self, phone_number):
        if phone_number in self.contacts:
            del self.contacts[phone_number]

    def search_contact(self, phone_number):
        return self.contacts.get(phone_number)

class Contact:
    def __init__(self, contact_id, name, phone_number):
        self.contact_id = contact_id
        self.name = name
        self.phone_number = phone_number

class Call:
    def __init__(self, caller, receiver, duration, is_spam=False):
        self.caller = caller
        self.receiver = receiver
        self.duration = duration
        self.timestamp = datetime.datetime.now()
        self.is_spam = is_spam

class CallerIdentification:
    def __init__(self, user_database):
        self.user_database = user_database

    def identify_caller(self, phone_number):
        for user in self.user_database.values():
            contact = user.search_contact(phone_number)
            if contact:
                return contact.name
        return "Unknown"
    
class SpamBlocker:
    def __init__(self):
        self.blacklist = set()

    def block_number(self, phone_number):
        self.blacklist.add(phone_number)

    def is_spam(self, phone_number):
        return phone_number in self.blacklist

class Truecaller:
    def __init__(self):
        self.users = {}
        self.caller_identification = CallerIdentification(self.users)
        self.spam_blocker = SpamBlocker()

    def register_user(self, user_id, name, phone_number):
        user = User(user_id, name, phone_number)
        self.users[phone_number] = user
        return user
    
    def add_contact(self, user_id, name, phone_number):
        user = self.users.get(user_id)
        if user:
            contact = Contact(name, phone_number)
            user.add_contact(contact)

    def remove_contact(self, user_id, phone_number):
        user = self.users.get(user_id)
        if user:
            user.remove_contact(phone_number)

    def identify_caller(self, phone_number):
        return self.caller_identification.identify_caller(phone_number)

    def block_number(self, phone_number):
        self.spam_blocker.block_number(phone_number)

    def is_spam_call(self, phone_number):
        return self.spam_blocker.is_spam(phone_number)

    def identify_call(self, caller_phone_number, receiver_phone_number, duration):
        caller = self.users.get(caller_phone_number)
        receiver = self.users.get(receiver_phone_number)
        if caller and receiver:
            call = Call(caller, receiver, duration)
            if receiver.phone_number in [contact.phone_number for contact in caller.contacts]:
                print(f"{caller.name} is calling {receiver.name}")
            else:
                print("Unknown Caller")
            if duration < 10:
                print("Potential Spam Call")
                call.is_spam = True
            return call
        else:
            print("Invalid phone numbers.")

# Example usage
if __name__ == "__main__":
    truecaller = Truecaller()

    # Register users and add contacts
    user1 = truecaller.register_user(1, "Alice", "1234567890")
    user2 = truecaller.register_user(2, "Bob", "9876543210")
    user1.add_contact(Contact(1, "Bob", "9876543210"))
    user2.add_contact(Contact(2, "Alice", "1234567890"))

    # Identify calls
    call1 = truecaller.identify_call("1234567890", "9876543210", 15)
    call2 = truecaller.identify_call("9876543210", "1234567890", 5)
