





def longestPalindrome(s):
    #bad approach
    # if(len(s) <= 1):
    #     return s
    # s_len = len(s)
    # temp=[]
    # for i in range(0, s_len):
    #     counter = 0
    #     temp_str = ""
    #     for j in range(i+1, s_len):
    #         if(counter == 0):
    #             temp_str = temp_str + (s[i] + s[j])
    #         else:
    #             temp_str = temp_str + s[j]
    #         counter+=1
    #         print(temp_str)
    #         if(temp_str == temp_str[::-1]):
    #             temp.append(temp_str)
    # if(temp == []):
    #     return s[0]
    # max_len = -1
    # for i in temp:
    #     if len(i) > max_len:
    #         max_len = len(i)
    #         res = i
    # return res


    #attemp 2
    if(len(s) <= 1):
        return false
    
    reversed_s = s[::-1]

            



babad
dabab

print(longestPalindrome("babad"))