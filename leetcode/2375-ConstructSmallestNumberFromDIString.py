class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
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