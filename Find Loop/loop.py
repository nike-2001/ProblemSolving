# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):

    slow = head.next
    fast = head.next.next

    while slow is not fast: 
        slow = slow.next
        fast = fast.next.next

    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow
        
