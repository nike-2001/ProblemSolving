def kadanesAlgorithm(array):
    max_sum = array[0]
    final_max = array[0]
    for i in range(1, len(array)):
        max_sum = max(array[i] + max_sum, array[i])
        final_max = max(final_max, max_sum)

    return final_max
        
