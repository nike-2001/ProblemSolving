def nodeDepths(root):
    depthSum = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        currElement = stack.pop()
        node, depth = currElement["node"], currElement["depth"]

        if node is None:
            continue 
            
        depthSum += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return depthSum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
