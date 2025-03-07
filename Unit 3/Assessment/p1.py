"""
Given a string containing just characters (,),{,},[,]
determine if input string is valid
"""


def is_valid(s):
    valid_stack = []
    for char in s:
        if char == "(" or char == "[" or char == "{":
            valid_stack.append(char)
        else:
            if len(valid_stack) == 0:
                return False
            elif char == ")" and valid_stack[-1] == "(":
                valid_stack.pop()
            elif char == "}" and valid_stack[-1] == "{":
                valid_stack.pop()
            elif char == "]" and valid_stack[-1] == "[":
                valid_stack.pop()
            else:
                return False

    return len(valid_stack) == 0
