y = int(raw_input())
def fact(y):
    if y is 1:
        return 1
    else:
        return y*fact(y-1)

f = fact(y)
print f


