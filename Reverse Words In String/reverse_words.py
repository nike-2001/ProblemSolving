def reverseWordsInString(string):
    words = []
    startOfWord = 0

    for idx in range(len(string)):

        char = string[idx] 
        if char == " ":
            words.append(string[startOfWord:idx])
            startOfWord = idx

        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx

    words.append(string[startOfWord:])
    reverseWords(words)

    return "".join(words)


def reverseWords(words):
    start, end = 0, len(words) - 1
    while start < end:
        words[start], words[end] = words[end], words[start]
        start += 1
        end -= 1

        
