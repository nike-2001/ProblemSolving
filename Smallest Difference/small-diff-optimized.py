def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    output = []
    min_diff = float("inf")
    first, second = 0, 0

    while first < len(arrayOne) and second < len(arrayTwo):
        firstNum = arrayOne[first]
        secondNum = arrayTwo[second]

        abs_diff = abs(firstNum - secondNum)
        if abs_diff >= 0 and abs_diff < min_diff:
            min_diff = abs_diff
            output = []
            output.extend([firstNum, secondNum])

        if firstNum < secondNum:
            first += 1
        else:
            second += 1

    return output
        
