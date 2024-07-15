from typing import List
from systemdesign.stock_exhange.models import Order


class OrderService:
    def __init__(self):
        self.open_orders: List[Order] = []
        self.executed_orders: List[Order] = []

    def submit_order(self, order: 'Order') -> None:
        self.open_orders.append(order)

    def cancel_order(self, order_id: int) -> None:
        for order in self.open_orders:
            if order.get_order_id() == order_id:
                order.set_status("CANCELLED")
                self.open_orders.remove(order)
                break

    def execute_order(self, sell_order_id: int, buy_order_id: int, quantity: int, price: float) -> None:
        # Logic to execute the order and update executed_orders list
        pass

    def match_orders(self) -> List[tuple]:
        # Logic to match buy and sell orders
        matched_orders = []
        # Implementation details depend on matching strategy (price, time priority)
        return matched_orders

    def get_open_orders(self) -> List[Order]:
        return self.open_orders

    def get_executed_orders(self) -> List[Order]:
        return self.executed_orders