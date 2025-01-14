class Solution(object):


    

    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = abs(nums[0])+1 if nums[0] < 0 else 1
        output = 0
        for i in range(len(nums)):
            if(i==0):
                output = start+nums[i]
            else:
                if (output + nums[i] < 1):
                    # get the add value
                    needToAdd = abs(output + nums[i]) + 1
                    # update the start value
                    start = start + needToAdd
                    # update the output
                    output = output + needToAdd
                    output = output + nums[i]
                else:
                    output = output+nums[i]
        return start
                    
            
            
                

                
nums = [2,3,5,-5,-1]
temp = Solution()
output = temp.minStartValue(nums)
print(output)
