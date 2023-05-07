def longestPalindrom(str):
    if len(str) == 0:
        return None
    if len(str) == 1:
        return str
    longest = str[0:1]
    for i in range(len(str)):
        tmp = helper(str,i,i)
        if(len(tmp) > len(longest)):
            longest = tmp
        tmp  = helper(str,i,i+1)
        if(len(tmp) > len(longest)):
            longest = tmp
    return longest

def helper(s,begin,end):
    while(begin >= 0 and end <= len(s)-1 and (s[begin] == s[end])):
        begin -= 1
        end += 1
    return s[begin+1:end]

print longestPalindrom("ramadamaandalda")