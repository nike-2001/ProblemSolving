def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, float("inf"))

def findClosestValueHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    if tree.value > target:
        return findClosestValueHelper(tree.left, target, closest)
    elif tree.value < target:
        return findClosestValueHelper(tree.right, target, closest)
    else:
        return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
