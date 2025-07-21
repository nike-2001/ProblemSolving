class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    
    newLinkedList = LinkedList(0)
    sumLinkedList = newLinkedList
    carry = 0

    firstLinkedList = linkedListOne
    secondLinkedList = linkedListTwo

    while firstLinkedList is not None or secondLinkedList is not None or carry != 0:
        firstLLValue = firstLinkedList.value if firstLinkedList is not None else 0
        secondLLValue = secondLinkedList.value if secondLinkedList is not None else 0

        addValue = firstLLValue + secondLLValue + carry
    
        newValue = addValue % 10

        newNode = LinkedList(newValue)
        sumLinkedList.next = newNode
        sumLinkedList = newNode
    
        carry = addValue // 10

        firstLinkedList = firstLinkedList.next if firstLinkedList is not None else None
        secondLinkedList = secondLinkedList.next if secondLinkedList is not None else None

    return newLinkedList.next

        
