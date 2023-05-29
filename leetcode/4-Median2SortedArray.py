class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = nums1 + nums2
        l.sort()
        if len(l) % 2 == 0 :
            r = l[(len(l) - 1)//2] + l[len(l)//2]
            return r*0.5
        else:
            return l[len(l)//2]