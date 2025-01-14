



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        counter=0
        for right in range(len(nums)):
            if(nums[left] == nums[right]):
                counter+=1
                if(counter>2):
                    nums[right], nums[-1] = nums[-1], nums[right]
                    nums.pop()
                    left=right
            else:
                counter=1
                left=right
        print(nums)



nums = [0,0,0,1,1,1,1,1,2,2,2,3,3]
solution = Solution()
result = solution.removeDuplicates(nums)
