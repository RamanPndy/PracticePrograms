-- Matches table
CREATE TABLE Matches (
    match_id VARCHAR(255) PRIMARY KEY,
    team1 VARCHAR(255),
    team2 VARCHAR(255),
    start_time DATETIME,
    end_time DATETIME
);

-- Users table
CREATE TABLE Users (
    user_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    balance DECIMAL(10, 2)
);

-- Teams table
CREATE TABLE Teams (
    team_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255),
    team_name VARCHAR(255),
    players TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Contests table
CREATE TABLE Contests (
    contest_id INT AUTO_INCREMENT PRIMARY KEY,
    contest_name VARCHAR(255),
    entry_fee DECIMAL(10, 2),
    prize_pool DECIMAL(10, 2)
);

-- UserContests table
CREATE TABLE UserContests (
    user_id VARCHAR(255),
    contest_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (contest_id) REFERENCES Contests(contest_id)
);

-- Scores table
CREATE TABLE Scores (
    user_id VARCHAR(255),
    score INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
