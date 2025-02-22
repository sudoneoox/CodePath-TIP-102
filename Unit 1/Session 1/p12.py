def locate_thistles(items):
    return [i for i, x in enumerate(items) if x == "thistle"]


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))
