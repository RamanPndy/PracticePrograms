class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"
        Steps:
        1. create a stack ans vars to hold current string and current number
        2. tranverse string character by character
            - if character is a number then assign it to current number
            - if character is opening bracket "["
                - append current number and current string in stack
                - reset current number and current string to 0 and ""
            - if character is closing bracket "]"
                - get previous string and previous number from stack after popping
                - append (previous string) + (current string * previous number) in current string
        """
        st = []
        cs = ''
        num = 0
        for c in s:
            if c.isdigit():
                num = num *10 + int(c)
            elif c == "[":
                st.append(num)
                st.append(cs)
                num = 0
                cs = ''
            elif c == "]":
                prev_str = st.pop()
                prev_num = st.pop()
                cs = prev_str + cs * prev_num
            else:
                cs += c
        while st:
            cs += st.pop()
        return cs