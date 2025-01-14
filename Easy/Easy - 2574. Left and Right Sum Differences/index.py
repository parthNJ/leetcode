class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=0
        right=sum(nums) - nums[0]
        output = []
        
        for i in range(len(nums)):
            output.append(abs(left - right))
            left = left + nums[i]
            if(i+1 < len(nums)):
                right = right - nums[i+1]
            else:
                right = right - 0
        return output
            





nums=[1]
solution = Solution()
result = solution.leftRightDifference(nums)
print(result)