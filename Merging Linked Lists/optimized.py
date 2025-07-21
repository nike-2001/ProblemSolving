# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):

    firstLL = linkedListOne
    secondLL = linkedListTwo

    while firstLL is not secondLL:
        if not firstLL:
            firstLL = linkedListTwo
        else:
            firstLL = firstLL.next

        if not secondLL:
            secondLL = linkedListOne
        else:
            secondLL = secondLL.next

    return secondLL
