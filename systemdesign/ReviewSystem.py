import datetime

class Review:
    def __init__(self, review_id, user_id, rating, comment):
        self.review_id = review_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.datetime.now()

class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_average_rating(self):
        if not self.reviews:
            return None
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

class ReviewSystem:
    def __init__(self):
        self.reviews = {}
        self.products = {}
        self.users = {}

    def add_review(self, review_id, user_id, rating, comment):
        review = Review(review_id, user_id, rating, comment)
        self.reviews[review_id] = review

    def remove_review(self, review_id):
        if review_id in self.reviews:
            del self.reviews[review_id]

    def get_reviews_for_user(self, user_id):
        return [review for review in self.reviews.values() if review.user_id == user_id]

    def get_average_rating(self):
        total_ratings = sum(review.rating for review in self.reviews.values())
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0
    
    def add_product(self, product_id, name):
        product = Product(product_id, name)
        self.products[product_id] = product
        return product

    def add_user(self, user_id, name):
        self.users[user_id] = name

    def submit_review(self, user_id, product_id, rating, content):
        user = self.users.get(user_id)
        product = self.products.get(product_id)
        if user and product:
            review_id = len(self.reviews) + 1
            review = Review(review_id, user, rating, content)
            product.add_review(review)
            self.reviews[review_id] = review
            return review
        else:
            return None

# Example usage
if __name__ == "__main__":
    review_system = ReviewSystem()

    # Add reviews
    review_system.add_review(1, 1, 4, "Great product!")
    review_system.add_review(2, 2, 5, "Excellent service!")
    review_system.add_review(3, 1, 3, "Could be better")

    # Get reviews for a user
    user_reviews = review_system.get_reviews_for_user(1)
    for review in user_reviews:
        print(f"User {review.user_id} rated {review.rating}: {review.comment}")

    # Remove a review
    review_system.remove_review(3)

    # Get average rating
    print("Average rating:", review_system.get_average_rating())
