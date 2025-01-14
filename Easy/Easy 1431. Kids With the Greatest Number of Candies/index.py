






class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output=[]
        high = max(candies)
        for candy in candies:
            if (candy + extraCandies >= high):
                output.append(True)
            else:
                output.append(False)
        return output


        
                



candies  = [12,1,12]
extraCandies = 10
solution = Solution()
result = solution.kidsWithCandies(candies, extraCandies)
print(result)


        


