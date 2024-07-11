design money manager system in python
functional requirements
1. any user can record the transaction for each category, time, amount.
2. user can create any category
3. user can view spend analytics on each category such as monthly or annually in which category transactions are more happened.
4. there should be ledger which will show record for each transaction for example, user x spent on category y of amount z at today
Non functional requirements
1. define proper models and relationship between them
2. define interfaces that will have methods to handle function requirements.
3. implement services using some design patterns which comply with SOLID principles.
4. implement repository which will be used for data persistence in some DB.


Define Models: We'll define models for User, Category, Transaction, and Ledger.
Create Interfaces: We'll define interfaces for the services required.
Implement Service Classes: We'll implement these services using design patterns and ensuring they comply with SOLID principles. We'll implement the services using Singleton and Factory patterns to comply with SOLID principles.
Implement Repository for Data Persistence: We'll implement a repository pattern for data persistence.
