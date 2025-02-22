def reverse_sentence(sentence: str) -> str:
    tmp = sentence.split(" ")
    if len(tmp) <= 1:
        return sentence
    tmp = tmp[::-1]
    return " ".join(tmp)


sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))
