class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        right=k
        if len(nums) < k:
            return 0
        max_sum = current_sum = sum(nums[:k])
        for i in range(1, len(nums)):
            if right < len(nums):
                current_sum = (current_sum - nums[i-1]) + nums[right]
                max_sum =max(current_sum, max_sum)
                right+=1
        return max_sum / float(k)

        

nums = [5]
k = 1
solution = Solution()
result = solution.findMaxAverage(nums, k)
print(result)