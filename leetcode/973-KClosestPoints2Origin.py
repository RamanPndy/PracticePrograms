import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        Input: points = [[1,3],[-2,2]], k = 1
        Output: [[-2,2]]
        Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

        TC: O(N * logK)
        SC: O(K)
        Steps:
            - make a maximum-heap to store distance, (point's distance to original, point)
            - each time call heapq.heappop (distance), it will pop the smallest item in the heap. 
            So heappop K times will be the result.
        """
        heap = []
        for i, (x,y) in enumerate(points):
            dist = (x**2 + y**2)
            heapq.heappush(heap,(dist, i))
        K_points = []
        for i in range(k):
            dist,i = heapq.heappop(heap)
            K_points.append(points[i])
        return K_points