# Three Number Sum

## Problem Statement

Write a function that takes in a **non-empty array** of **distinct integers** and an **integer representing a target sum**.

The function should find all **triplets in the array** that sum up to the target sum and return a **two-dimensional array** of these triplets.

- Each triplet should be in **ascending order**.
- The final array of triplets should also be sorted in **ascending order** with respect to the numbers they hold.
- If no such triplet exists, return an **empty array**.

## Sample Input
```python
array = [12, 3, 1, -6, -5, -8, 6]
targetSum = 0
```
## Sample Output
```
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
