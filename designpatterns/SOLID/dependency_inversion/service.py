from designpatterns.SOLID.dependency_inversion.interface import ILogger

class UserService:
    def __init__(self, logger: ILogger):
        self.logger = logger

    def add_user(self, user):
        # Add user logic here
        self.logger.log(f"User {user} added")
