from systemdesign.order_management_system.interface import ICart, IInventory, INotification, IOffer, IOrder, IPayment


class Order(IOrder):
    def __init__(self):
        self.orders = []
        self.current_id = 0

    def place_order(self, cart, customer):
        self.current_id += 1
        order = {
            'order_id': self.current_id,
            'customer': customer,
            'items': cart.items,
            'total_price': cart.get_total(),
            'status': 'Placed'
        }
        self.orders.append(order)
        return order

    def cancel_order(self, order_id):
        for order in self.orders:
            if order['order_id'] == order_id:
                order['status'] = 'Cancelled'
                return order
        return None

    def get_order_status(self, order_id):
        for order in self.orders:
            if order['order_id'] == order_id:
                return order['status']
        return None
    
class Inventory(IInventory):
    def __init__(self):
        self.stock = {}

    def check_stock(self, item):
        return self.stock.get(item, 0)

    def update_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity
        else:
            self.stock[item] = quantity

class Offer(IOffer):
    def __init__(self, offer_id, description, discount):
        self.offer_id = offer_id
        self.description = description
        self.discount = discount

    def apply_offer(self, order):
        order['total_price'] *= (1 - self.discount)
        return order
    
class Cart(ICart):
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append({'item': item, 'quantity': quantity})

    def remove_item(self, item):
        self.items = [i for i in self.items if i['item'] != item]

    def clear_cart(self):
        self.items = []

    def get_total(self):
        return sum(item['quantity'] * item['item'].price for item in self.items)
    
class Payment(IPayment):
    def __init__(self):
        self.payments = []
        self.current_id = 0

    def process_payment(self, amount):
        self.current_id += 1
        payment = {
            'payment_id': self.current_id,
            'amount': amount,
            'status': 'Processed'
        }
        self.payments.append(payment)
        return payment
    
class Notification(INotification):
    def send_notification(self, user, message):
        print(f"Notification to {user}: {message}")