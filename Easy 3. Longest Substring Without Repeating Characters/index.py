class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub=[]
        t_counter=0
        counter=1
        for i in range(len(s)):
            print(i, counter, t_counter, sub)
            if i+1 == len(s)-1:
                greater = counter if counter >= t_counter else t_counter
                return greater
            elif s[i] in sub:
                t_counter = len(sub)
                sub=[]
                sub.append(s[i])
                counter=1
            else:
                counter+=1
                sub.append(s[i])
            print(i, counter, t_counter, sub)
        return t_counter
        

                



s = "ab"
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)
        