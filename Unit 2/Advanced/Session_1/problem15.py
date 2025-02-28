from typing import Dict


def find_most_frequent_word(text, illegibles):
    result: Dict = {}
    word_arr = text.split(" ")
    for word in word_arr:
        if illegibles in word:
            continue
