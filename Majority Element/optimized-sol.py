# O(n) - Time 
# O(1) - Space

def majorityElement(array):
    counter = 0
    majority_ele = array[0]
    for num in array:
        if counter == 0:
            majority_ele = num

        if num == majority_ele:
            counter += 1
        else:
            counter -= 1

    return majority_ele
