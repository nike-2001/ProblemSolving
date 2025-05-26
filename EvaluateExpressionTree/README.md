# 🧮 Evaluate Expression Tree

You're given a binary expression tree. Write a function to evaluate this tree mathematically and return a single resulting integer.

### 📘 Problem Statement

All leaf nodes in the tree represent **operands** (positive integers).  
All other nodes represent **operators**, defined by negative integers:

- `-1`: ➕ Addition (left + right)
- `-2`: ➖ Subtraction (left - right)
- `-3`: ➗ Division (left ÷ right), rounded towards zero
- `-4`: ✖️ Multiplication (left × right)

You can assume the tree will always be a **valid expression tree**.

> **Note**: Operators act like grouping symbols – child subtrees are always evaluated before applying the operator.

---

### 🌳 Sample Input (Tree Structure)

```python
tree =     -1
         /   \
       -2    -3
      /  \   / \
     -4   2 8   3
    / \
   2   3
        
```

### ✅ Sample Output

```python

# 6   // (((2 * 3) - 2) + (8 / 3))

```
