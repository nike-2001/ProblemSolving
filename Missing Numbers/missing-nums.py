def missingNumbers(nums):

    present_sum = sum(nums)
    expected_sum = 0
    for i in range(1, len(nums) + 3):
        expected_sum += i

    avg = (expected_sum - present_sum) // 2
    
    leftHalfSum, rightHalfSum = 0, 0

    for num in nums:
        if num <= avg:
            leftHalfSum += num
        else:
            rightHalfSum += num

    totalLeftHalfSum = sum(range(1, avg + 1))
    totalRightHalfSum = sum(range(avg + 1, len(nums) + 3))

    return [totalLeftHalfSum - leftHalfSum, totalRightHalfSum - rightHalfSum]
        

    
    
