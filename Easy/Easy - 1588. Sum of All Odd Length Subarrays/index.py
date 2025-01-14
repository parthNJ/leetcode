class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        pre_fix,post_fix=[],[]
        for i in range(len(arr)):
            if(i==0):
                pre_fix.append(arr[i])
            else:
                pre_fix.append(arr[i]+pre_fix[i-1])
        
        for i in range(len(arr)-1,-1,-1):
            if(i==len(arr)-1):
                post_fix.append(arr[i])
            else:
                post_fix.insert(0, arr[i]+post_fix[0])
        print(pre_fix, post_fix)

        output=[]
        for i in range(len(arr)):
            output.append(i)
            if i != 0 or i != len(arr):
                if i % 3 == 0:
                    output.append(pre_fix[i-1])
                    output.append(post_fix[i-1])
        print(output)
                



        

arr = [1,4,2,5,3]
solution = Solution()
result = solution.sumOddLengthSubarrays(arr)