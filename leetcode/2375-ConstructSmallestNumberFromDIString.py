class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        Input: pattern = "IIIDIDDD"
        Output: "123549876"
        Explanation:
        At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
        At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
        Some possible values of num are "245639871", "135749862", and "123849765".
        It can be proven that "123549876" is the smallest possible num that meets the conditions.
        Note that "123414321" is not possible because the digit '1' is used more than once.
        """
        stack = []
        num = 1
        ans = ""
        for i, p in enumerate(pattern):
            if(p == "D"):
                stack.append(num)
                num+=1
            if(p == "I"):
                stack.append(num)
                num+=1
                while(stack):
                    k = stack.pop()
                    ans+= str(k)
        stack.append(num)
        while(stack):
            k = stack.pop()
            ans+= str(k)
            
        return ans