class Discount:
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
    
    def get_discount(self):
      return self.price * 0.2
    
class VIPDiscount(Discount):
    def get_discount(self):
      return super().get_discount() * 2