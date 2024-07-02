-- View Ongoing Matches (Uses the index on start_time)
SELECT * FROM Matches WHERE start_time <= NOW() AND end_time >= NOW();

-- Fetch Teams for a User (Uses the index on user_id)
SELECT * FROM Teams WHERE user_id = 'user1';

-- Fetch Contests a User Joined (Uses the index on user_id)
SELECT * FROM UserContests WHERE user_id = 'user1';

-- Fetch Users in a Contest (Uses the index on contest_id)
SELECT * FROM UserContests WHERE contest_id = 1;

-- Fetch User Score (Uses the index on user_id)
SELECT * FROM Scores WHERE user_id = 'user1';

