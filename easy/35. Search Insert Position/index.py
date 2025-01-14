""" 
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""


def searchInsert(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        half = (low+high) // 2
        if nums[half] < target:
            low = half + 1
        elif nums[half] > target:
            high = half - 1
        else:
            return half
    return high + 1


print(searchInsert([1, 3, 4, 7, 8, 10, 12, 14, 15, 32, 45, 47, 55], 454))