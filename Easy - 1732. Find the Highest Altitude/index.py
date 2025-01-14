class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        if len(gain) > 0:
            higestAltitude=0
            p = [0] * (len(gain) + 1)
            for i in range(len(gain)):
                # p[i+1] = p[i] + gain[i]
                if(p[i+1] > higestAltitude):
                    higestAltitude = p[i+1]
            return higestAltitude
        else:
            return 0


# Time Complexity O(n)


gain=[-5,1,5,0,-7]
classObj = Solution()
output = classObj.largestAltitude(gain)
print(output)
        