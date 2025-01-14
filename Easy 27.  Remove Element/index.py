


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            if nums[left] == val:
                nums.pop(left)
                right = right-1
            else:
                left=left+1
        return len(nums)

        
nums = [0,1,2,2,3,0,4,2]
val = 2
solution = Solution()
result = solution.removeElement(nums, val)
print(result)