class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        new_Word=[]
        for i in range(len(s)):
            if(i == len(s)-1):
                new_Word.append(s[left:i+1][::-1])
            if(s[i] == " "):
                new_Word.append(s[left:i][::-1])
                left = i+1
        return " ".join(new_Word)
                

            
        

s = "Let's take LeetCode contest"
solution = Solution()
result = solution.reverseWords(s)