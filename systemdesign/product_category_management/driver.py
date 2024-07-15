from systemdesign.product_category_management.impl import ProductCategoryManager

manager = ProductCategoryManager(n=10)
    
manager.add_product_category("MOBILES")
manager.get_product_category("MOBILES")  # Output: ALL_PRODUCTS > MOBILES

manager.add_product_category("ANDROID", "MOBILES")
manager.add_product_category("IOS", "MOBILES")

manager.get_product_category("IOS")  # Output: ALL_PRODUCTS > MOBILES > IOS
manager.get_product_category("ANDROID")  # Output: ALL_PRODUCTS > MOBILES > ANDROID

manager.add_product_category("SMARTPHONES", "MOBILES")

manager.move_product_category("ANDROID", "SMARTPHONES")
manager.move_product_category("IOS", "SMARTPHONES")

manager.get_product_category("IOS")  # Output: ALL_PRODUCTS > MOBILES > SMARTPHONES > IOS
manager.get_product_category("ANDROID")  # Output: ALL_PRODUCTS > MOBILES > SMARTPHONES > ANDROID
