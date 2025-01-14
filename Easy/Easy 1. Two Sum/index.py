

class Solution(object):
    def twoSum(self, nums, target):
        memory = {}
        for i in range(0, len(nums)):
            missingValue = target - nums[i]
            if missingValue in memory:
                return ([memory[missingValue],i])
            else:
                memory[nums[i]] = i