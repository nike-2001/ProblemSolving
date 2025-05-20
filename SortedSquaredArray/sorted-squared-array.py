def sortedSquaredArray(array):
    squared_array = [0] * len(array) 
    start, end = 0, len(array) - 1
    i = len(array) - 1
    while start <= end:
        end_value = array[end]
        start_value = array[start]
        
        if abs(start_value) < abs(end_value):
            squared_array[i] = end_value ** 2
            end -= 1
        else:
            squared_array[i] = start_value ** 2
            start += 1  

        i -= 1
                  
    return squared_array
            
