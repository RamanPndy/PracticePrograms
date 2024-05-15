class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Input: s = "()[]{}"
        Output: true
        Steps:
        1. create a stack and dictionary which will hold closing bracket as key and opening bracket and value
        2. traverse each character in string
            - if current character is in dictionary values i.e. current character is a opening bracket then append that 
              character in stack
            - else if current character is in dictionary keys i.e. closing bracket
                - if stack is empty or value of current character in dictionary is not equal to top of stack then return false.
            - else return false
        3. return to check if stack is empty
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        