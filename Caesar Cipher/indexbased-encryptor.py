def caesarCipherEncryptor(string, key):
    result = ""
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    key = key % 26

    for letter in string:
        new_pos = alphabets.index(letter) + key
        result += alphabets[new_pos % 26]

    return result
        
