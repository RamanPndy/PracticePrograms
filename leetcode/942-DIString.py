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

        Question: What is the permutation perm that corresponds to the given string s?
        Intuition: The permutation can be constructed by assigning the smallest available number to 'I' and the largest available number to 'D' 
        as we iterate through the string.
        Steps:
        1. Initialize two pointers, start and end, representing the smallest and largest available numbers.
        2. Iterate through the string s:
            - If the current character is 'I', append the number at the start pointer to the result and increment start.
            - If the current character is 'D', append the number at the end pointer to the result and decrement end.
        3. Append the last remaining number to the result.
        4. Return the result as the reconstructed permutation.
        Time Complexity: O(n), where n is the length of the string s, as we iterate through the string once.
        Space Complexity: O(n) for the result array.
        Interview Explanation: The key insight is to use two pointers to keep track of the smallest and largest available numbers. 
        By assigning the smallest number to 'I' and the largest number to 'D', we can reconstruct the permutation efficiently.
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