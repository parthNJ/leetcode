class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict,t_dict={},{}
        for i in s:
            if i in s_dict:
                s_dict[i] = s_dict[i]+1
            else:
                s_dict[i] = 1
        for j in t:
            if j in t_dict:
                t_dict[j] = t_dict[j]+1
            else:
                t_dict[j] = 1
        
        if s_dict == t_dict:
            return True
        return False
   
s = "rat"
t = "car"
solution = Solution()
result = solution.isAnagram(s, t)
print(result)