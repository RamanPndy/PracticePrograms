class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def sum(a,b):
    sum = 0
    carry = 0
    res = None

    while a != None or b != None:
        f = a.data if a else 0
        s = b.data if b else 0
        sum  = carry + f + s
        carry = 1 if sum >= 10 else 0
        sum  = sum if sum < 10 else sum % 10
        
        t =  Node(sum)
        if not res:
            res = t
        else:
            res.next = t
            res = t
        if a is not None:
            a = a.next
        if b is not None:
            b = b.next