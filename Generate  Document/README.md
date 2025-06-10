# Generate Document 🟢⭐

You're given a string of available **characters** and a string representing a **document** that you need to generate.

Write a function that determines if you can generate the document using the available characters.  
If you can generate the document, your function should return `true`; otherwise, it should return `false`.

---

## ✅ Conditions

- You can only generate the document **if the frequency of every character in the `document` is less than or equal to its frequency in `characters`**.
- The document may include **any printable characters**, such as:
  - Uppercase and lowercase letters
  - Digits
  - Punctuation
  - Whitespace

> Note: You can **always** generate the empty string `""`.

---

## 🧪 Sample Input

```python
characters = "Bst!hetsi ogAexlprt x "
document = "AlgoExpert is the Best!"
```

## ✅ Sample Output
```
True
