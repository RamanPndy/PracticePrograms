+----------------+         +---------------+
|    ICoffeeMachine    |<---------|  CoffeeMachine  |
+----------------+         +---------------+
| + select_beverage() |         | + select_beverage() |
| + dispense_beverage()|         | + dispense_beverage() |
| + refill_ingredient()   |         | + refill_ingredient()   |
+----------------+         +---------------+
        ^
        |
        +-----------------------------------------------+
        |                           |                                 |
+---------------+        +------------------+         +----------------+
|      IBeverage       |<---------|       Espresso        |     +      Latte            |
+---------------+        +------------------+         +----------------+
| + get_name()      |        | + get_name()       |         | + get_name()      |
| + get_recipe()    |        | + get_recipe()     |         | + get_recipe()    |
+---------------+        +------------------+         +----------------+
        ^
        |
        +-----------------------------------------------+
        |                           |                                 |
+---------------+        +------------------+         +----------------+
|     Inventory          |<---------|      Cappuccino      |    +     BeverageFactory|
+---------------+        +------------------+         +----------------+
| + add_ingredient() |        | + get_name()       |         | + create_beverage() |
| + use_ingredient() |        | + get_recipe()     |         +----------------+
| + get_quantity()   |
+---------------+
