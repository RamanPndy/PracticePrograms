from collections import defaultdict

class Node(object):
    def __init__(self, val, prevNode=None, nextNode=None):
        self.val = val
        self.prev = prevNode
        self.next = nextNode

class LinkedList(object):
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}
    
    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = Node(val, self.left, self.right)
        self.map[val] = node
        node.prev.next = node
        node.next.prev = node
    
    def pop(self, val):
        if val in self.map:
            node = self.map.pop(val, None)
            nodePrev, nodeNext = node.prev, node.next
            nodePrev.next = nodeNext
            nodeNext.prev = nodePrev
    
    def popLeft(self):
        val = self.left.next.val
        self.pop(val)
        return val
    
    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.lfuCount = 0
        self.valMap = {}
        self.countMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] = cnt + 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt+1].pushRight(key)

        if cnt == self.lfuCount and self.listMap[cnt].length() == 0:
            self.lfuCount += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.valMap:
            self.counter(key)
            return self.valMap.get(key)
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cap == 0:
            return

        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCount].popLeft()
            print (key, value, self.lfuCount, res)
            print (self.valMap)
            print (self.countMap)
            self.valMap.pop(res)
            self.countMap.pop(res)
        
        self.valMap[key] = value
        self.counter(key)
        self.lfuCount = min(self.lfuCount, self.countMap[key])
 

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)