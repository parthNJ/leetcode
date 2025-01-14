class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        last_found = None
        left=0
        output=[]
        for i in range(len(s)):
            print(f"i:{i} left:{left} last:{last_found}")
            if(s[i] == c):
                while left <= i:
                    if(last_found != None and (abs(last_found-left) <= abs(left-i))):
                        output.append(abs(last_found-left))
                        print(f"---- LEFT adding {s[left]} at index{i} with {abs(last_found-left)}")
                    else:
                        output.append(abs(left-i))
                        print(f"---- RIGHT adding {s[i]} at index{i} with {abs(left-i)}")
                    left+=1
                    last_found=i
            
        print(output)
        

s = "adasjdjfw" 
c = "j"
solution = Solution()
result = solution.shortestToChar(s, c)