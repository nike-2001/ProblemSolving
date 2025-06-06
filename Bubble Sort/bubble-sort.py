def bubbleSort(array):

    length = len(array)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
                swapped = True

        if swapped == False:
            break

    return array
