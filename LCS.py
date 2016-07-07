def lcs(S,T):
    m = len(S)
    n = len(T)

    counter = [[0]*(n+1)for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                    # print lcs_set
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])
                    # print lcs_set

lcs('raman','aman')