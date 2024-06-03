'''
Components
Customer: Represents a customer with payment details.
Merchant: Represents a merchant or seller.
PaymentMethod: Represents a payment method (e.g., credit card, bank account).
Payment: Represents a payment transaction between a customer and a merchant.
StripeGateway: Manages customers, merchants, payment methods, and payments.
'''
from enum import Enum

# Step 1: Define the Customer and Merchant
class Customer:
    def __init__(self, customer_id, name, email, payment_methods=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.payment_methods = payment_methods or []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

class Merchant:
    def __init__(self, merchant_id, name, email):
        self.merchant_id = merchant_id
        self.name = name
        self.email = email

# Step 2: Define the PaymentMethod
class PaymentMethod:
    def __init__(self, method_id, type, details):
        self.method_id = method_id
        self.type = type  # e.g., credit card, bank account
        self.details = details  # payment method details

class CreditCard(PaymentMethod):
    def __init__(self, method_id, card_number, expiration_date, cvv):
        super().__init__(method_id, "credit_card", {
            "card_number": card_number,
            "expiration_date": expiration_date,
            "cvv": cvv
        })

class BankAccount(PaymentMethod):
    def __init__(self, method_id, account_number, routing_number):
        super().__init__(method_id, "bank_account", {
            "account_number": account_number,
            "routing_number": routing_number
        })

class PaymentStatus(Enum):
    PENDING, SUCCESS, FAILED = 1,2,3

# Step 3: Define the Payment
class Payment:
    def __init__(self, payment_id, customer_id, merchant_id, amount, payment_method_id):
        self.payment_id = payment_id
        self.customer_id = customer_id
        self.merchant_id = merchant_id
        self.amount = amount
        self.payment_method_id = payment_method_id
        self.status = PaymentStatus.PENDING

# Step 4: Define the StripeGateway
import uuid

class StripeGateway:
    def __init__(self):
        self.customers = {}
        self.merchants = {}
        self.payments = {}
        self.next_payment_id = 1

    def create_customer(self, name, email):
        customer_id = str(uuid.uuid4())
        customer = Customer(customer_id, name, email)
        self.customers[customer_id] = customer
        return customer

    def create_merchant(self, name, email):
        merchant_id = str(uuid.uuid4())
        merchant = Merchant(merchant_id, name, email)
        self.merchants[merchant_id] = merchant
        return merchant

    def add_payment_method(self, customer_id, payment_method):
        customer = self.customers.get(customer_id)
        if customer:
            customer.add_payment_method(payment_method)
            return True
        return False

    def process_payment(self, customer_id, merchant_id, amount, payment_method_id):
        customer = self.customers.get(customer_id)
        merchant = self.merchants.get(merchant_id)
        if customer and merchant:
            payment_id = self.next_payment_id
            payment = Payment(payment_id, customer_id, merchant_id, amount, payment_method_id)
            self.payments[payment_id] = payment
            self.next_payment_id += 1
            return payment
        return None

stripe_gateway = StripeGateway()

# Create customer and merchant
customer = stripe_gateway.create_customer("Alice", "alice@example.com")
merchant = stripe_gateway.create_merchant("Acme Inc.", "sales@acme.com")

# Add payment method to customer
credit_card = CreditCard("cc_123", "1234567812345678", "12/25", "123")
stripe_gateway.add_payment_method(customer.customer_id, credit_card)

# Process payment
payment = stripe_gateway.process_payment(customer.customer_id, merchant.merchant_id, 100.0, credit_card.method_id)

if payment:
    print(f"Payment {payment.payment_id} processed successfully.")
else:
    print("Payment processing failed.")
