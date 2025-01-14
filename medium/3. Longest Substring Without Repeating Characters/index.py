"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""




class Solution(object):

    def lengthOfLongestSubstring(self, s):
        tempObj = []
        tempObjLengths = []
        if len(s) == 1:
            return 1
        for i in s:
            if i in tempObj:
                tempObjLengths.append(len(tempObj))
                tempObj = []
                tempObj.append(i)
            else:
                tempObj.append(i)
                if len(tempObj) >= len(s):
                    return len(tempObj)
        return max(tempObjLengths)


temp = Solution()
x = temp.lengthOfLongestSubstring("zxyzopmbpx")
print(x)  


    # def lengthOfLongestSubstring(self, s):
    #     tempObj = []
    #     tempObjLengths = []

    #     if len(s) == 1:
    #         return 1
    #     counter  = 0
    #     for i in s:
    #         print(i)
    #         print(tempObj)
    #         if i in tempObj:
    #             tempObjLengths.append(len(tempObj))
    #             tempObj = []
    #             tempObj.append(i)
    #         else:
    #             tempObj.append(i)
    #             if(counter == len(s)):
    #                 tempObjLengths.append(len(tempObj))
    #                 return (lambda tempObjLengths: max(tempObjLengths) if len(tempObjLengths) >= 1 else 0 )(tempObjLengths)
    #     return(lambda tempObjLengths: max(tempObjLengths) if len(tempObjLengths) >= 1 else 0 )(tempObjLengths)




