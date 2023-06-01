class User:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass