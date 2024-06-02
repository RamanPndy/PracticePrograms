'''
Components
User Management: Handles user registration, authentication, and profile management.
Tweet: Represents a message posted by a user.
Follow System: Manages following and follower relationships between users.
Timeline: Aggregates tweets from followed users to create a user's timeline.
Notification: Notifies users of relevant activities such as mentions or likes.
Database: Stores user data, tweets, follow relationships, and other metadata.
'''

# Step 1: Define the User
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.followers = set()
        self.following = set()
        self.tweets = []
        self.likes = set()
        self.retweets = set()

    def __repr__(self):
        return f"User({self.user_id}, {self.username}, {self.email})"

# Step 2: Define the Tweet
import time

class Tweet:
    def __init__(self, tweet_id, content, author):
        self.tweet_id = tweet_id
        self.content = content
        self.timestamp = time.time()
        self.author = author
        self.likes = set()
        self.retweets = set()

    def __repr__(self):
        return f"Tweet({self.tweet_id}, {self.author.username}, {self.content})"

# Step 3: Define the Twitter System
class TwitterSystem:
    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.next_user_id = 1
        self.next_tweet_id = 1

    def create_user(self, username, email):
        user_id = self.next_user_id
        user = User(user_id, username, email)
        self.users[user_id] = user
        self.next_user_id += 1
        return user

    def create_tweet(self, user_id, content):
        tweet_id = self.next_tweet_id
        author = self.users.get(user_id)
        if author:
            tweet = Tweet(tweet_id, content, author)
            self.tweets[tweet_id] = tweet
            author.tweets.append(tweet)
            self.next_tweet_id += 1
            return tweet
        else:
            return None

    def follow_user(self, follower_id, followee_id):
        follower = self.users.get(follower_id)
        followee = self.users.get(followee_id)
        if follower and followee:
            follower.following.add(followee_id)
            followee.followers.add(follower_id)

    def like_tweet(self, user_id, tweet_id):
        user = self.users.get(user_id)
        tweet = self.tweets.get(tweet_id)
        if user and tweet:
            user.likes.add(tweet_id)
            tweet.likes.add(user_id)

    def retweet(self, user_id, tweet_id):
        user = self.users.get(user_id)
        tweet = self.tweets.get(tweet_id)
        if user and tweet:
            user.retweets.add(tweet_id)
            tweet.retweets.add(user_id)

    def get_timeline(self, user_id):
        user = self.users.get(user_id)
        if user:
            timeline = []
            for followee_id in user.following:
                followee = self.users.get(followee_id)
                timeline.extend(followee.tweets)
            timeline.sort(key=lambda x: x.timestamp, reverse=True)
            return timeline

# Example Usage
twitter_system = TwitterSystem()

# Create users
user1 = twitter_system.create_user("user1", "user1@example.com")
user2 = twitter_system.create_user("user2", "user2@example.com")

# Create tweets
tweet1 = twitter_system.create_tweet(user1.user_id, "Hello, Twitter!")
tweet2 = twitter_system.create_tweet(user2.user_id, "Tweeting is fun!")

# Follow users
twitter_system.follow_user(user1.user_id, user2.user_id)

# Like tweets
twitter_system.like_tweet(user1.user_id, tweet2.tweet_id)

# Retweet
twitter_system.retweet(user1.user_id, tweet2.tweet_id)

# Get user1's timeline
timeline = twitter_system.get_timeline(user1.user_id)
for tweet in timeline:
    print(f"{tweet.author.username} tweeted: {tweet.content}")
