def split_haycorns(quantity):
    list = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            list.append(i)
    return list


quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))
