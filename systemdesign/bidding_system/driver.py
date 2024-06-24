from systemdesign.bidding_system.impl import AuctionBid, AuctionUser
'''
Design Patterns Used
Observer Pattern: To notify all users when a new bid is placed.
Strategy Pattern: Can be used if there are different bidding strategies (not implemented in this example, but useful for extensibility).
Interface Segregation: Using interfaces to define the contract for bidding and user operations.

Further Enhancements
Decorator Pattern: For additional features like bid validation, minimum increment checks, etc.
Singleton Pattern: If there is a need to ensure only one instance of the AuctionBid class.
'''
if __name__ == "__main__":
    bid = AuctionBid()

    user1 = AuctionUser("Alice")
    user2 = AuctionUser("Bob")

    user1.place_bid(bid, 100)
    user2.place_bid(bid, 150)

    # Output will include notifications to both Alice and Bob about the new highest bid
