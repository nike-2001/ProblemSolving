def insertionSort(array):
   
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while j > 0 and key < array[j-1]:
            array[j] = array[j-1]
            j -= 1
            
        array[j] = key

    return array
        
        
        

