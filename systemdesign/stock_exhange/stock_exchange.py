from systemdesign.stock_exhange.models import Order
from systemdesign.stock_exhange.services import OrderService

class StockExchange:
    def __init__(self):
        self.order_service = OrderService()

    def submit_order(self, order: 'Order') -> None:
        self.order_service.submit_order(order)

    def cancel_order(self, order_id: int) -> None:
        self.order_service.cancel_order(order_id)

    def execute_order(self, sell_order_id: int, buy_order_id: int, quantity: int, price: float) -> None:
        self.order_service.execute_order(sell_order_id, buy_order_id, quantity, price)
