# Merging Linked Lists

## Problem Description
You're given two `LinkedList` objects of potentially unequal length. These `LinkedList` objects potentially merge at a shared intersection node. Write a function that returns the intersection node or `None` / `null` if there is no intersection.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` / `null` if it's the tail of the list.

**Note:** Your function should return an existing node. It should not modify either `LinkedList`, and it should not create any new `LinkedList` objects.

## Sample Input

```
LinkedList1one = 2 -> 3 -> 1 -> 4
LinkedList2two = 8 -> 7 -> 1 -> 4
```

## Sample Output
```

1 -> 4 // The lists intersect at the node with value 1
