class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a 
        string s of length n where:
            s[i] == 'I' if perm[i] < perm[i + 1], and
            s[i] == 'D' if perm[i] > perm[i + 1].
        Given a string s, reconstruct the permutation perm and return it.
        Input: s = "IDID"
        Output: [0,4,1,3,2]
        """
        start=0
        end=len(s)
        res=[]
        perm=[j for j in range(start,end+1)]
        for i in s:
            if i=="I":
                res.append(perm[start])
                start+=1
            if i=="D":
                res.append(perm[end])
                end-=1
            
        res.append(perm[start])
        return res