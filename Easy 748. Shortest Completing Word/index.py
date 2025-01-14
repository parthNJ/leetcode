class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        words_dict = []
        chars=[]
        for word in words:
            freq = {}
            for char in word:
                freq[char] = freq.get(char, 0) + 1
            words_dict.append(freq)
        print(words_dict)

        counter=0
        for i in licensePlate:
            if i.isalpha():
                print(i.lower())
                while counter < len(words):
                    
        

licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
solution = Solution()
result = solution.shortestCompletingWord(licensePlate, words)