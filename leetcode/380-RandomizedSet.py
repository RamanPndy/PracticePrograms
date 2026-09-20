import random
'''
Insert Delete GetRandom O(1)

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
Strategy: Use a list to store the elements and a dictionary to store the indices of the elements in the list. 
This allows for O(1) insertion, deletion, and random access.
Time Complexity: O(1) for insert, remove, and getRandom operations.
Space Complexity: O(n), where n is the number of elements in the set.
Steps:
1. Initialize an empty list and an empty dictionary.
2. For insert operation:
    - Check if the element is already in the dictionary.
    - If not, add it to the list and update the dictionary with its index.
3. For remove operation:
    - Check if the element is in the dictionary.
    - If it is, swap it with the last element in the list and update the dictionary.
    - Remove the last element from the list and delete the element from the dictionary.
4. For getRandom operation:
    - Return a random element from the list using random.choice().
'''

class RandomizedSet(object):

    def __init__(self):
        self.arr = list() #list to hold elements
        self.m = dict() #Dictionary to hold index of element

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.m:
            self.m[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        Steps:
        1. Check if the element is in the dictionary.
        2. If it is, swap it with the last element in the list and update the dictionary.
        3. Remove the last element from the list and delete the element from the dictionary.
        4. Return True if the element was removed, False otherwise.
        """
        if val in self.m:
            last_elem_in_list = self.arr[-1]
            index_of_elem_to_remove = self.m[val]
            self.arr[index_of_elem_to_remove] = last_elem_in_list
            self.m[last_elem_in_list] = index_of_elem_to_remove
            
            # delete the last element
            self.arr.pop()
            del self.m[val]
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()