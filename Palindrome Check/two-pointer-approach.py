def isPalindrome(string):
    start, end = 0, len(string) - 1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
            
    return True
