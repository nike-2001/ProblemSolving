def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, float("inf"))

def findClosestValueHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if currentNode.value > target:
            currentNode = currentNode.left
        elif currentNode.value < target:
            currentNode = currentNode.right
        else:
            break
    return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
