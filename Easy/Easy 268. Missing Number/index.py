class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = (len(nums)+1)*(len(nums))/2
        for i in nums:
            total-=i
        return int(total)


        
nums = [3,5,1,4,2,6]
solution = Solution()
result = solution.missingNumber(nums)
print(result)