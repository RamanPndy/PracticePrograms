def lengthofLongestSubstring(str):
    if len(str) == 0:
        return None

    l = list(str)
    pre = 0

    mapL = {}
    for i in range(len(l)):
        if(not mapL.has_key(l[i])):
            mapL[l[i]]=i
        else:
            pre = max(pre,len(mapL))
            i = mapL.get(l[i])
            mapL.clear()

    return max(pre,len(mapL))

print lengthofLongestSubstring("raman")