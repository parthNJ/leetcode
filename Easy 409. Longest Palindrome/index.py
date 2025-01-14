class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_occurance_dict = {}
        output = 0
        placeholder = False
        for i in s:
            if i not in s_occurance_dict:
                s_occurance_dict[i] = 1
            else:
                s_occurance_dict[i] += 1

        for freq in s_occurance_dict.values():
            if freq % 2 == 0:
                output += freq
            else:
                output += freq - 1
                placeholder = True
        if placeholder:
            return output + 1
        return output
        

s = "abccccdd"   
solution = Solution()
result = solution.longestPalindrome(s)
print(result)