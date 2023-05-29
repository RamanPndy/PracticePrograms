class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.
        """
        pos, neg, zero, res = [], [], [], set()
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zero.append(num)

        if zero:
            for n in pos:
                if -1 * n in neg:
                    res.add((n , -1*n, 0))

        if len(zero) >= 3:
            res.add((0,0,0))

        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                t = -1 * (neg[i] + neg[j])
                if t in pos:
                    res.add(tuple(sorted([neg[i], neg[j], t])))

        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                t = -1 * (pos[i] + pos[j])
                if t in neg:
                    res.add(tuple(sorted([pos[i], pos[j], t])))
        
        # print (res)
        # nums.sort()
        # for i in range(len(nums)-2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     l, r = i+1, len(nums)-1
        #     while l < r:
        #         s = nums[i] + nums[l] + nums[r]
        #         if s < 0:
        #             l +=1 
        #         elif s > 0:
        #             r -= 1
        #         else:
        #             res.add((nums[i], nums[l], nums[r]))
        #             while l < r and nums[l] == nums[l+1]:
        #                 l += 1
        #             while l < r and nums[r] == nums[r-1]:
        #                 r -= 1
        #             l += 1; r -= 1
        # return res