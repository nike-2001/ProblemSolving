def twoNumberSum(array, targetSum):
    set = {}
    for i in range(len(array)):
        diff = targetSum - array[i]
        if diff in set:
            return [diff, array[i]]
        else:
            set[array[i]] = 1

    return []
