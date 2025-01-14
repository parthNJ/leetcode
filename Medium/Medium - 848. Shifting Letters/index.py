


class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        postFixSum = []
        output_str=""
        for i in range(len(shifts), 0, -1):
            if i == len(shifts):
                postFixSum.append(shifts[len(shifts)-1])
                new_char_value = (ord(s[i-1])-ord('a'))+shifts[len(shifts)-1]
                char_position = new_char_value % 26
                output_str+=chr(ord('a')+ char_position)
            else:
                test = (ord(s[i-1])-ord('a')+ (shifts[i-1]+postFixSum[0]))
                new_char = test % 26
                output_str+=chr(ord('a')+ new_char)
                postFixSum.insert(0, shifts[i-1]+postFixSum[0])
        return output_str[::-1]
                
       
            
        
            

s = "axc"
shifts = [3,5,9]
solution = Solution()
result = solution.shiftingLetters(s, shifts)