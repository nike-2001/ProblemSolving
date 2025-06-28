# O(n) and O(n) - Time and Space
def firstDuplicateValue(array):
    tracing_values = set()
    for i in range(len(array)):
        if array[i] not in tracing_values:
            tracing_values.add(array[i])
        else:
            return array[i]

    return -1
