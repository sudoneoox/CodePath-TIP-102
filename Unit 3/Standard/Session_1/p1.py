def is_valid_post_format(posts):
    if len(posts) == 0:
        return False

    stack_1 = []
    for ch in posts:
        if ch == "(" or ch == "[" or ch == "{":
            stack_1.append(ch)
        else:
            if not stack_1:
                return False
            elif ch == ")" and stack_1[-1] == "(":
                stack_1.pop()
            elif ch == "}" and stack_1[-1] == "{":
                stack_1.pop()
            elif ch == "]" and stack_1[-1] == "[":
                stack_1.pop()
            else:
                return False

    return len(stack_1) == 0


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))
print(is_valid_post_format("((()))"))
print(is_valid_post_format("(()"))
print(is_valid_post_format("(()())"))
print(is_valid_post_format("))))(((("))
