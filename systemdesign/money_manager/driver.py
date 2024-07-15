from datetime import datetime
from systemdesign.money_manager.services import AnalyticsServiceImpl, CategoryServiceImpl, TransactionServiceImpl, UserServiceImpl


def main():
    user_service = UserServiceImpl()
    category_service = CategoryServiceImpl()
    transaction_service = TransactionServiceImpl()
    analytics_service = AnalyticsServiceImpl()

    # Create a user
    user = user_service.create_user("Alice", "alice@example.com")

    # Create categories
    food_category = category_service.create_category(user, "Food")
    travel_category = category_service.create_category(user, "Travel")

    # Record transactions
    transaction_service.record_transaction(user, food_category, 50.0, datetime(2024, 7, 6))
    transaction_service.record_transaction(user, travel_category, 200.0, datetime(2024, 7, 6))

    # View spend analytics
    monthly_analytics = analytics_service.get_spend_analytics(user, "monthly")
    print("Monthly Spend Analytics:", monthly_analytics)

    # View ledger
    transactions = transaction_service.get_transactions(user)
    for t in transactions:
        print(f"{t.user.name} spent {t.amount} on {t.category.name} at {t.date}")

if __name__ == "__main__":
    main()
