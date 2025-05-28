# Minimum Waiting Time ⏳✅

You're given a non-empty array of positive integers representing the amounts of time that specific queries take to execute. Only one query can be executed at a time, but the queries can be executed in any order.

## 🧠 Problem Statement

A query's **waiting time** is defined as the amount of time that it must wait before its execution starts.  
- If a query is executed second, then its waiting time is the duration of the first query.
- If a query is executed third, then its waiting time is the sum of the durations of the first two queries, and so on.

Write a function that returns the **minimum amount of total waiting time** for all of the queries.

> 💡 You are allowed to mutate the input array.

### 🧮 Sample Input

Given the queries:  
```python
queries = [3, 2, 1, 2, 6]
```

### 🧮 Sample Output

```python
17
```

