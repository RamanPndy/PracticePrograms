A = int(raw_input())
B = int(raw_input())

def power(A,B):
    t = A
    for i in range(B-1):
        A = t * A
        # print A
    return  A

M = power(10,9)+ 7
print power(A,B) % M