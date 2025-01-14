


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=len(s)-1
        right=len(s)-1
        output=[]
        while left >= 0:
            word=""
            if(s[left] != " "):
                right = left
            while left >= 0 and s[left] != " ":
                word = s[left:right+1]
                left = left-1
            left = left-1
            if(len(word) >= 1):
                output.append(word)
        return " ".join(output)

                
            
            
        

s="the sky is blue"
solution = Solution()
result = solution.reverseWords(s)
print(result) 