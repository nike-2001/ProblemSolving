def caesarCipherEncryptor(string, key):
    result = ""
    key = key % 26
    for ele in string:
        new_ele = ord(ele) + key
        if new_ele > 122:
             new_ele -= 26
        result += chr(new_ele)

    return result


