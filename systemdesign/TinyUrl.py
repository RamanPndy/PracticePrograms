import hashlib
import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, long_url):
        """Shorten a long URL."""
        hash_code = self.generate_hash(long_url)
        short_url = self.generate_short_url(hash_code)
        self.url_map[short_url] = long_url
        return short_url

    def generate_hash(self, long_url):
        """Generate a unique hash for the long URL."""
        hash_object = hashlib.sha256(long_url.encode())
        return hash_object.hexdigest()

    def generate_short_url(self, hash_code):
        """Generate a short URL from the hash code."""
        alphabet = string.ascii_letters + string.digits
        # You can adjust the length of the short URL as needed
        short_url = ''.join(random.choice(alphabet) for _ in range(6))
        return short_url

    def redirect(self, short_url):
        """Redirect to the original long URL."""
        if short_url in self.url_map:
            return self.url_map[short_url]
        else:
            return "Short URL not found."

# Example usage:
shortener = URLShortener()
long_url = "https://example.com/very-long-url-with-many-characters"
short_url = shortener.shorten_url(long_url)
print("Short URL:", short_url)
print("Long URL:", shortener.redirect(short_url))
