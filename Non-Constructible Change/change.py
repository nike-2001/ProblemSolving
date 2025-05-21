def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for num in coins:
        if num > change + 1:
            return change + 1
        change += num
            
    return change + 1
