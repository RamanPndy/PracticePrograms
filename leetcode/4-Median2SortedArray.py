class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.
        """
        l = nums1 + nums2
        l.sort()
        if len(l) % 2 == 0 :
            r = l[(len(l) - 1)//2] + l[len(l)//2]
            return r*0.5
        else:
            return l[len(l)//2]
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.
        1)take an newarray and assign two variables i,j to traverse the nums1,nums2 let m=len(nums1) and n=len(nums2)
        2)execute the while loop until i<=m and j<=n for traversal and adding the elements into the new array
        3)if nums1[i]<nums2[j] implies the nums1[i] is less than nums2[j]
          we add the smaller element into the new array(the concept which we use to merge two arrays in merge sort)
        4)after completing the while loop there may be a chance for len(nums1)<len(nums2) or len(nums2)>len(num1) 
          consider as case1,case2
          so we had used two more while loops one for case 1 and other for case 2
        6)after the loops we get the sorted newarray.find the median of the sorted array 
        if len(newarray) is odd return(newarray[mid]/2)
        if len(newarray) is even return median by return((newarray[mid-1]=newarray[mid],2))
        TC: O(m + n)
        SC: O(1)
        """
        m=len(nums1)-1
        n=len(nums2)-1
        new=[]
        i,j=0,0
        while i<=m and j<=n:
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i=i+1
            else:
                new.append(nums2[j])
                j=j+1
        while(i<=m):
            new.append(nums1[i])
            i=i+1
        while(j<=n):
            new.append(nums2[j])
            j=j+1
        median=len(new)
        i=median//2
        if median%2==0:
            median=(new[i-1]+new[i])/2
        else:
            median=new[i]
        return median

    def findMedianSortedArrays(self,nums1, nums2):
        '''
        TC : O(log (m+n))
        '''
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
        
class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    '''
    # Time: O(logmin(m,n))
    # Space: O(1) 
    '''
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
      return self.findMedianSortedArrays(nums2, nums1)

    l = 0
    r = n1

    while l <= r:
      partition1 = (l + r) // 2
      partition2 = (n1 + n2 + 1) // 2 - partition1
      maxLeft1 = -2**31 if partition1 == 0 else nums1[partition1 - 1]
      maxLeft2 = -2**31 if partition2 == 0 else nums2[partition2 - 1]
      minRight1 = 2**31 - 1 if partition1 == n1 else nums1[partition1]
      minRight2 = 2**31 - 1 if partition2 == n2 else nums2[partition2]
      if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
        return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5 if (n1 + n2) % 2 == 0 else max(maxLeft1, maxLeft2)
      elif maxLeft1 > minRight2:
        r = partition1 - 1
      else:
        l = partition1 + 1
