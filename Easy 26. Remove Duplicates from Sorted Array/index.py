



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=1
        print(nums)
        while right < len(nums):
            print(left, right, len(nums))
            if(nums[left] == nums[right]):
                nums.pop(right)
            else:
                right+=1
                left+=1
        return (nums)
        

nums = [0,0,0,0,3,3]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)