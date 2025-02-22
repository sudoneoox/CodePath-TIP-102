def final_value_after_operations(operations):
    retOp = 1
    for _, item in enumerate(operations):
        if item == "bouncy" or item == "flouncy":
            retOp += 1
        elif item == "trouncy" or item == "pouncy":
            retOp -= 1
        else:
            continue
    return retOp


operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
