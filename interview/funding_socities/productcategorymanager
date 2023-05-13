Product Category Manager
Problem Statement
Implement a command line application for managing catalog of product categories for an e-commerce platform. 
The application must allow n-level(1 < n < 10) hierarchy depth. Value of n to be read as a program argument.
Users of the application must be able to perform the following actions. 
The application must get initialized with a default root product category named `ALL PRODUCTS`.
Requirements
Add a product category (all product categories must have unique name)
ADD_PRODUCT_CATEGORY <product_category_name(non null)> <parent_product_category_name(nullable)>
If parent_product_category_name == null -- add product category under root category
If parent_product_category_name != null and exists -- add product_category under parent_product_category


Move a product category
MOVE_PRODUCT_CATEGORY <product_category_name(non null)> <parent_product_category_name(nullable)>
If parent_product_category_name == null -- move product category under root category
If parent_product_category_name != null and exists -- add product_category under parent_product_category


Get product category
GET_PRODUCT_CATEGORY <product_category_name(non null)>
If product_category_name == null -- return error message(category <name> does not exist)
If product_category_name != null and exists -- return the hierarchy of the product categories from the root to the given product_category

Test Cases
#
Command (Input - STDIN)
Expected Output(STDOUT)
1
ADD_PRODUCT_CATEGORY MOBILES


2
GET_PRODUCT_CATEGORY MOBILES
ALL_PRODUCTS > MOBILES
3
ADD_PRODUCT_CATEGORY ANDROID MOBILES


4
ADD_PRODUCT_CATEGORY IOS MOBILES


5
GET_PRODUCT_CATEGORY IOS
ALL_PRODUCTS > MOBILES > IOS
6
GET_PRODUCT_CATEGORY ANDROID
ALL_PRODUCTS > MOBILES > ANDROID
7
ADD_PRODUCT_CATEGORY SMARTPHONES MOBILES


8
MOVE_PRODUCT_CATEGORY ANDROID SMARTPHONES


9
MOVE_PRODUCT_CATEGORY IOS SMARTPHONES


10
GET_PRODUCT_CATEGORY IOS
ALL_PRODUCTS > MOBILES > SMARTPHONES > IOS
11
GET_PRODUCT_CATEGORY ANDROID
ALL_PRODUCTS > MOBILES > SMARTPHONES > ANDROID


Guidelines
Do not use any third party libraries or frameworks to develop the application. 
Do not use any database/cache (persistent or in-memory). 
Design your own data structure and hold the data in memory.

