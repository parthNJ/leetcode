



class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[0]*(len(nums) + 1)
        for i in range(len(nums)):
            p[i+1] = p[i] + nums[i]
        
        p.remove(0)
        return p
        

nums=[3,1,2,10,1]
solution = Solution()
result = solution.runningSum(nums)
print(result)

