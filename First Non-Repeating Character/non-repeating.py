def firstNonRepeatingCharacter(string):
    freq_count = {}
 
    for char in string:
        if char not in freq_count:
            freq_count[char] = 0
        freq_count[char] += 1

    for index, key in enumerate(string):
        if freq_count[key] == 1:
            return index

    return -1
    
