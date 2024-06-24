from systemdesign.instagram.impl import ConcreteTagManager, ConcreteUser

'''
Design Patterns Used
Observer Pattern: To notify followers of new posts, comments, or likes.
Strategy Pattern: Can be used for different types of profile privacy settings.
Factory Pattern: To create instances of users, posts, comments, and tags.
Singleton Pattern: For the Tag Manager to ensure a single instance managing tags across the application.
'''
if __name__ == "__main__":
    tag_manager = ConcreteTagManager()

    user1 = ConcreteUser("user1", "public")
    user2 = ConcreteUser("user2", "private")

    user1.follow(user2)

    post1 = user1.post_photo("photo1.jpg")
    post1.add_tag("nature")

    comment1 = user2.add_comment(post1, "Nice photo!")
    comment1.add_tag("compliment")

    user2.like_post(post1)
    user1.like_comment(comment1)

    top_tags = tag_manager.get_top_k_tags(2)
    print(top_tags)  # Should print the top 2 tags used by all users
