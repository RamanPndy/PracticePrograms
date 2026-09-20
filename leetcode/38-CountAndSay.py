class Solution(object):
    def countAndSay(self, n):
        """
        The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

        countAndSay(1) = "1"
        countAndSay(n) is the run-length encoding of countAndSay(n - 1).
        Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

        Given a positive integer n, return the nth element of the count-and-say sequence.
        Input: n = 4

        Output: "1211"

        Explanation:

        countAndSay(1) = "1"
        countAndSay(2) = RLE of "1" = "11"
        countAndSay(3) = RLE of "11" = "21"
        countAndSay(4) = RLE of "21" = "1211"

        Intuition
        Is problem me hume ek sequence generate karna hai jisme har term, previous term ke digits ka count + digit batata hai. 
        Matlab "look-and-say" pattern follow hota hai.

        Approach
        Base case n=1 ke liye result "1" hoga.
        Har step pe current string ko read karo aur consecutive digits ka count nikal ke ek nayi string banao.
        Yeh naya string agla result ban jaata hai.
        Is process ko n-1 baar repeat karna hai.

        Complexity
        Time complexity:
        Har step me string ke sabhi characters traverse karte hain → O(n * m), jaha m average length of string hai.
        Roughly acceptable as per constraints.

        Space complexity:
        Sirf ek new string store karte hain → O(m).

        Question: Generate the nth term of the count-and-say sequence.
        Approach:
        - Start with the base case "1" for n=1.
        - For each subsequent term, read the previous term and count consecutive digits.
        - Construct the new term by concatenating the count and the digit.
        - Repeat this process until reaching the nth term.
        Time Complexity: O(n * m), where m is the average length of the string.
        Space Complexity: O(m).
        Steps:
        1. Start with the base case "1" for n=1.
        2. For each subsequent term, read the previous term and count consecutive digits.
        3. Construct the new term by concatenating the count and the digit.
        4. Repeat this process until reaching the nth term.
        """
        res = "1"

        for _ in range(1, n):
            new_res = ""
            i = 0
            while i < len(res):
                count = 1 #count digit
                while i +1 < len(res) and res[i] == res[i+1]:
                    i +=1
                    count +=1 #if same digit
                new_res += str(count) + res[i] #add count and digit
                print (i, res[i], new_res)
                i +=1
            res = new_res
            print("res", res)
        return res
    
    def countAndSay(self, n):
        #base case
        if n== 1:
            return "1"
        
        #we want to get previous value
        prev = self.countAndSay(n-1)
        
        res = "" #this will be used to concatenate all our previous count and say
        count =1 #this will keep track of number of instances of a number in our string

        for i in range(len(prev)):
            #need to check if our current character is equal to next character and if it is then increment the counter
            if i + 1 < len(prev) and prev[i] == prev[i+1]:
                count +=1
            else:
                res += str(count) + prev[i]
                count = 1
        return res


            
        