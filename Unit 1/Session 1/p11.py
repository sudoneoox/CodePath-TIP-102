def tiggerfy(s):
    trigger_words = "tigerTIGER"
    for ch in trigger_words:
        s = s.replace(ch, "")
    return s


s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))
