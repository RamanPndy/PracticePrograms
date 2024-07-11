from systemdesign.pizza_delivery_system.services import DeliveryServiceImpl, OrderServiceImpl, PizzaServiceImpl, UserServiceImpl


def main():
    user_service = UserServiceImpl()
    pizza_service = PizzaServiceImpl()
    order_service = OrderServiceImpl()
    delivery_service = DeliveryServiceImpl()

    # Register users
    user1 = user_service.register_user("Alice", "123 Main St", "alice@example.com")
    user2 = user_service.register_user("Bob", "456 Elm St", "bob@example.com")

    # Add pizzas
    pizza1 = pizza_service.add_pizza("Margherita", ["cheese", "tomato"], 8.5)
    pizza2 = pizza_service.add_pizza("Pepperoni", ["cheese", "pepperoni"], 10.0)

    # Create an order
    order = order_service.create_order(user1, [pizza1, pizza2])

    # Assign delivery
    delivery = delivery_service.assign_delivery(order, "John Doe")
    delivery_service.update_delivery_status(delivery.delivery_id, "Delivered")

    # Print order and delivery details
    print(f"Order {order.order_id} for {order.user.name}:")
    for pizza in order.pizzas:
        print(f"- {pizza.name} (${pizza.price})")
    print(f"Total price: ${order.total_price}")
    print(f"Delivery status: {delivery.status}")

if __name__ == "__main__":
    main()
