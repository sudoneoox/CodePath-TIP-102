def engagement_boost(engagement_boost):
    # List Comprehension Power of 2
    engagement_boost = [num**2 for num in engagement_boost]

    aux_stack = []
    while len(engagement_boost) != 0:
        # reference element
        tmp_val = engagement_boost.pop()

        # if tmp_val is biggest then we need to transfer
        # all those elements to aux_stack
        while len(aux_stack) != 0 and aux_stack[-1] > tmp_val:
            engagement_boost.append(aux_stack.pop())

        aux_stack.append(tmp_val)

    # while len(aux_stack) != 0:
    # engagement_boost.append(aux_stack.pop())

    return aux_stack


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
