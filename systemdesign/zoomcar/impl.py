from typing import Dict

from systemdesign.zoomcar.interface import Car


class SedanCar(Car):
    def __init__(self, car_id: str, brand: str, model: str):
        self.car_id = car_id
        self.brand = brand
        self.model = model

    def get_details(self) -> Dict[str, str]:
        return {'car_id': self.car_id, 'brand': self.brand, 'model': self.model, 'type': 'Sedan'}

class SuvCar(Car):
    def __init__(self, car_id: str, brand: str, model: str):
        self.car_id = car_id
        self.brand = brand
        self.model = model

    def get_details(self) -> Dict[str, str]:
        return {'car_id': self.car_id, 'brand': self.brand, 'model': self.model, 'type': 'SUV'}

class HatchbackCar(Car):
    def __init__(self, car_id: str, brand: str, model: str):
        self.car_id = car_id
        self.brand = brand
        self.model = model

    def get_details(self) -> Dict[str, str]:
        return {'car_id': self.car_id, 'brand': self.brand, 'model': self.model, 'type': 'Hatchback'}
