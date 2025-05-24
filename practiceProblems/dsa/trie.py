class TrieNode:
    '''
    A single node in the Trie structure.
    Each node contains a dictionary of children nodes and a boolean to mark the end of a word.
    TC: O(1) for node creation
    SC: O(1) for storing children nodes
    '''
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    '''
    A Trie (prefix tree) implementation for efficient storage and retrieval of strings.
    Supports insertion, searching for complete words, and checking for prefixes.
    TC: O(m) for insertion and search, where m is the length of the word
    SC: O(n * m) for storing n words of average length m
    '''
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

trie = Trie()
trie.insert("hello")
trie.insert("helium")

print(trie.search("hello"))    # True
print(trie.search("helix"))    # False
print(trie.starts_with("hel")) # True
print(trie.starts_with("hey")) # False
