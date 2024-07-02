from typing import Dict
from systemdesign.zoomcar.interface import Car


class CarService:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def get_car_details(self, car_id: str) -> Dict[str, str]:
        for car in self.cars:
            if car.get_details()['car_id'] == car_id:
                return car.get_details()
        return {}

class UserService:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id: str, user_info: Dict[str, str]):
        self.users[user_id] = user_info

    def get_user_profile(self, user_id: str) -> Dict[str, str]:
        return self.users.get(user_id, {})
