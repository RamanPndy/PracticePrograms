class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        Input: path = "/home/"
        Output: "/home"
        Explanation: Note that there is no trailing slash after the last directory name.

        Input: path = "/../"
        Output: "/"
        Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

        Input: path = "/home//foo/"
        Output: "/home/foo"
        Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

        1. The problem can be solved using a stack to keep track of the directories in the path. 
        2. We split the input path by slash '/'
        3. iterate over the directories, and perform the following operations:
            1. Ignore the current directory '.' and empty directories.
            2. Go one level up for double period '..' by popping the top element from the stack if it is not empty.
            3. For any other directory, push it to the stack.
        4. Finally, we join the directories in the stack with slash '/' and 
            add a slash at the beginning to form the simplified canonical path.
        """
        stack = []
        directories = path.split('/')
        for dir in directories:
            if dir == "." or not dir:
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/' + '/'.join(stack)