# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    count = 0

    currentNode = linkedList
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next

    middle_node = linkedList
    for _ in range(count // 2):
        middle_node = middle_node.next

    return middle_node

    
            
    
