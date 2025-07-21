# Sum of Linked Lists

## Problem Description
You're given two `LinkedList` objects of potentially unequal length. Each `LinkedList` represents a non-negative integer, where each node in the `LinkedList` is a digit of that integer, and the first node in each `LinkedList` always represents the least significant digit of the integer. Write a function that returns the head of a new `LinkedList` that represents the sum of the integers represented by the two input `LinkedLists`.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` / `null` if it's the tail of the list. The `value` of each `LinkedList` node is always in the range of `[0 - 9]`.

**Note:** Your function must create and return a new `LinkedList`, and you're not allowed to modify either of the input `LinkedLists`.

## Sample Input
```
linkedListOne = 2 -> 4 -> 7 -> 1
linkedLIstTwo = 9 -> 4 -> 5
```

## Sample Output

```
1 -> 9 -> 2 -> 2

// LinkedList1one represents 1742
// LinkedList2two represents 549
// 1742 + 549 = 2291
