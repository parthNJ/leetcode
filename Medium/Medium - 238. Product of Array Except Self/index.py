class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        preFixSum=[]
        postFixSum=[]
        left=1
        right=1
        
        for i in range(len(nums)):
            if(i==0):
                preFixSum.append(nums[i])
            else:
                preFixSum.append(preFixSum[i-1] * nums[i])
        
        for i in range(len(nums),0,-1):
            if(i==len(nums)):
                postFixSum.insert(0,nums[len(nums)-1])
            else:
                postFixSum.insert(0, postFixSum[0]*nums[i-1])

        output=[]
        for i in range(len(nums)):
            if i == 0:
                left = 1
                right = postFixSum[i+1]
            elif(i == len(nums)-1):
                left = preFixSum[i-1]
                right = 1
            else:
                left = preFixSum[i-1]
                right = postFixSum[i+1]
            output.append(left*right)
        return output
    


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        

nums = [1,2,3,4]
solution = Solution()
result = solution.productExceptSelf(nums)
print(result)