from collections import defaultdict
from systemdesign.instagram.interface import Comment, Post, TagManager, ConcreteComment, ConcretePost, User

class ConcreteUser(User):
    def __init__(self, username, profile_type):
        self.username = username
        self.profile_type = profile_type
        self.followers = []
        self.posts = []

    def get_profile_type(self):
        return self.profile_type

    def post_photo(self, photo):
        post = ConcretePost(photo, self)
        self.posts.append(post)
        return post

    def follow(self, user):
        user.followers.append(self)

    def add_comment(self, post, comment_text):
        comment = ConcreteComment(comment_text, self)
        post.add_comment(comment)
        return comment

    def like_post(self, post):
        post.add_like(self)

    def like_comment(self, comment):
        comment.add_like(self)

    def add_tag(self, tag):
        TagManager().add_tag(tag)

class ConcretePost(Post):
    def __init__(self, photo, user):
        self.photo = photo
        self.user = user
        self.comments = []
        self.likes = []
        self.tags = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        self.likes.append(user)

    def add_tag(self, tag):
        self.tags.append(tag)
        TagManager().add_tag(tag)

class ConcreteComment(Comment):
    def __init__(self, text, user):
        self.text = text
        self.user = user
        self.likes = []
        self.tags = []

    def add_like(self, user):
        self.likes.append(user)

    def add_tag(self, tag):
        self.tags.append(tag)
        TagManager().add_tag(tag)

class ConcreteTagManager(TagManager):
    def __init__(self):
        self.tag_count = defaultdict(int)

    def add_tag(self, tag):
        self.tag_count[tag] += 1

    def get_top_k_tags(self, k):
        sorted_tags = sorted(self.tag_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_tags[:k]
