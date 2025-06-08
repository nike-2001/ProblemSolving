# Run-Length Encoding ✅⭐

## Problem Statement

Write a function that takes in a non-empty string and returns its run-length encoding.

From Wikipedia, **run-length encoding** is a form of lossless data compression in which runs of data are stored as a single data value and count, rather than as the original run. For this problem, a run of data is any sequence of consecutive, identical characters.

- Example: The run `"AAA"` would be encoded as `"3A"`.

### Special Rule:
Since the input string can contain **any character** (including numbers), and decoding must be unambiguous, we cannot naively use encodings like `"12A"` (which could be decoded as `"1" + "2A"` or `"12A"`).  

To avoid this, **runs of 10 or more** characters must be **split**.  
For example:
- `"AAAAAAAAAAAA"` (12 A's) should be encoded as `"9A3A"`, not `"12A"`.

---

## Sample Input
```python
string = "AAAAAAAAAAAAABBCCCCDD"
```

## Sample Output
```
"9A4A2B4C2D"



