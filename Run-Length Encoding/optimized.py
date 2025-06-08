def runLengthEncoding(string):
    encoding = []
    count = 1

    for char in range(1, len(string)):
        if string[char] != string[char - 1] or count == 9:
            encoding.append(str(count))
            encoding.append(string[char-1])
            count = 0

        count += 1

    encoding.append(str(count))
    encoding.append(string[len(string)-1])


    return "".join(encoding)
