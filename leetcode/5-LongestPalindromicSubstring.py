class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.
        Input: s = "cbbd"
        Output: "bb"
        Idea: Expanding Around Centers
        The idea behind this approach is to consider every character in the string as a potential center of a palindrome and 
        then expand around that center to find the longest palindromic substring.

        steps: 
        1. create res and resLen which will hold result string and it's length
        2. traverse through length of string
        3. use 2 pointer approach for even and odd places
            even := l,r = i, i
            odd := l, r = i, i+1
        4. for both above cases loop until l >= 0 and r < len(s) and s[l] == s[r]
            - if r-l+1 > resLen then res = s[l:r+1]
            decrease l and increase r

        # Time: O(n2)
        # Space: O(1)
        """
        res = ""
        resLen = 0
        for i in range(len(s)):
            #even palindrome string
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l = l -1
                r = r + 1
            
            #odd palindrome string
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l = l -1
                r = r + 1
        return res
    
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Even length palindrome
            palindrome1 = expandAroundCenter(i, i)
            # Odd length palindrome
            palindrome2 = expandAroundCenter(i, i + 1)

            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest
            
class Solution:
  def longestPalindrome(self, s):
    '''
    # Time: O(n)
    # Space: O(n)
    Steps:
    1. add sentinels(@ and $) to each end of the input string
    2. 
    '''
    # @ and $ signs are sentinels appended to each end to avoid bounds checking
    t = '#'.join('@' + s + '$')
    n = len(t)
    # t[i - maxExtends[i]..i) ==
    # t[i + 1..i + maxExtends[i]]
    maxExtends = [0] * n
    center = 0

    for i in range(1, n - 1):
      rightBoundary = center + maxExtends[center]
      mirrorIndex = center - (i - center)
      maxExtends[i] = rightBoundary > i and \
          min(rightBoundary - i, maxExtends[mirrorIndex])

      # Attempt to expand palindrome centered at i
      while t[i + 1 + maxExtends[i]] == t[i - 1 - maxExtends[i]]:
        maxExtends[i] += 1

      # If palindrome centered at i expand past rightBoundary,
      # adjust center based on expanded palindrome.
      if i + maxExtends[i] > rightBoundary:
        center = i

    # Find the maxExtend and bestCenter
    maxExtend, bestCenter = max((extend, i)
                                for i, extend in enumerate(maxExtends))
    return s[(bestCenter - maxExtend) // 2:(bestCenter + maxExtend) // 2]
