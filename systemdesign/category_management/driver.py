# Create categories and subcategories
from systemdesign.category_management.models import Category, Product

electronics = Category('Electronics')
mobiles = Category('Mobiles')
laptops = Category('Laptops')

# Add subcategories to main category
electronics.add(mobiles)
electronics.add(laptops)

# Create products
iphone = Product('iPhone', 999.99)
samsung = Product('Samsung Galaxy', 899.99)
macbook = Product('MacBook', 1299.99)
dell = Product('Dell Inspiron', 799.99)

# Add products to subcategories
mobiles.add(iphone)
mobiles.add(samsung)
laptops.add(macbook)
laptops.add(dell)

# Display the category structure
electronics.display()
