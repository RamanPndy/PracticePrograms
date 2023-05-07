def allPalindromeSubstring(s):
    v = set()

    pivot = 0.0
    while pivot < len(s):

        pr = pivot - int(pivot)

        while ((pivot + pr) < len(s) and (pivot - pr) >= 0 and (s[int(pivot - pr)] == s[int(pivot + pr)])):
            palistr = s[int(pivot - pr): int(pivot + pr + 1)]
            print (palistr)
            v.add(palistr)

            pr += 1

        pivot += 0.5
    return v