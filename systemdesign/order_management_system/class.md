+---------------------+
|      IOrder         |
+---------------------+
| +place_order()      |
| +cancel_order()     |
| +get_order_status() |
+---------------------+
         ^
         |
+---------------------+
|      Order          |
+---------------------+
| -order_id: int      |
| -customer: Customer |
| -items: list        |
| -total_price: float |
| -status: str        |
+---------------------+
| +place_order()      |
| +cancel_order()     |
| +get_order_status() |
+---------------------+

+---------------------+
|    IInventory       |
+---------------------+
| +check_stock()      |
| +update_stock()     |
+---------------------+
         ^
         |
+---------------------+
|    Inventory        |
+---------------------+
| -stock: dict        |
+---------------------+
| +check_stock()      |
| +update_stock()     |
+---------------------+

+---------------------+
|     IOffer          |
+---------------------+
| +apply_offer()      |
+---------------------+
         ^
         |
+---------------------+
|      Offer          |
+---------------------+
| -offer_id: int      |
| -description: str   |
| -discount: float    |
+---------------------+
| +apply_offer()      |
+---------------------+

+---------------------+
|     ICart           |
+---------------------+
| +add_item()         |
| +remove_item()      |
| +clear_cart()       |
| +get_total()        |
+---------------------+
         ^
         |
+---------------------+
|      Cart           |
+---------------------+
| -items: list        |
+---------------------+
| +add_item()         |
| +remove_item()      |
| +clear_cart()       |
| +get_total()        |
+---------------------+

+---------------------+
|    IPayment         |
+---------------------+
| +process_payment()  |
+---------------------+
         ^
         |
+---------------------+
|     Payment         |
+---------------------+
| -payment_id: int    |
| -amount: float      |
| -status: str        |
+---------------------+
| +process_payment()  |
+---------------------+

+---------------------+
|    INotification    |
+---------------------+
| +send_notification()|
+---------------------+
         ^
         |
+---------------------+
|   Notification      |
+---------------------+
| -notification_id: int|
| -message: str       |
+---------------------+
| +send_notification()|
+---------------------+
