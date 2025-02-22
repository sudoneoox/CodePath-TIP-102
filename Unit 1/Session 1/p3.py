"""
Problem 3: Catchphrase
Write a function print_catchphrase() that accepts a string character as a parameter and prints
the catchphrase of the given character
"""


def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Trigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")


print_catchphrase("Pooh")

print_catchphrase("Piglet")
