Problem statement:
design dream11 with below use cases
1. able to view ongoing matches
2. create a fantasy team
3. user should be able to create/join a contest
4. scores should be calculated in real time
also define DB schemas of tables included.

Step 1: Define Interfaces
IMatchService: Interface for viewing ongoing matches.
ITeamService: Interface for creating a fantasy team.
IContestService: Interface for creating/joining a contest.
IScoreService: Interface for real-time score calculation.

Step 2: Implement Design Patterns
Factory Pattern: For creating instances of matches, teams, and contests.
Observer Pattern: For real-time score updates.
Strategy Pattern: For different scoring strategies.

Explanation of Index Choices
Primary Keys: Used on primary columns to ensure data uniqueness and fast primary lookups.
Foreign Keys: Ensure referential integrity between related tables.
Indexes on Foreign Keys: Speed up join operations and lookups based on foreign key columns.
Indexes on frequently queried columns: Improve performance for commonly used query filters and joins.