+-------------------+          +-----------------------+         +-----------------------+
|       IUser       |          |    StockExchange      |         |     OrderService      |
+-------------------+          +-----------------------+         +-----------------------+
|                   |          | +submit_order()       |         | +match_orders()       |
|                   | 1      * | +execute_order()      | 1     * | +cancel_order()       |
+-------------------+ -------->+ +cancel_order()       +-------->+ +get_open_orders()    |
                                +-----------------------+         | +get_executed_orders()|
                                                                   +-----------------------+
            ^                                                                       ^
            |                                                                       |
            +-----------------------------------------------------------------------+
                                            ^
                                            |
+-------------------+        1             +------------------+
|       Order       | -------------------->   Stock          |
+-------------------+                      +------------------+
| -order_id: int    |                      | -name: str       |
| -time: datetime   |                      | -price: float    |
| -stock_name: str  |                      +------------------+
| -type: str        |
| -quantity: int    |
| -price: float     |
| -status: str      |
+-------------------+
| +get_order_id()   |
| +get_time()       |
| +get_stock_name() |
| +get_type()       |
| +get_quantity()   |
| +get_price()      |
| +get_status()     |
+-------------------+
