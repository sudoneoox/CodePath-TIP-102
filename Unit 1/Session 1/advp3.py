def tiggerfy(word):
    """
    Remove 't', 'i', 'gg', and 'er' substrings from a word (case insensitive).
    """
    if not word:
        return ""

    # Convert to lowercase for case insensitive matching
    word_lower = word.lower()
    result = ""
    i = 0

    while i < len(word):
        # Check for 'gg' (2 characters)
        if i < len(word) - 1 and word_lower[i : i + 2] == "gg":
            i += 2
        # Check for 'er' (2 characters)
        elif i < len(word) - 1 and word_lower[i : i + 2] == "er":
            i += 2
        elif word_lower[i] in "ti":
            i += 1
        else:
            result += word[i]
            i += 1

    return result


word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))
