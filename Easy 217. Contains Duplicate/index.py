# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         nums_freq={}
#         for i in nums:
#             nums_freq[i] = nums_freq.get(i, 0) + 1
        
#         for freq in nums_freq.values():
#             if freq >= 2:
#                 return True
#         return False

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        

nums=[1,1,1,3,3,4,3,2,4,2]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)