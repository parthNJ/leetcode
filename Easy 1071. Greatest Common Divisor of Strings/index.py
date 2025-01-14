



class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        if(len(str1) < len(str2)):
            smallerStr = str1
            biggerStr = str2
        elif(len(str1) > len(str2)):
            smallerStr = str2
            biggerStr = str1
        else:
            smallerStr = str2
            biggerStr = str1

        for i in range(len(smallerStr)):
            sub = smallerStr[0:len(smallerStr)-i]
            remainingFromSmall = smallerStr[len(smallerStr)-i:len(smallerStr)]
            if(len(biggerStr) % len(sub) == 0):
                counter=0
                for j in range(0, len(biggerStr), len(sub)):
                    if(biggerStr[j:j+len(sub)] != sub):
                        break
                    else:
                        counter = counter+1
                        if(j + len(sub) >=  len(biggerStr) and (len(smallerStr) % len(sub) == 0)):
                            print(f"sub - {sub} remaining-{remainingFromSmall}")
                            if(len(remainingFromSmall) < 1):
                                return sub
                            else:
                                for k in range(0, len(remainingFromSmall), len(sub)):
                                    print(remainingFromSmall[k:k+len(sub)])
                                    if(remainingFromSmall[k:k+len(sub)]) != sub and len(remainingFromSmall) > 1:
                                        print()
                                        break
                                    else:
                                        return sub
                                
            else:
                continue
        return ""
        
           


str1 = "AAAAAAAAA"
str2 = "AAACCC"
solution = Solution()
result = solution.gcdOfStrings(str1, str2)
print(result)