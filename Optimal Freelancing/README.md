# Optimal Freelancing 💼

You recently started freelance software development and have been offered a variety of job opportunities. Each job has a deadline, meaning there is no value in completing the work after the deadline. Additionally, each job has an associated payment representing the profit for completing that job.

## Problem Statement

Given a list of jobs where each job is represented as a dictionary with a `deadline` and a `payment`, write a function that returns the **maximum profit** that can be obtained in a **7-day period**.

Each job:
- Takes **1 full day** to complete.
- Must be completed **on or before its deadline**.
- Only **one job** can be worked on per day.

**Note:** There is no requirement to complete all of the jobs.

## Constraints

- 1 ≤ number of jobs ≤ 100
- 1 ≤ deadline ≤ 7
- 1 ≤ payment ≤ 10⁶

## Sample Input 

```python
jobs = [
    {"deadline": 1, "payment": 1},
    {"deadline": 2, "payment": 1},
    {"deadline": 2, "payment": 2}
]
```

## Sample Output 
```
3 // Job 0 would be completed first followed by job 2. Job 1 is not completed.

```
