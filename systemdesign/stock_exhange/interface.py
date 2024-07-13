from systemdesign.stock_exhange.models import Order

class IUser:
    def submit_order(self, order: 'Order') -> None:
        pass

    def cancel_order(self, order_id: int) -> None:
        pass

    def execute_order(self, sell_order_id: int, buy_order_id: int, quantity: int, price: float) -> None:
        pass