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

        Question: What are the k closest points to the origin?
        Intuition: The closest points to the origin can be determined by their Euclidean distance from the origin. 
        Using a heap allows us to efficiently keep track of the k smallest distances.

        Steps:
        1. Initialize an empty heap.
        2. Iterate through the list of points, calculating the distance of each point from the origin and pushing it onto the heap along with its index.
        3. Pop the smallest distance from the heap k times to get the k closest points.
        4. Append the corresponding points to the result list.
        5. Return the result list as the k closest points.

        Time Complexity: O(N * logK), where N is the number of points, due to heap operations.
        Space Complexity: O(K) for the heap storing the k closest points.
        Interview Explanation: The key insight is to use a heap to efficiently track the k closest points to the origin based on their Euclidean distance. 
        By pushing all points onto the heap and then popping the smallest distances k times, we can obtain the desired result.
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