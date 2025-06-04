def findThreeLargestNumbers(array):
    val1, val2, val3 = float("-inf"), float("-inf"), float("-inf")

    for ele in array:
        if ele > val1:
            val3 = val2
            val2 = val1
            val1 = ele
        elif ele > val2:
            val3 = val2
            val2 = ele
        elif ele > val3:
            val3 = ele

    return [val3, val2, val1]
            

    
