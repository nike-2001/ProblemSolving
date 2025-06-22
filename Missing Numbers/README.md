# 🧩 Missing Numbers

You're given an unordered list of **unique integers** `nums` in the range `[1, n]`, where `n` is the length of `nums + 2`.  
This means **two numbers** are missing from this complete range.

Your task is to write a function that takes this list and **returns a new list** with the two missing numbers, **sorted numerically**.

---

## 📝 Problem Statement

Given:
- An array `nums` containing `n - 2` unique integers from the range `[1, n]`.

Find:
- The two missing numbers from the range `[1, n]`.

Return:
- A **sorted list** of the two missing numbers.

---

## 🧪 Sample Input 

```python
nums = [1, 4, 3]
```

## ✅ Output
```
[2, 5]
// Explanation: n = 5
// Completed range should be: [1, 2, 3, 4, 5]
// Missing numbers: 2 and 5

