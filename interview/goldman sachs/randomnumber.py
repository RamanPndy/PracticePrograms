class CustomRandom:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def random(self):
        return self.next() / float(self.m)

# Example usage
custom_rng = CustomRandom(seed=12345)
print(custom_rng.random())  # Generate a random number between 0 and 1
print(custom_rng.random())  # Generate another random number
