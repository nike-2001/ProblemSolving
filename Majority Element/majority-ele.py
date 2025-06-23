# O(n) - Time and Space

def majorityElement(array):
    array_map = {}
    for num in array:
        if num not in array_map:
            array_map[num] = 1
        else:
            array_map[num] += 1

    for key, value in array_map.items():
        if value > len(array) // 2:
            return key

    return -1
