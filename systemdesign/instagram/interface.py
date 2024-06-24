from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_profile_type(self):
        pass

    @abstractmethod
    def post_photo(self, photo):
        pass

    @abstractmethod
    def follow(self, user):
        pass

    @abstractmethod
    def add_comment(self, post, comment):
        pass

    @abstractmethod
    def like_post(self, post):
        pass

    @abstractmethod
    def like_comment(self, comment):
        pass

    @abstractmethod
    def add_tag(self, tag):
        pass

class Post(ABC):
    @abstractmethod
    def add_comment(self, comment):
        pass

    @abstractmethod
    def add_like(self, user):
        pass

    @abstractmethod
    def add_tag(self, tag):
        pass

class Comment(ABC):
    @abstractmethod
    def add_like(self, user):
        pass

    @abstractmethod
    def add_tag(self, tag):
        pass

class TagManager(ABC):
    @abstractmethod
    def add_tag(self, tag):
        pass

    @abstractmethod
    def get_top_k_tags(self, k):
        pass
