def commonCharacters(strings):
    result_set = {}

    for string in strings:
        string_set = set(string)
        for letter in string_set:
            if letter not in result_set:
                result_set[letter] = 0
            result_set[letter] += 1

    result = []
    for key, value in result_set.items():
        if value == len(strings):
            result.append(key)

    return result
        

