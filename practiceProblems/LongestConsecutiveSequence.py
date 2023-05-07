def longestConsecutive(num):
    if (len(num) == 0):
        return 0

    a = set(m for m in num)
    maxn = 1

    for e in a:
        left = e - 1
        right = e + 1
        count = 1
        while (left in a):
            count += 1
            a.pop(left)
            left -= 1
        while (right in a):
            count += 1
            a.pop(right)
            right += 1

        maxn = max(count,maxn)
    return maxn

print longestConsecutive([1,0,0,0,2,5])