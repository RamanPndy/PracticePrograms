Design a stock exchange system. There is a list of stocks given with following attributes

order_id
time
stock name
type(BUY/SELL)
quantity
price
You need to output list of stocks in the following format sell_id, buy_id, quantity, price which will get executed.

Implementation of Design Patterns
Observer Pattern for Order Updates:

Notify users or systems when orders are executed or cancelled using observer pattern.
Strategy Pattern for Order Matching:

Implement different strategies (OrderMatchingStrategy) for matching orders based on price and time.
Singleton Pattern for Stock Exchange:

Implement StockExchange as a singleton to ensure only one instance handling order operations.

Use Cases
Submitting an Order:
Use Case: User submits a new buy or sell order for a stock.
Flow: IUser calls submit_order() on StockExchange, creating a new Order object.

Cancelling an Order:
Use Case: User cancels an existing order.
Flow: IUser calls cancel_order() on StockExchange, updating the Order status to cancelled.

Matching Orders:
Use Case: Matching buy and sell orders to execute trades.
Flow: OrderService implements match_orders() to find matching pairs based on price and time priority.

Retrieving Open Orders:
Use Case: Fetching all active buy and sell orders.
Flow: OrderService provides get_open_orders() to retrieve all orders that are active and not yet executed.

Retrieving Executed Orders:
Use Case: Fetching all executed buy and sell orders.
Flow: OrderService provides get_executed_orders() to retrieve all orders that have been successfully matched and executed.