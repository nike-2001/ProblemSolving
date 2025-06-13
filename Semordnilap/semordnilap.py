def semordnilap(words):
    wordSet = set(words)
    result = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordSet and reverse != word:
            result.append([word, reverse])
            wordSet.remove(word)
            wordSet.remove(reverse)

    return result
