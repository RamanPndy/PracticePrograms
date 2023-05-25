class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
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