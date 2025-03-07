def post_compare(draft_1, draft_2):
    stack_1 = []
    stack_2 = []

    for ch in draft_1:
        if ch == "#" and len(stack_1) != 0:
            stack_1.pop()
        else:
            stack_1.append(ch)

    for ch in draft_2:
        if ch == "#" and len(stack_2) != 0:
            stack_2.pop()
        else:
            stack_2.append(ch)

    if len(stack_1) != len(stack_2):
        return False

    for _ in range(0, len(stack_1)):
        if stack_1.pop() != stack_2.pop():
            return False
    return True


print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#"))
print(post_compare("a#c", "b"))
