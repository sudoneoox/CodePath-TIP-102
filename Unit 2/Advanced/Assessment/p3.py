from typing import Dict


def roman_to_integer(s):
    roman_dict: Dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }
    resulting_sum: int = 0
    i: int = 0
    while i < len(s):
        if i + 1 >= len(s):
            resulting_sum += roman_dict[s[i]]
            break
        if s[i] + s[i + 1] in roman_dict:
            resulting_sum += roman_dict[s[i] + s[i + 1]]
            i += 2
            continue
        resulting_sum += roman_dict[s[i]]
        i += 1

    return resulting_sum
