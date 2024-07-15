from datetime import datetime

class Order:
    def __init__(self, order_id: int, time: datetime, stock_name: str, type: str, quantity: int, price: float):
        self.order_id = order_id
        self.time = time
        self.stock_name = stock_name
        self.type = type
        self.quantity = quantity
        self.price = price
        self.status = "OPEN"

    def get_order_id(self) -> int:
        return self.order_id

    def get_time(self) -> datetime:
        return self.time

    def get_stock_name(self) -> str:
        return self.stock_name

    def get_type(self) -> str:
        return self.type

    def get_quantity(self) -> int:
        return self.quantity

    def get_price(self) -> float:
        return self.price

    def get_status(self) -> str:
        return self.status

    def set_status(self, status: str) -> None:
        self.status = status