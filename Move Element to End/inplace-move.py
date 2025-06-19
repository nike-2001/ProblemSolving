def moveElementToEnd(array, toMove):
    start, end = 0, len(array) - 1
    while start < end:
        if array[end] == toMove:
            end -= 1
        if array[start] != toMove:
            start += 1

        if array[start] == toMove and array[end] != toMove:
            array[start], array[end] = array[end], array[start]
            end -= 1
            start += 1

    return array
