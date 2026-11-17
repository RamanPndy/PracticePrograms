class Trie(object):
    '''
    Question: Implement a trie with insert, search, and startsWith methods.
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

    Example:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")   # returns True
    trie.search("app")     # returns False
    trie.startsWith("app") # returns True

    Approach:
    1. We use a dictionary to store the children of each node.
    2. Each node also has a boolean flag to indicate if it is the end of a word.
    3. This allows us to efficiently check for the existence of words and prefixes by traversing the tree according 
    to the characters in the input string.
    4. This approach ensures that both insertion and search operations have a time complexity of O(n), 
    where n is the length of the word or prefix.
    
    Why this works ?
    Each node in the trie represents a character in the inserted words.
    By storing children in a dictionary, we can quickly navigate to the next character.
    The boolean flag at each node indicates whether a complete word ends at that node.
    This structure allows us to efficiently check for both full word matches and prefix matches.

    The trie structure is particularly effective for scenarios where we need to perform multiple prefix-based searches, 
    as it allows us to quickly eliminate non-matching branches and focus only on relevant parts of the tree.

    Time complexity:
    - Insertion: O(n), where n is the length of the word being inserted.
    - Search: O(n), where n is the length of the word being searched.
    - Prefix search: O(n), where n is the length of the prefix.

    Space complexity:
    - O(n*m), where n is the number of words inserted and m is the average length of the words.
    '''

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        How the insertion works:
        1. We start from the root node and iterate through each character of the word.
        2. For each character, we check if it exists in the current node's children.
        3. If it doesn't exist, we create a new Trie node for that character.
        4. We then move to the child node corresponding to the current character.
        5. After processing all characters, we mark the last node as the end of a word.
        """
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        How the search works:
        1. We start from the root node and iterate through each character of the word.
        2. For each character, we check if it exists in the current node's children.
        3. If it doesn't exist, we return False as the word is not present.
        4. We then move to the child node corresponding to the current character.
        5. After processing all characters, we check if the last node is marked as the end of a word.
        6. If it is, we return True, indicating the word exists in the trie; otherwise, we return False.
        """
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        How the prefix search works:
        1. We start from the root node and iterate through each character of the prefix.
        2. For each character, we check if it exists in the current node's children.
        3. If it doesn't exist, we return False as no word with the given prefix is present.
        4. We then move to the child node corresponding to the current character.
        5. After processing all characters, if we haven't returned False, we return True, indicating that there is at least one word in the trie with the given prefix.
        """
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)