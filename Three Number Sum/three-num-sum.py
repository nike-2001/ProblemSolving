def threeNumberSum(array, targetSum):
    array.sort() 
    output = []

    for i in range(len(array) - 2):
        
        left_count = i + 1
        right_count = len(array) - 1
    
        while left_count < right_count:
    
            curr = array[i]
            left = array[left_count]
            right = array[right_count]
                
            curr_sum = curr + left + right
            
            if curr_sum == targetSum:
                output.append([curr, left, right])
                left_count += 1
                right_count -= 1
                
            elif curr_sum < targetSum:
                left_count += 1
            else:
                right_count -= 1

    return output
            
        
