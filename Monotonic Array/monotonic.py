def isMonotonic(array):
      
    if len(array) <= 1:
        return True

    increasing = True
    decreasing = True
    
    for num in range(1, len(array)):
        if array[num] > array[num-1]:
            decreasing = False
        if array[num] < array[num-1]:
            increasing = False

    return increasing or decreasing

