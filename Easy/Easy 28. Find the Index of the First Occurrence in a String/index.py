class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(0, len(haystack)):
            sub= haystack[i:i+len(needle)]
            if(sub==needle):
                return i
        return -1
        

haystack = "mississippi" 
needle = "issi"
solution = Solution()
result = solution.strStr(haystack, needle)
print(result)