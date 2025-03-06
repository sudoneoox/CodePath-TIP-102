def is_symmetrical_title(title):
    i, j = 0, len(title) - 1
    while i <= j:
        ch_1 = title[i].lower()
        ch_2 = title[j].lower()
        if ch_1 == " " or ch_1 == ",":
            i += 1
            continue
        elif ch_2 == " " or ch_2 == ",":
            j -= 1
            continue
        print(f"comparing {ch_1} with {ch_2}")
        if ch_1 != ch_2:
            return False
        i += 1
        j -= 1

    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))
