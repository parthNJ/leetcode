class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        counter=0
        for i in range(len(s)):
            if (i+1 < len(s) and s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")):
                counter = counter-roman[s[i]]
            elif(i+1 < len(s) and s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")):
                counter = counter-roman[s[i]]
            elif(i+1 < len(s) and s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M")):
                counter = counter-roman[s[i]]
            else:
                counter=counter+roman[s[i]]
        return counter

        

s = "XLIX"
solution = Solution()
result =solution.romanToInt(s)
print(result)