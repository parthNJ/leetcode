class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        else:
            if(len(flowerbed) == 1):
                if flowerbed[0] == 0:
                    return True
                return False
            
            prev = 0
            next = flowerbed[1]
            counter = 0
            for i in range(len(flowerbed)):
                if counter == n:
                    return True
                next = 0 if (i + 1 >= len(flowerbed)) else flowerbed[i + 1]
                if prev == 0 and flowerbed[i] == 0 and next == 0:
                    flowerbed[i] = 1
                    prev = 1
                    counter += 1
                else:
                    prev = flowerbed[i]
                    next = 0 if (i + 1 >= len(flowerbed)) else flowerbed[i + 1]
            if counter == n:
                return True
            return False


        
        
flowerbed = [1]
n = 0
solution = Solution()
result = solution.canPlaceFlowers(flowerbed, n)
print(result)