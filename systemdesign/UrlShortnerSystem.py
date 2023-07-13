import string
import random

'''
the URL shortener system consists of the URLShortener class. The URLShortener class has a url_mapping 
dictionary that stores the mapping between shortened URLs and their corresponding original URLs. 
The characters variable defines the set of characters to be used for generating the short URL, and 
short_length determines the length of the short URL.

The shorten_url method generates a short URL for a given original URL and stores the mapping in the 
url_mapping dictionary. The generate_short_url method generates a unique short URL using random 
characters until an unused one is found. The get_original_url method retrieves the original URL 
given a short URL.
'''

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.characters = string.ascii_letters + string.digits
        self.short_length = 7

    def shorten_url(self, original_url):
        short_url = self.generate_short_url()
        self.url_mapping[short_url] = original_url
        return short_url

    def generate_short_url(self):
        while True:
            short_url = ''.join(random.choice(self.characters) for _ in range(self.short_length))
            if short_url not in self.url_mapping:
                return short_url

    def get_original_url(self, short_url):
        if short_url in self.url_mapping:
            return self.url_mapping[short_url]
        else:
            return None

    def __str__(self):
        return f"URL Shortener\nTotal URLs: {len(self.url_mapping)}"


# Usage example
url_shortener = URLShortener()

original_url = "https://www.example.com/very/long/url/to/be/shortened"
short_url = url_shortener.shorten_url(original_url)

print(f"Short URL: {short_url}")
print(f"Original URL: {url_shortener.get_original_url(short_url)}")
print(url_shortener)
