'''
In this case, the UserService class is tightly coupled to the Logger class. If we want to change the logging mechanism 
(e.g., to a file logger), we need to modify the UserService class.
'''
class Logger:
    def log(self, message):
        print(f"Log message: {message}")

class UserService:
    def __init__(self):
        self.logger = Logger()

    def add_user(self, user):
        # Add user logic here
        self.logger.log(f"User {user} added")
