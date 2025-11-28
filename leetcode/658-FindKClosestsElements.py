class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        Example 1:
            Input: arr = [1,2,3,4,5], k = 4, x = 3
            Output: [1,2,3,4]

        Example 2:
            Input: arr = [1,1,2,3,4,5], k = 4, x = -1
            Output: [1,1,2,3]

        Explaination:
        1. if array is not sorted then sort the array
        2. get the length of the array
        3. if x <= first element of the sorted array then return array elements upto k
        4. if x >= last element of the sorted array then return array elements from n-k
        5. perform binary search
            a. set low to 0 and high to len(arr) -k
            b. while low < high:
                mid = (low + high) // 2
                if x - mid of arr is greater than mid + k of arr - x then set low = mid + 1
                else set high = mid
            c. return arr of low to low + k
        """
        sortedarr = sorted(arr)
        n = len(sortedarr)
        if (x <= sortedarr[0]):
            return arr[:k]
        if (x >= sortedarr[n-1]):
            return arr[n-k:]
        low, high = 0, len(arr)-k
        while low<high:
            mid = (low + high)//2
            if x-arr[mid]>arr[mid+k]-x:
                low = mid + 1
            else:
                high = mid
        return arr[low:low+k]
        