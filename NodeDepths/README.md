# 🌲 Node Depths

The distance between a node in a Binary Tree and the tree’s root is called the node's **depth**.

### 🧩 Problem Statement

Write a function that takes in a Binary Tree and returns the **sum of its nodes' depths**.

Each `BinaryTree` node has:
- an integer `value`
- a `left` child node
- a `right` child node

Child nodes can either be `BinaryTree` nodes themselves or `None` / `null`.

---

### 🧪 Sample Input

```python
tree =     1
         /   \
        2     3
      /  \   / \
     4    5 6   7
    / \
   8   9
        
```

### ✅ Sample Output

```python

16

The depth of the node with value 2 is 1.
The depth of the node with value 3 is 1.
The depth of the node with value 4 is 2.
The depth of the node with value 5 is 2.
....
The depth of the node with value 9 is 3.

Sum of all depths = 16
```
