def repeatedChars(str):
    order =[]
    counts ={}
    for x in str:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            order.append(x)

    for x in order:
        if counts[x]== 1:
            return x
    return None

print repeatedChars("raman")