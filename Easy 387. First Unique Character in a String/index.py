class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_freq_dict={}
        for i in s:
            s_freq_dict[i] = s_freq_dict.get(i, 0) + 1
        
        for index, char in enumerate(s):
            if s_freq_dict[char] == 1:
                return index
        return -1

s="loveleetcode"
solution = Solution()
result = solution.firstUniqChar(s)
print(result)
