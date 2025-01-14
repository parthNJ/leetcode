


class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=[0]*(len(nums)+ 1) 
        
        for i in range(len(nums)):
            p[i+1] = p[i] + nums[i]
        
        count = p.count(0)-1
        return count



nums=[3,2,-3,-4]
solution = Solution()
results = solution.returnToBoundaryCount(nums)
print(results)