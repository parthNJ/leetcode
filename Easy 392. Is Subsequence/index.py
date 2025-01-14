




class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        right=0
        right_found=""
        for i in range(0, len(s)):
            looking_for=s[i]
            while(right < len(t) and t[right] != looking_for):
                right+=1
            
            if(right < len(t) and t[right] == looking_for):
                right_found+=t[right]
                right+=1
        if s == right_found:
            return True
        return False
        


s = "aec"
t = "abcde"
solution = Solution()
result = solution.isSubsequence(s, t)
print(result)