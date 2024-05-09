# Given a 2D array with integers(both negaitive and positive)
# operation: multiply any 2 adjancent elements with -1
# any number of times
# find the maximum sum possible
# -5 1 2
# 1 -2 1
# 4  3 1

def max_sum_after_operations(arr):
    rows, cols = len(arr), len(arr[0])
    
    # Initialize a DP table to store the maximum sum
    dp = [[0] * cols for _ in range(rows)]
    
    # Fill the first row of DP table
    dp[0] = [abs(arr[0][i]) if i % 2 == 0 else -abs(arr[0][i]) for i in range(cols)]
    
    # Iterate through the rest of the rows
    for i in range(1, rows):
        for j in range(cols):
            # Calculate the maximum sum for each cell based on the previous row
            if j == 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]) + abs(arr[i][j])
            elif j == cols - 1:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + abs(arr[i][j])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + abs(arr[i][j])
    
    # The maximum sum will be in the last row of the DP table
    return max(dp[-1])

# Example usage
arr = [
    [-5, 1, 2],
    [1, -2, 1],
    [4, 3, 1]
]
result = max_sum_after_operations(arr)
print("Maximum sum after operations:", result)
