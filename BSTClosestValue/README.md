# Find Closest Value in BST ✅🌲

## 🧠 Problem Statement

Write a function that takes in a **Binary Search Tree (BST)** and a **target integer value**, and returns the closest value to that target value contained in the BST.

You can assume that there will only be **one closest value**.

Each `BST` node has:
- an integer `value`
- a `left` child node
- a `right` child node

A node is said to be a valid BST node **if and only if** it satisfies the **BST property**:
- Its `value` is strictly greater than the values of every node to its left.
- Its `value` is less than or equal to the values of every node to its right.
- Its children are either valid `BST` nodes themselves or `None` / `null`.

---

## 📥 Sample Input

```text
tree =    10
         /  \
        5    15
       / \   / \
      2   5 13 22
     /       \
    1         14

target = 12
```

## 📥 Sample Output
```
13
```
