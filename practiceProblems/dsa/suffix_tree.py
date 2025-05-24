class SuffixTrieNode:
    '''
    TC: O(n)
    SC: O(n)
    This class represents a node in the Suffix Trie.
    Each node contains a dictionary of children nodes and a list of indexes
    where suffixes pass through this node.'''
    def __init__(self):
        self.children = {}
        self.indexes = []  # Store indices of suffixes passing through this node

class SuffixTrie:
    '''
    TC: O(n * m)
    SC: O(n * m)
    This class implements a Suffix Trie, which is a trie that contains all the suffixes of a given string.
    It allows for efficient searching of patterns within the string.
    '''
    def __init__(self, text):
        self.root = SuffixTrieNode()
        self.text = text
        self._build_suffix_trie()

    def _build_suffix_trie(self):
        for i in range(len(self.text)):
            current = self.root
            for char in self.text[i:]:
                if char not in current.children:
                    current.children[char] = SuffixTrieNode()
                current = current.children[char]
                current.indexes.append(i)

    def search(self, pattern):
        current = self.root
        for char in pattern:
            if char not in current.children:
                return []  # pattern not found
            current = current.children[char]
        return current.indexes  # All starting positions of pattern in text

text = "banana"
trie = SuffixTrie(text)

print(trie.search("ana"))  # Output: [1, 3]
print(trie.search("nan"))  # Output: [2]
print(trie.search("apple"))  # Output: []

def build_suffix_array(text):
    '''
    TC: O(n^2 log n)
    SC: O(n)
    This function builds the suffix array using a naive approach.
    It generates all suffixes of the string, sorts them, and returns the
    starting indices of the sorted suffixes.
    '''
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort(key=lambda x: x[0])
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

text = "banana"
sa = build_suffix_array(text)
print(sa)  # Output: [5, 3, 1, 0, 4, 2]


def build_suffix_array_efficient(text):
    '''
    TC: O(n log n)
    SC: O(n)
    This function builds the suffix array using a more efficient algorithm
    based on the idea of sorting suffixes by their first k characters and
    then using the sorted order to build the suffix array for 2k characters.
    It uses a counting sort-like approach to achieve O(n log n) time complexity.
    '''
    n = len(text)
    k = 1
    rank = [ord(c) for c in text]
    sa = list(range(n))

    while k < n:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp = [0] * n
        for i in range(1, n):
            prev, curr = sa[i - 1], sa[i]
            tmp[curr] = tmp[prev] + (1 if (rank[prev], rank[prev + k] if prev + k < n else -1) != 
                                          (rank[curr], rank[curr + k] if curr + k < n else -1) else 0)
        rank = tmp
        k <<= 1

    return sa

text = "banana"
sa = build_suffix_array_efficient(text)
print(sa)  # Output: [5, 3, 1, 0, 4, 2]
