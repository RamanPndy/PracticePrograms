Given a string s, find the longest substring without repeating characters

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
s = "abcbxy"
s2 = "abbxy"
s3 = "abcba"
s4 = "aaaa"
s5 = "abcd"
s6 = "abcdaxyz"

h = set()
f = dict()
def LRO(s):
    res = ""
    for i in range(len(s)):
        if s[i] in f:
            f[s[i]] += 1
        else:
            f[s[i]] = 1
        if s[i] in res:
            for c in res[:i]:
                if c in h:
                    h.remove(c)
            res = res [i-1:]
        res += s[i]
        h.add(s[i])
    t = ''
    for c in f:
        if c not in res and f[c] == 1 and c in h:
            t += c
    print (t + res)
    
LRO(s6)