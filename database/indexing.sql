-- When to Use Normal Indexes

-- Frequent Single-Column Lookups: Use normal indexes for columns that are frequently queried individually.
-- Example: Searching users by email.
CREATE INDEX idx_users_email ON Users(email);

-- Primary and Foreign Keys: Always index primary and foreign keys to ensure fast lookups and maintain referential integrity.
-- Example: Primary key on user_id
CREATE TABLE Users (
    user_id VARCHAR(255) PRIMARY KEY,
    ...
);

-- Columns Frequently Used in WHERE Clauses: Index columns that are often used in WHERE clauses to filter results.
-- Example: Filtering matches by start time.
CREATE INDEX idx_matches_start_time ON Matches(start_time);

-- Columns Used in ORDER BY and GROUP BY: Index columns used in ORDER BY or GROUP BY clauses to speed up sorting and grouping operations.
-- Example: Ordering matches by end time.
CREATE INDEX idx_matches_end_time ON Matches(end_time);

-- When to Use Composite Indexes

-- Queries Filtering on Multiple Columns: Use composite indexes when queries often filter on multiple columns in combination.
-- Example: Searching for matches by both start_time and end_time.
CREATE INDEX idx_matches_time ON Matches(start_time, end_time);

-- Columns Frequently Used Together in WHERE Clauses: Composite indexes are beneficial when multiple columns are used together in WHERE clauses.
-- Example: Finding user contests by both user_id and contest_id.
CREATE INDEX idx_usercontests_user_contest ON UserContests(user_id, contest_id);

-- Covering Indexes: Use composite indexes to cover a query, meaning all the columns needed by the query are included in the 
-- index, preventing the need to access the table.
-- Example: A query frequently fetches user_id and score from the Scores table.
CREATE INDEX idx_scores_user_score ON Scores(user_id, score);

-- Queries with Multiple Column Conditions: If queries involve conditions on multiple columns and return a large number of rows, 
-- a composite index can help improve performance.
-- Example: Finding contests by both contest_name and entry_fee.
CREATE INDEX idx_contests_name_fee ON Contests(contest_name, entry_fee);

-- Summary
-- Use Normal Indexes when queries typically involve a single column.
-- Use Composite Indexes when queries typically involve multiple columns in conjunction.
-- Always index primary and foreign keys.
-- Consider the order of columns in composite indexes based on query patterns (e.g., most selective columns first).