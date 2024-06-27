-- Primary Key on match_id: Ensures uniqueness and fast lookups.
-- Index on start_time: Optimizes queries for viewing ongoing matches based on time.
CREATE TABLE Matches (
    match_id VARCHAR(255) PRIMARY KEY,
    team1 VARCHAR(255),
    team2 VARCHAR(255),
    start_time DATETIME,
    end_time DATETIME,
    INDEX (start_time)
);

-- Primary Key on user_id: Ensures uniqueness and fast lookups.
-- Unique Index on email: Ensures email uniqueness and optimizes queries for user lookups by email.
-- Index on email: Speeds up lookups by email.
CREATE TABLE Users (
    user_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    balance DECIMAL(10, 2),
    INDEX (email)
);

-- Primary Key on team_id: Ensures uniqueness and fast lookups.
-- Index on user_id: Optimizes queries for fetching teams by user.
CREATE TABLE Teams (
    team_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255),
    team_name VARCHAR(255),
    players TEXT,
    INDEX (user_id)
);

-- Primary Key on contest_id: Ensures uniqueness and fast lookups.
-- Index on contest_name: Optimizes queries for fetching contests by name.
CREATE TABLE Contests (
    contest_id INT AUTO_INCREMENT PRIMARY KEY,
    contest_name VARCHAR(255),
    entry_fee DECIMAL(10, 2),
    prize_pool DECIMAL(10, 2),
    INDEX (contest_name)
);

-- Indexes on user_id and contest_id: Optimize queries for fetching contests by user and users by contest.
CREATE TABLE UserContests (
    user_id VARCHAR(255),
    contest_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (contest_id) REFERENCES Contests(contest_id),
    INDEX (user_id),
    INDEX (contest_id)
);

-- Index on user_id: Optimizes queries for fetching scores by user.
CREATE TABLE Scores (
    user_id VARCHAR(255),
    score INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    INDEX (user_id)
);
