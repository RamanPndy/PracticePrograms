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

        Question: What is the smallest number that can be constructed from the given pattern?
        Intuition:
        - We can use a stack to keep track of the numbers and ensure the pattern is followed.
        - For each "D" in the pattern, we push the current number onto the stack.
        - For each "I" in the pattern, we push the current number onto the stack and then pop all elements from the stack to the answer string.
        - For example, for the pattern "IIIDIDDD", the stack helps in reversing the numbers for "D" sequences to maintain the decreasing order.
        - This approach ensures that the smallest possible number is constructed while adhering to the "I" and "D" pattern.
        - The stack temporarily holds numbers to reverse their order when a "D" is encountered, ensuring the decreasing sequence is correctly formed.
        Time Complexity: O(n) where n is the length of the pattern.
        Space Complexity: O(n) for the stack.
        Approach:
        - Initialize an empty stack and set the current number to 1.
        - Traverse the pattern:
            - If the current character is "D", push the current number onto the stack and increment the number.
            - If the current character is "I", push the current number onto the stack, increment the number, and pop all elements from the stack to the answer string.
        - After traversing the pattern, push the last number onto the stack and pop all elements to the answer string.
        - Return the answer string as the smallest number that meets the pattern.
        Steps:
        1. Initialize an empty stack and set the current number to 1.
        2. Traverse the pattern:
            - If the current character is "D", push the current number onto the stack and increment the number.
            - If the current character is "I", push the current number onto the stack, increment the number, and pop all elements from the stack to the answer string.
        3. After traversing the pattern, push the last number onto the stack and pop all elements to the answer string.
        4. Return the answer string as the smallest number that meets the pattern.
        """
        stack = []
        ans = ""
        num = 1
        for ch in pattern:
            if ch == "D":
                stack.append(str(num))
                num += 1
            else:  # ch == "I"
                stack.append(str(num))
                num += 1
                while stack:
                    ans += stack.pop()
        stack.append(str(num))
        while stack:
            ans += stack.pop()
        return ans