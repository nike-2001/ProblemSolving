def smallestDifference(arrayOne, arrayTwo):
    min_diff = float("inf")
    output = []
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            abs_diff = abs(arrayOne[i] - arrayTwo[j])
            if abs_diff >= 0 and abs_diff < min_diff:
                min_diff = abs_diff
                output = []
                output.extend([arrayOne[i], arrayTwo[j]])
                

    return output
    
