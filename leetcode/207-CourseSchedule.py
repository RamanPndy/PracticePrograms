from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
        You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

        Return true if you can finish all courses. Otherwise, return false.

        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
        Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0. So it is possible.

        1. use visited set to add course which is completed

        TC: O(Number of nodes + pre-requisites) ie. O(N+P)
        """
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = set() #all courses along the curr DFS path

        def dfs(crs):
            if crs in visited:
                return False #visited course twice and loop detected
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs) #we no longer visiting the course or we have finished visiting the course
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True