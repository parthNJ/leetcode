""" 
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

"""


def isPalindrome(x):
    if (x < 0 or x % 10 == 0):
        return False
    
    temp = 0
    while x > temp:
        temp = (temp * 10) + (x % 10)
        x = x // 10
    
    return x == temp or x == temp // 10




    # Approach 1 - converting to a string
    # str_x = str(x)
    # str_x_reversed = str_x[::-1]
    # if(str_x == str_x_reversed):
    #     return True
    # return False


print(isPalindrome(121))