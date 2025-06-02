# 🟢 Product Sum

Write a function that takes in a **"special" array** and returns its product sum.

---

### 📘 What is a "Special" Array?

A **special array** is a non-empty array that contains either integers or other **special** arrays.

The **product sum** of a "special" array is the sum of its elements, where **"special" arrays inside it are summed themselves and then multiplied by their level of depth**.

---

### 📏 Depth of a Special Array

- The depth of `[]` is `1`
- The depth of `[[]]` is `2`
- The depth of `[[[[]]]]` is `4`

Each nested level increases the depth by 1.

---

### 📌 Product Sum Examples

- `productSum([x, y]) = x + y`
- `productSum([x, [y, z]]) = x + 2 * (y + z)`
- `productSum([x, [y, [z]]]) = x + 2 * (y + 3 * z)`

---

## ✅ Sample Input

```python
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
```

## 🎯 Sample Output
```python
12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)

