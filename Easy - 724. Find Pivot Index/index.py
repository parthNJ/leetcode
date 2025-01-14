

"""
    This function finds the "middle index" in an array where the sum of all numbers 
    to the left of the index is equal to the sum of all numbers to the right of the index. 
    If no such index exists, the function returns -1.

    Steps:
    1. Initialize two variables:
        - `left` to track the sum of elements to the left of the current index (initially 0).
        - `right` to track the sum of elements to the right of the current index 
            (initially the total sum of the array).

    2. Iterate through the array:
        - For each index `i`, update `right` by subtracting the current element `nums[i]`.
        - Check if `left` is equal to `right`:
            - If true, return the current index `i` as the middle index.
        - Otherwise, update `left` by adding the current element `nums[i]`.

    3. If no middle index is found after checking all indices, return -1.

    Example:
    For nums = [2, 3, -1, 8, 4]:
    - At i = 3, left = 4 and right = 4, so the function returns 3.

    Edge Cases:
    - If nums is empty, return -1.
    - If nums contains only one element, return 0 because left and right sums are 0.
        """

class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=sum(nums)

        for i in range(len(nums)):
            right = right - nums[i]
            if(left == right):
                return i
            else:
                left = left + nums[i]
        return -1
            
        


nums=[1,2,3]
temp = Solution()
middleIndex = temp.findMiddleIndex(nums)
print(middleIndex)