class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0
        for i in range(len(s)):
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l = l -1
                r = r + 1
            
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l = l -1
                r = r + 1
        return res
            
class Solution:
  def longestPalindrome(self, s):
    '''
    # Time: O(n)
    # Space: O(n)
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
