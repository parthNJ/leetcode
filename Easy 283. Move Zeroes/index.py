



class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        
        while left < right:
            if nums[left] == 0:
                nums.pop(left)
                right = right -1
                nums.append(0)
            else:
                left = left + 1
        return nums
        

nums=[0,5,4,5,3,4,5,6,0,0]
solution = Solution()
result = solution.moveZeroes(nums)
print(result)