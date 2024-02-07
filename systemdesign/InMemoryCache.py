import time

class CacheItem:
    def __init__(self, key, value, ttl):
        self.key = key
        self.value = value
        self.ttl = ttl
        self.creation_time = time.time()

    def is_expired(self):
        return time.time() - self.creation_time > self.ttl

class InMemoryCache:
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl=60):
        self.cache[key] = CacheItem(key, value, ttl)

    def get(self, key):
        if key in self.cache:
            cache_item = self.cache[key]
            if not cache_item.is_expired():
                return cache_item.value
            else:
                del self.cache[key]
        return None

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        self.cache = {}

# Example usage
if __name__ == "__main__":
    cache = InMemoryCache()

    # Set cache values
    cache.set("key1", "value1")
    cache.set("key2", "value2", ttl=5)

    # Get cache values
    print("Value for key1:", cache.get("key1"))
    print("Value for key2:", cache.get("key2"))

    # Wait for key2 to expire
    time.sleep(6)

    # Get expired cache value
    print("Value for key2 after expiration:", cache.get("key2"))

    # Delete cache value
    cache.delete("key1")

    # Clear cache
    cache.clear()
