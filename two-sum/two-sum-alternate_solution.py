def twoNumberSum(array, targetSum):
    array.sort()
    start, high = 0, len(array) - 1
    while start < high:
        if array[start] + array[high] == targetSum:
            return [array[start], array[high]]
        elif array[start] + array[high] > targetSum:
            high -=  1
        else:
            start += 1

    return []
