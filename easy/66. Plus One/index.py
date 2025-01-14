"""
You are given a large integer represented as an integer array digits, where each digits[i]
is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


"""


def plusOne(digits):

    #Decent approach
    # borrow = 1
    # total_len = len(digits)-1
    # for i in range(total_len, -1, -1):
    #     if borrow == 1 and i == 0 and digits[i] == 9:
    #         digits.pop(i)
    #         digits.insert(0, 1)
    #         digits.insert(1, 0)
    #         borrow = 0
    #     elif borrow == 1 and digits[i] == 9:
    #         digits[i] = 0
    #     elif borrow == 1:
    #         digits[i] = digits[i]+1
    #         borrow = 0
    #     else:
    #         return digits
    # return digits

    #Better approach
    digits_str = []
    final = []
    for i in digits:
        digits_str.append(str(i))
    digits_num = int("".join(digits_str))
    digits_updated = str(digits_num+1)
    for j in digits_updated:
        final.append(int(j))
    print(final)

    
    
    

print(plusOne([9,9,9]))