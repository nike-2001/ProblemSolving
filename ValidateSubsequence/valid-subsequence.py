def isValidSubsequence(array, sequence):
    start = 0
    for i in range(len(array)):
        if sequence[start] == array[i]:
            start += 1
        if start == len(sequence):
            return True

    return False
