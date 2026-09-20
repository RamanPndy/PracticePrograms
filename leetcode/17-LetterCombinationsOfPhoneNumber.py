class Solution(object):
    def letterCombinations(self, digits):
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
        Return the answer in any order.
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        Question: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
        Approach:
        - Use a queue to perform a breadth-first search (BFS) to generate all possible combinations.
        - Start with an initial element (0, "") in the queue, where 0 is the index and "" is the current combination.
        - For each element in the queue, if the index equals the length of the digits, add the combination to the result.
        - Otherwise, get the next digit and its corresponding letters, and append new elements to the queue with updated index and combination.
        Time Complexity: O(4^n) where n is the length of the digits string (since the maximum number of letters for a digit is 4).
        Space Complexity: O(4^n) for storing the combinations in the queue and result list.
        Steps:
        1. create a dictionary having key as phone number digit and value as respective string
        2. create a result array and queue
        3. append (0, "") in the queue
        4. traverse through queue
            - pop the first element from queue which will return index and character
            - if index is length(digits) then append character in result array
            - else 
                i. get next digit from digits i.e. from current index which is digits[i]
                ii. get all letters from the phone number dictionary for next digit found in above step
                iii. traverse each letter and append it to queue along with (index + 1, character + letter)
        r. return result array
        """
        if not digits:
            return []

        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        q = []
        q.append((0, ""))
        while q:
            i, c = q.pop(0)
            if i == len(digits):
                res.append(c)
            else:
                nextDigit = digits[i]
                letters = m[nextDigit]
                for letter in letters:
                    q.append((i+1, c + letter))
        return res