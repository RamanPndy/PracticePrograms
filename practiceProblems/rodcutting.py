def mystery(a):
    if a <= 0:
        return 1
    else:
        return mystery(a-1)

print mystery(100)

