from collections import deque


def edit_post(post):
    words = post.split()
    result = []

    for word in words:
        queue = deque()
        # Add each character to the queue from the left
        # This reverses the word as we build the queue
        for char in word:
            queue.appendleft(char)

        # Join the characters in the queue to form the reversed word
        result.append("".join(queue))

    return " ".join(result)


print(edit_post("Boost your engagement with these tips"))
print(edit_post("Check out my latest vlog"))
