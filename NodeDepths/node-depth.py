def nodeDepths(root):
    return depthSum(root, 0)

def depthSum(node, depth_sum):

    if node is None:
        return 0
    
    return depth_sum + depthSum(node.left, depth_sum + 1) + depthSum(node.right, depth_sum + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
