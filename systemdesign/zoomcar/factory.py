from systemdesign.zoomcar.impl import HatchbackCar, SedanCar, SuvCar
from systemdesign.zoomcar.interface import Car


class CarFactory:
    @staticmethod
    def create_car(car_type: str, **kwargs) -> Car:
        if car_type == 'sedan':
            return SedanCar(**kwargs)
        elif car_type == 'suv':
            return SuvCar(**kwargs)
        elif car_type == 'hatchback':
            return HatchbackCar(**kwargs)
        else:
            raise ValueError("Unknown car type")
