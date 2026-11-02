class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        Question:
        Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. 
        You can return them in any order.

        Example:
        Input: s = "25525511135"
        Output: ["255.255.11.135","255.255.111.35"]

        Approach:
        Use backtracking to generate all possible segments of the IP address.
        1. Each segment should be between 0 and 255.
        2. Avoid leading zeros unless the segment is "0".
        3. Recursively build the IP address and add it to the result if it has exactly 4 segments.

        Why this works:
        By exploring all valid segment combinations and ensuring the constraints are met, 
        we can generate all possible valid IP addresses.

        Time complexity:
        O(1) as the number of valid IP addresses is limited.

        Space complexity:
        O(1) as we are using constant extra space for the result.
        """
        res = []
        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
            if len(path) >= 4:
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start+length]
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(start+length, path + [segment])

        backtrack(0, [])
        return res