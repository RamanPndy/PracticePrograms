'''
Question — Can k flowers be planted without adjacent flowers?
Problem: Given a binary array where 0 means empty and 1 means occupied, determine whether k additional 
flowers can be planted without placing flowers in adjacent positions.

Example:
Input: flowerbed = [1,0,0,0,1], k = 1
Output: True

Input: flowerbed = [1,0,0,0,1], k = 2
Output: False

Approach:
1. Initialize a counter for the number of flowers that can be planted.
2. Iterate through the flowerbed array.
   a. If the current position is empty and both adjacent positions are empty or out of bounds, 
   plant a flower and increment the counter.
   b. Skip the next position to avoid adjacent planting.
3. After iterating through the array, check if the counter is greater than or equal to k.
4. Return True if k flowers can be planted, otherwise return False.

Why this works:
The algorithm works by iterating through the flowerbed and planting flowers only in positions where both adjacent 
positions are empty or out of bounds. 
By skipping the next position after planting a flower, it ensures that no two flowers are adjacent. 
The final count of planted flowers is then compared with k to determine if it is possible to plant k flowers without 
violating the adjacency rule.

Time Complexity: O(n), where n is the length of the flowerbed array.
Space Complexity: O(1), as no additional space is used apart from the counter.
'''

def can_place_flowers(flowerbed, k):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
            i += 1  # Skip the next position to avoid adjacent planting
        i += 1
    return count >= k 

# Example usage:
flowerbed = [1,0,0,0,1]
k = 1
print(can_place_flowers(flowerbed, k))  # Output: True

flowerbed = [1,0,0,0,1]
k = 2
print(can_place_flowers(flowerbed, k))  # Output: False