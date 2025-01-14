


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        loopLen = len(word1) if len(word1) > len(word2) else len(word2)

        for i in range(loopLen):
            if i < len(word1):
                output = output + word1[i]
            
            if i < len(word2):
                output = output + word2[i]
        
        return output



        

word1, word2 = "abcd", "pq"
solution = Solution()
result = solution.mergeAlternately(word1, word2)