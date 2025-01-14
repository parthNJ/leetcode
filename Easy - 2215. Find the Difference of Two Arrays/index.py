class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums_1_set = set(nums1)
        nums_2_set = set(nums2)
        left,right,overall = [],[],[]
        for i in nums_1_set:
            if i not in nums_2_set:
                left.append(i)
        
        for j in nums_2_set:
            if j not in nums_1_set:
                right.append(j)
        
        overall.append(left)
        overall.append(right)
        return overall



        
nums1 = [0]
nums2 = [1]
solution = Solution()
result = solution.findDifference(nums1, nums2)
print(result)