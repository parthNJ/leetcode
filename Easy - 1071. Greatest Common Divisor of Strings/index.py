class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        smaller = min(str1, str2)
        len_str1 = len(str1)
        len_str2 = len(str2)


        for i in range(len(smaller), 0, -1):
            if(len_str2 % i == 0 and len_str1 %  i == 0):
                str1_denominator, str2_denominator = int(len_str1/i), int(len_str2/i)
                new_str1 = smaller[0:i] * str1_denominator
                new_str2 = smaller[0:i] * str2_denominator
                if new_str1 == str1 and new_str2 == str2:
                    return min(str1[0:i], str2[0:i])
                else:
                    continue 
        return ""
            

        
str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
solution =Solution()
result = solution.gcdOfStrings(str1, str2)
print(result)