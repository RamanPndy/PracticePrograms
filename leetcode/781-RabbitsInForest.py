class Solution(object):
    '''
    There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" 
    and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
    Given the array answers, return the minimum number of rabbits that could be in the forest.

    Input: answers = [1,1,2]
    Output: 5
    Explanation:
    The two rabbits that answered "1" could both be the same color, say red.
    The rabbit that answered "2" can't be red or the answers would be inconsistent.
    Say the rabbit that answered "2" was blue.
    Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
    The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
    Question: Find the minimum number of rabbits that could be in the forest based on the given answers.
    Intuition: Rabbits that give the same answer can be grouped together, 
    and each group must have at least the number of rabbits indicated by the answer plus one.
    Steps:
    1. Initialize a frequency dictionary to count the occurrences of each answer.
    2. Initialize a count variable to keep track of the minimum number of rabbits.
    3. Iterate through each answer in the answers array:
        - If the answer is 0, increment the count by 1.
        - Otherwise, check if the answer is not in the frequency dictionary or if the frequency has reached the answer value:
            - If so, initialize the frequency for this answer to 0 and increment the count by answer + 1.
        - Increment the frequency for this answer.
    4. Return the count as the minimum number of rabbits in the forest.
    Time Complexity: O(n), where n is the length of the answers array, as we iterate through the array once.
    Space Complexity: O(n) for the frequency dictionary in the worst case when all answers are unique.
    Interview Explanation: The key insight is to recognize that rabbits giving the same answer can be grouped together, 
    and each group must have at least the number of rabbits indicated by the answer plus one. 
    By keeping track of the frequency of each answer and starting a new group when necessary, 
    we can calculate the minimum number of rabbits in the forest.
    '''
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        freq = dict()
        count = 0
        for i in answers:
            if i == 0:
                count +=1
            else:
                # Check if we need to start a new group for this answer.
                if i not in freq or i == freq[i]:
                    freq[i] = 0
                    count += i + 1
                else:
                    # Start a new group for this answer.
                    freq[i] += 1
        return count
        
# 1, 2, 2,3
# red = 2
# green = 2 + 1
# blue = 4

# 1,2,2,2,2,0,3
# red=2
# blue = 3
# green = 3
# yellow= 1
# black = 4