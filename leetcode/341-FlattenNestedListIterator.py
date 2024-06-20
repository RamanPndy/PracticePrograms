'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Initialization:
    The __init__ method initializes the iterator with the nested list. It uses the flatten method to process the nested list 
    and store elements in a stack.

Flatten Method:
    The flatten method takes a nested list and pushes its elements onto the stack in reverse order. This ensures that when we 
    pop elements from the stack, we get them in the correct order.

Next Method:
    The next method pops the top element from the stack and returns it. It assumes that the top element is always an integer 
    since hasNext ensures this before next is called.

HasNext Method:
    The hasNext method checks if there are any integers left in the stack.
    It processes elements at the top of the stack: if the top element is an integer, it returns True. If it's a list, it pops 
    the list, flattens it, and pushes its elements onto the stack.

Key Points
    Using a stack allows us to process elements in LIFO (Last In, First Out) order, which is suitable for handling nested structures.
    The flatten method ensures that the nested list is processed correctly.
    The hasNext method ensures that only integers are at the top of the stack when next is called.
'''
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        self.flatten(nestedList)
    
    def flatten(self, nestedList):
        # Flatten the list from the end to the start
        for element in reversed(nestedList):
            self.stack.append(element)
    
    def next(self) -> int:
        # hasNext would have ensured that the top of the stack is an integer
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.flatten(top.getList())
        return False

# This would be used in a solution where the NestedInteger interface is predefined:
class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self._list = []
        else:
            self._integer = value
            self._list = None

    def isInteger(self):
        return self._list is None

    def getInteger(self):
        return self._integer

    def getList(self):
        return self._list

    def add(self, elem):
        if self._list is None:
            self._list = []
        self._list.append(elem)

# Example usage:
nestedList = [NestedInteger([NestedInteger(1), NestedInteger([NestedInteger(4), NestedInteger([NestedInteger(6)])])])]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)  # Output: [1, 4, 6]
