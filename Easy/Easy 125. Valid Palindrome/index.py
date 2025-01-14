import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left=0
        right=len(s)-1

        while left <= right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
        
s = "A man, a plan, a canal: Panama"
solution = Solution()
result = solution.isPalindrome(s)
print(result)