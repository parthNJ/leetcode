

def isValid(s):
    bracket_options = {"(":")", "{": "}", "[": "]"}
    temp=[]
    for i in s:
        if i in bracket_options:
            temp.append(bracket_options[i])
        else:
            if temp[-1] != i:
                return False
            else:
                temp.pop()
    if len(temp) >= 1:
        return False
    return True


    




print(isValid("([)]"))

# isValid("[[]()}")


