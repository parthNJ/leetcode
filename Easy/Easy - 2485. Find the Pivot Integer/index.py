class Solution(object):

    def preFixSum(self, a):
        output=[]
        for i in range(len(a)):
            if i == 0:
                output.append(a[0])
            else:
                output.append(output[i-1] + a[i])
        return output


    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        arrayUpToN=[i+1 for i in range(n)]
        leftSum=0
        rightSum=0
        a = self.preFixSum(arrayUpToN)

        for i in range(len(a)):
            leftSum = a[i]
            if i == 0:
                rightSum = a[len(a)-1]
            else:
                rightSum = a[len(a)-1] - a[i-1]
            if(leftSum == rightSum):
                return i+1
        return -1





class Solution2(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_sum = n * (n+1)/2
        left_sum=0
        for x in range(1, n+1):
            left_sum += x
            right_sum = total_sum - left_sum + x
            if left_sum == right_sum:
                return x
        return -1


n = 8
solution = Solution2()
result = solution.pivotInteger(n)
print(result)