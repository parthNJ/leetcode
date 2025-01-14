

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=("A","E","I","O","U","a","e","i","o","u")
        left=0
        right=len(s)-1
        a=list(s)
        while left < right:
            while left < right and a[left] not in vowel:
                left+=1
            while left < right and a[right] not in vowel:
                right-=1

            tempLeft = a[left]
            tempRight = a[right]
            a[left] = tempRight
            a[right] = tempLeft
            left+=1
            right-=1
        return "".join(a)



s = "leetcode"
solution = Solution()
result = solution.reverseVowels(s)
print(result)