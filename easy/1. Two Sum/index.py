

"""
Difficulty : Easy
Method : Hash map dictionary - memory
Approach : Start at the start of the array and iterate till the end, find the missingValue 
that would add up to the target value. Once that value is found check to see if we've seen it before in our dictionary. If we've seen it return the value - stored as an index.
If we have not seen that value then add the current index into out memory hash as key value pair, where key is the nums[i] and value is the curretn index. 
"""
def twoSum(nums, target):
    memory = {}
    for i in range(0, len(nums)):
        missingValue = target - nums[i]
        if missingValue in memory:
            return ([memory[missingValue],i])
        else:
            memory[nums[i]] = i

#case 1
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

#case 2
nums = [2,4,9,6,5]
target = 10
print(twoSum(nums, target))

#case 3
nums = [2,23,32,44,7,4,5,6,7]
target = 6
print(twoSum(nums, target))