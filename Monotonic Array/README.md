# Monotonic Array 🟢⭐

## Problem Description

Write a function that takes in an array of integers and returns a boolean indicating whether the array is **monotonic**.

An array is considered **monotonic** if its elements, from left to right, are either:
- Entirely **non-increasing**, or
- Entirely **non-decreasing**.

> Note:
- An array is **non-increasing** if every element is **less than or equal to** the previous element.
- An array is **non-decreasing** if every element is **greater than or equal to** the previous element.
- **Empty arrays** and **arrays with one element** are trivially monotonic.

---

## Sample Input

```python
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
```

## Sample Output
```
true
