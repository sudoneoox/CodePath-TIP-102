def booth_navigation(clues):
    stack = []
    for i in range(0, len(clues)):
        if clues[i] == "back":
            if stack:
                stack.pop()
        else:
            stack.append(clues[i])
    return stack


clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues))

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues))

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues))
