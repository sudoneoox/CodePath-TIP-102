"""
A clean post does not have two adjacent characters post[i] and post[i + 1]
Where post[i] is lowercase and post[i + 1] is the same letter but uppercase
Return a clean post
"""


def clean_post(post):
    stack_1 = []
    for ch in post:
        if stack_1 and ch.lower() == stack_1[-1].lower() and stack_1[-1] != ch:
            stack_1.pop()
            continue
        stack_1.append(ch)
    return "".join(stack_1)


print(clean_post("poOost"))
print(clean_post("abBAcC"))
print(clean_post("s"))
print(clean_post(""))
