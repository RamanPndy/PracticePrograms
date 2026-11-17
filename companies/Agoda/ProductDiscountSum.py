'''
For discount type 1, product will be selled at fixed discount such as if product selling price is 10 and for type 1 discount is 4 then product will be selled at 4.
For discount type 2, it will be percentage discount
For discount type 3, it will be flat discount such as if base price is 10 and for type 3 discount is 4 then product will be selled at 10-4= 6 
So 2 arrays, products and discount arrays will be provided and total selling price need to be calculated.
For example, product array is [["10", "d0", "d1"],["15", "EMPTY", "EMPTY"],["20","d1","EMPTY"]]
discount array is [["d0","1","3"],["d1","2",7]]

The function `calculate_total_price` will take these two arrays and calculate the total selling price after applying the discounts according to their types.
For discount type 1, the product will be sold at the fixed discount price.
For discount type 2, the product will be sold at the percentage discount price.
For discount type 3, the product will be sold at the base price minus the flat discount.

Approach:
1. Build a discount lookup map from the discount array.
2. Iterate through each product and calculate the final price after applying all applicable discounts.
3. For each discount, determine the discounted price based on its type.
4. Keep track of the minimum discounted price for each product.
5. Sum up the final prices of all products to get the total selling price.

Time Complexity: O(n * m) where n is the number of products and m is the number of discounts per product.
Space Complexity: O(d) where d is the number of discounts.

'''
def calculate_total_price(products, discounts):
    discount_map = {}

    # Build discount lookup
    for discount_id, discount_type, value in discounts:
        discount_map[discount_id] = (
            int(discount_type),
            float(value)
        )

    total = 0

    for product in products:
        base_price = float(product[0])
        final_price = base_price

        for discount_id in product[1:]:
            if discount_id == "EMPTY":
                continue

            discount_type, value = discount_map[discount_id]

            if discount_type == 1:
                discounted_price = value

            elif discount_type == 2:
                discounted_price = base_price * (1 - value / 100)

            elif discount_type == 3:
                discounted_price = base_price - value

            else:
                continue

            final_price = min(final_price, discounted_price)

        total += max(0, final_price)

    return total


products = [
    ["10", "d0", "d1"],
    ["15", "EMPTY", "EMPTY"],
    ["20", "d1", "EMPTY"]
]

discounts = [
    ["d0", "1", "3"],
    ["d1", "2", "7"]
]

print(calculate_total_price(products, discounts))

'''
There could be multiple discounts with same id but different types.
In such cases, the last occurrence in the discounts array will overwrite the previous ones in the discount lookup map.

discounts = [
    ["d0", "1", "3"],
    ["d0", "2", "20"],
    ["d0", "3", "4"],
    ["d1", "2", "7"]
]

Approach: For each product, we check all applicable discounts and calculate the best possible price by considering all
discount rules for each discount ID.

Time Complexity: O(n * m) where n is the number of products and m is the number of discounts per product.
Space Complexity: O(d) where d is the number of discounts.
'''
def calculate_total_price(products, discounts):
    discount_map = {}

    # Store all discount rules for each ID
    for discount_id, discount_type, value in discounts:
        discount_map.setdefault(discount_id, []).append(
            (int(discount_type), float(value))
        )

    total = 0

    for product in products:
        base_price = float(product[0])
        best_price = base_price

        for discount_id in product[1:]:
            if discount_id == "EMPTY":
                continue

            for discount_type, value in discount_map.get(discount_id, []):

                if discount_type == 1:
                    price = value

                elif discount_type == 2:
                    price = base_price * (1 - value / 100)

                elif discount_type == 3:
                    price = base_price - value

                else:
                    continue

                best_price = min(best_price, price)

        total += max(0, best_price)

    return total