# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):

    listNodes = set()
    firstLL = linkedListOne
    secondLL = linkedListTwo

    while firstLL is not None:
        listNodes.add(firstLL)
        firstLL = firstLL.next
    
    while secondLL is not None:
        if secondLL in listNodes:
            return secondLL

        secondLL = secondLL.next

    return None
