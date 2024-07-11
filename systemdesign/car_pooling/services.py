from systemdesign.car_pooling.models import User


class UserRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserRegistry, cls).__new__(cls)
            cls._instance.users = []
        return cls._instance

    def register_user(self, user: User):
        self.users.append(user)
    
    def get_user(self, user_id: int):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
