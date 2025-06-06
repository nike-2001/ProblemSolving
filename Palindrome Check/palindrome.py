def isPalindrome(string):
    reverse = ""
    for i in reversed(string):
        reverse += i

    if reverse == string:
        return True
    return False
