"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

"""


def strStr(haystack, needle):
     for x, y in enumerate(haystack):
          print(x, y)
    # if(haystack == needle):
    #     return 0
    # for i in range(0, len(haystack)):
    #     remainingLength = len(haystack) - i
    #     # print("remainingLength", remainingLength)
    #     if(remainingLength >= len(needle)):
    #         # print("value", haystack[i: i + len(needle)])
    #         if(haystack[i: i + len(needle)] == needle):
    #             return i
    #     else:
    #         return -1
    # else:
    #     return -1

print(strStr("mississippi", "a"))