"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

def longestCommonPrefix(strs):
    if(len(strs) == 0):
            return ""
    first = strs[0]
    for i in range(len(first)):
        for word in strs[1:]:
            if(i == len(word) or word[i] != first[i]):
                return first[0:i]
    return first




print(longestCommonPrefix(["ab","a"]))