


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(len(nums)/2)
        value=None
        counter=0
        for i in nums:
            if(counter==0):
                value=i
            if i == value:
                counter += 1
            else:
                counter -= 1
        return value
        

nums = [2,2,1,1,1,2,2]
solution = Solution()
result = solution.majorityElement(nums)
print(result)