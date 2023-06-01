Implement the RandomizedSet class:
	•	RandomizedSet() Initializes the RandomizedSet object.
	•	bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
	•	bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
	•	int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Import random
Class RandomizedSet:
	def __init__(self):
		self.val = set()
		self.m = dict()
	def insert(self, val):
		if val in self.val:
			return True
		self.val.add(val)
		self.m[val] = len(self.val)
		return False
	def remove(self, val):
		if val not in self.m:
			return False
		lastElementSet = self.val[-1]
		i = self.m[val]
		self.m[lastElementSet] = i
		self.val[I] = lastElementSet
		self.val[-1] = val
		del self.m[val]
		return True
	def random():
		c = random.choice(0, len(self.val))
		return self.val[c]

class Node { 
Node[ ] children ;
String type ; //file or dir
String name;
String location;
} 
A directory structure is usually represented as a tree. Lets assume you have been given the root Node of that tree
Write a function that given the root dir ,returns a list of filenames contained beneath it that start with the letter ‘a’ (case insensitive). 
Given Inputs : Node node(the root dir) 
Expected Output : List/Array of all names of "files" that are part of the directory sub-tree with the given node as root.

Def LOT(root):
	if not root:
		return
	res = []
	q = [root]
	while q:
		node = q.pop(0)
		if node.name.startswith(‘a’) and node.type == “file”:
			res.append(node.name)
		for child in range(node.children):
			if child is not None:
				q.append(child)
	return res