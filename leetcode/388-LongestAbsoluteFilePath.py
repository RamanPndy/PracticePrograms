class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        Question: Find the length of the longest absolute path to a file in the given file system string.
        Approach: 
        1. Use a stack to keep track of the current path length at each depth level.
        2. Split the input by newline characters to process each file or directory.
        3. For each item, determine its depth by counting the leading tab characters.
        4. If the item is a file, update the maximum length using the current path length.
        5. If the item is a directory, update the stack with the new path length.

        Why this works: By maintaining the path length at each depth level, we can efficiently compute the 
        absolute path length for each file without reconstructing the entire path.

        Time Complexity: O(n) where n is the length of the input string.
        Space Complexity: O(d) where d is the maximum depth of the directory structure.
        """
        stack = [0]  # stack to store the current path length at each depth
        max_len = 0
        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')
            while depth + 1 < len(stack):
                stack.pop()
            if '.' in name:
                max_len = max(max_len, stack[-1] + len(name))
            else:
                stack.append(stack[-1] + len(name) + 1)
        return max_len