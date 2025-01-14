class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_dict={}
        for i in magazine:
            if i not in m_dict:
                m_dict[i] = 1
            else:
                m_dict[i] = m_dict[i]+1

        for i in ransomNote:
            if i not in m_dict:
                return False
            else:
                if m_dict[i]==0:
                    return False
                elif m_dict[i] >= 1:
                    m_dict[i] = m_dict[i]-1
                else:
                    del m_dict[i]
        return True


        
ransomNote = "a"
magazine = "axhdueyhdsewxzcbhdab"
solution = Solution()
result = solution.canConstruct(ransomNote, magazine)
print(result)