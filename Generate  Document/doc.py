def generateDocument(characters, document):
    for char in document:
        doc_freq = countCharFreq(char, document)
        char_freq = countCharFreq(char, characters)

        if doc_freq > char_freq:
            return False
        
    return True


def countCharFreq(char, input):
    freq = 0
    for letter in input:
        if letter == char:
            freq += 1

    return freq
