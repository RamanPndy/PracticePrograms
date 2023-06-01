import random

class RandomizedSet(object):

    def __init__(self):
        self.arr = list()
        self.m = dict()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.arr:
            self.arr.append(val)
            self.m[val] = len(self.arr)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.m:        
            last_elem_in_list = self.arr[-1]
            index_of_elem_to_remove = self.m[val]

            self.m[last_elem_in_list] = index_of_elem_to_remove
            self.arr[index_of_elem_to_remove] = last_elem_in_list
            
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