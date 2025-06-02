# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    calculated_sum = 0

    for item in array:
        if type(item) == list:
            calculated_sum += productSum(item, depth + 1)
        else:
            calculated_sum += item

    return calculated_sum * depth

