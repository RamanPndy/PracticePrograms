# find number of occurrence of each character in string
# find the number of days between 2dates
# two numbers are given find the number of primes inclusive and in those prime numbers find the digit which has most frequency
s = raw_input()
d = {}
for i in s:
    d[i] = 0
for i in d.keys():
    l = 0
    for j in s:
        if i==j:
            l +=1
            d[i] = l

print d
print max([ x for x in d.values()])