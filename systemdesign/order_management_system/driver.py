# Example Usage
from systemdesign.order_management_system.impl import Cart, Inventory, Notification, Offer, Order, Payment

inventory = Inventory()
cart = Cart()
order_service = Order()
offer = Offer(1, "10% off", 0.1)
payment_service = Payment()
notification_service = Notification()

# Simulate adding items to inventory
inventory.update_stock('item1', 10)

# Simulate customer adding items to cart
cart.add_item('item1', 2)

# Place order
order = order_service.place_order(cart, 'customer1')

# Apply offer
order = offer.apply_offer(order)

# Process payment
payment = payment_service.process_payment(order['total_price'])

# Send notification
notification_service.send_notification('customer1', f"Order {order['order_id']} placed successfully!")

# Check order status
status = order_service.get_order_status(order['order_id'])
print(f"Order Status: {status}")
