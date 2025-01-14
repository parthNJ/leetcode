



class Solution(object):

    def is_english_character(slef, char):
        if len(char) != 1:
            raise ValueError("Input must be a single character.")
        return ('A' <= char <= 'Z') or ('a' <= char <= 'z')


    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        left,right= 0,len(s_list)-1

        while left < right:
            if not self.is_english_character(s_list[left]):
                left+=1
            elif not self.is_english_character(s_list[right]):
                right-=1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left+=1
                right-=1
        return "".join(s_list)

s = "Test1ng-Leet=code-Q!"
solution = Solution()
result = solution.reverseOnlyLetters(s)
print(result)