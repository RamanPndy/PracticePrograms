class IOrder:
    def place_order(self, cart, customer):
        pass

    def cancel_order(self, order_id):
        pass

    def get_order_status(self, order_id):
        pass

class IInventory:
    def check_stock(self, item):
        pass

    def update_stock(self, item, quantity):
        pass

class IOffer:
    def apply_offer(self, order):
        pass

class ICart:
    def add_item(self, item, quantity):
        pass

    def remove_item(self, item):
        pass

    def clear_cart(self):
        pass

    def get_total(self):
        pass

class IPayment:
    def process_payment(self, amount):
        pass

class INotification:
    def send_notification(self, user, message):
        pass