class SegmentTree:
    '''
    A Segment Tree is a binary tree used for storing intervals or segments.
    It allows querying the sum of elements in a given range efficiently.
    The tree is built in a way that each node represents an interval, and the leaf nodes represent individual elements.
    The time complexity for building the tree is O(n), where n is the number of elements.
    The time complexity for querying the sum of a range is O(log n).
    The space complexity is O(n) for storing the tree.
    This implementation supports range sum queries and point updates.
    '''
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)  # Segment tree array

        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        # Set value at position index
        pos = index + self.n
        self.tree[pos] = value

        # Move upward and update parents
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            pos //= 2

    def query(self, left, right):
        # Get sum on interval [left, right)
        result = 0
        left += self.n
        right += self.n

        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2

        return result

data = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(data)

print(seg_tree.query(1, 4))  # Sum from index 1 to 3: 3+5+7=15

seg_tree.update(1, 10)       # data[1] = 10

print(seg_tree.query(1, 4))  # Now sum is 10+5+7=22
