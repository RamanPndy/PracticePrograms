import mmh3  # MurmurHash library (you can install via `pip install mmh3`)
from bitarray import bitarray  # Bit array library (`pip install bitarray`)

class BloomFilter:
    '''
    TC: O(k) for add and check operations, where k is the number of hash functions
    SC: O(m) where m is the size of the bit array
    '''
    def __init__(self, size, hash_count):
        self.size = size  # Size of bit array
        self.hash_count = hash_count  # Number of hash functions
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = 1

    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == 0:
                return False
        return True

bf = BloomFilter(size=5000, hash_count=7)

words = ["apple", "banana", "grape", "orange", "watermelon"]

for word in words:
    bf.add(word)

print(bf.check("apple"))       # True (probably in set)
print(bf.check("banana"))      # True (probably in set)
print(bf.check("cherry"))      # False (definitely not in set)
print(bf.check("watermelon"))  # True (probably in set)
print(bf.check("mango"))       # False (definitely not in set)
