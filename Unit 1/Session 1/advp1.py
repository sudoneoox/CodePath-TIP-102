def linear_search(lst, target):
    for idx, item in enumerate(lst):
        if target == item:
            return idx
    return -1


items = ["haycorn", "haycorn", "haycorn", "hunny", "haycorn"]
target = "hunny"
print(linear_search(items, target))

items = ["bed", "blue jacket", "red shirt", "hunny"]
target = "red balloon"
print(linear_search(items, target))
