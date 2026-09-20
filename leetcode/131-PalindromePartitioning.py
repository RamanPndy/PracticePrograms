class Solution(object):
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        backtracking
        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]
        Use a backtracking approach to generate all the possible palindrome partitions.
        For each character of the string, consider all possible substrings starting at the 
        current character and check if it's a palindrome.
        If it's a palindrome, add it to the current partition and recursively find all partitions that 
        can be formed from the rest of the string.
        When we have traversed the whole string, add the current partition to the final result.
        1.Create a list to store the final result.
        2.Create an empty list to store the current partition.
        3.Write a recursive function to generate all the possible partitions.
        4.In the function, check if the current partition is a valid palindrome partition or not. 
          If it's valid, add the current partition to the final result.
        5.For each character of the string, consider all possible substrings starting at the current 
        character and check if it's a palindrome. If it's a palindrome, add it to the current partition 
        and recursively find all partitions that can be formed from the rest of the string.
        6. When we have traversed the whole string, add the current partition to the final result.
        7. Return the final result.

        Question:

        Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
        Approach:
        - Use backtracking to explore all possible partitions of the string.
        - For each substring, check if it is a palindrome.
        - If it is, include it in the current partition and recursively process the remaining string.
        - Once the end of the string is reached, add the current partition to the result list.
        Complexity Analysis:
        - Time: O(n * 2^n) where n is the length of the string, as there are 2^n possible partitions and checking each partition takes O(n) time.
        - Space: O(n) for the recursion stack and the current partition list.
        Steps:
        1. Initialize an empty list to store the final result.
        2. Define a helper function for backtracking.
        3. In the helper function, iterate through the string and check for palindromic substrings.
        4. If a palindromic substring is found, add it to the current partition and recursively call the helper function for the remaining string.
        5. Once the end of the string is reached, add the current partition to the final result.
        6. Return the final result.
        """
        res  = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range (i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i: j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
        