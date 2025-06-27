def arrayOfProducts(array):
    product = [1 for i in range(len(array))]

    leftProduct = 1
    for i in range(len(array)):
        product[i] = leftProduct
        leftProduct *= array[i]

    rightProduct = 1
    for j in reversed(range(len(array))):
        product[j] *= rightProduct
        rightProduct *= array[j]

    return product
