def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end ) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binarySearchHelper(array, target, mid + 1, end)
    else:
        return binarySearchHelper(array, target, start, mid - 1)
