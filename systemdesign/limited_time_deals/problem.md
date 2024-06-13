Problem Statement
You happen to be a budding entrepreneur and you have come up with an idea to build an e-commerce giant like Amazon, Flipkart, Walmart, etc. As part of this ambition, you want to build a platform to duplicate the concept of Limited Time Deals. create low level design of limited time deals using interface, multiple modules using design pattern.

Limited Time Deals
******************
A limited-time deal implies that a seller will put up an item on sale for a limited time period, say, 2 hours, and will keep a maximum limit on the number of items that would be sold as part of that deal. 
Users cannot buy the deal if the deal time is over 
Users cannot buy if the maximum allowed deal has already been bought by other users.
One user cannot buy more than one item as part of the deal.

The task is to create APIs to enable the following operations

Create a deal with the price and number of items to be sold as part of the deal
End a deal 
Update a deal to increase the number of items or end time
Claim a deal


Design Patterns Used
Singleton Pattern: Ensure that DealManager is a single instance (if needed) to handle all deals.
Strategy Pattern: If you want to add different types of deals (e.g., percentage off, buy one get one), you can define strategies for each deal type.

