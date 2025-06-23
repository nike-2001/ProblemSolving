# 🟢 Majority Element

## 📘 Problem Statement

Write a function that takes in a **non-empty, unordered array** of positive integers and returns the array's **majority element** without sorting the array and **without using more than constant space**.

> An array's majority element is an element that appears in **over half** of its indices.

Note:
- The **most common element** isn’t necessarily the **majority element**.
- For example:
  - `[3, 2, 2, 1]` and `[3, 4, 2, 2, 1]` both have `2` as the most frequent, but **not a majority** since it doesn’t appear in more than half the indices.
- You may **assume** that the input array **will always** contain a majority element.

---

## 🧪 Sample Input

```python
array = [1, 2, 3, 2, 2, 1, 2]
```

## ✅ Sample Output
```
2  // 2 occurs in 4/7 indices, making it the majority element

