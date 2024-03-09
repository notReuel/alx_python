def multiple_returns(sentence):
    length = len(sentence)
    for char in sentence:
        if char == sentence[0]:
            first = char
    return length, first

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))