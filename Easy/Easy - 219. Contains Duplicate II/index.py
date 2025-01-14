class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict={}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                if abs(nums_dict[nums[i]] - i) <= k:
                    return True
                else:
                    nums_dict[nums[i]] = i
            else:
                nums_dict[nums[i]] = i
        return False


        
nums = [1,2,3,1,2,3]
k = 2
solution = Solution()
result = solution.containsNearbyDuplicate(nums, k)
print(result)