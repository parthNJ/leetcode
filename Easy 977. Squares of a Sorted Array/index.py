class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        output=[0]* len(nums)
        counter=len(nums)-1
        while left <= right:
            if (abs(nums[left]) < abs(nums[right])):
                output[counter] = nums[right]*nums[right]
                right-=1
            else:
                output[counter] = nums[left]*nums[left]
                left+=1
            counter-=1
        return output
            

        


nums = [-7,-3,2,3,11]
solution = Solution()
result = solution.sortedSquares(nums)
print(result)