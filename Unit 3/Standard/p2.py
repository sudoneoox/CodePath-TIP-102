def reverse_comments_queue(comments):
    stack1 = []
    for _ in range(0, len(comments)):
        stack1.append(comments.pop())
    return stack1


print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
