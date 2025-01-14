


class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = s.count('1')
        left=0
        total=0

        for i in range(len(s)-1):
            if(s[i] =='1'):
                right = right - 1
                
            else:
                left = left + 1
            
            tempTotal = left+right
            print(f"index{i} : {left} + {right} = {tempTotal}")
            if(tempTotal > total):
                total = tempTotal
        return total

        
        




s = "011101"
solution = Solution()
score = solution.maxScore(s)
print(score)