# 🚴‍♂️ Tandem Bicycle

A tandem bicycle is a bicycle that’s operated by two people: person A and person B. Both people pedal the bicycle, but the person that pedals faster dictates the speed of the bicycle.  
So if person A pedals at a speed of `5`, and person B pedals at a speed of `4`, the tandem bicycle moves at a speed of `5` (i.e., `tandemSpeed = max(speedA, speedB)`).

You’re given two lists of positive integers:
- One that contains the speeds of riders wearing red shirts
- One that contains the speeds of riders wearing blue shirts

Each rider is represented by a single positive integer, which is the speed that they pedal a tandem bicycle at.  
Both lists have the same length, meaning there are as many red-shirt riders as blue-shirt riders.  
Your goal is to pair every rider wearing a red shirt with a rider wearing a blue shirt to operate a tandem bicycle.

Write a function that returns the maximum possible total speed or the minimum possible total speed of all of the tandem bicycles being ridden based on an input parameter `fastest`.  
If `fastest = true`, your function should return the **maximum** total possible speed; otherwise it should return the **minimum** total speed.

**Total speed** is defined as the sum of the speeds of all the tandem bicycles being ridden.  
For example, if there are 4 riders (2 red-shirt riders and 2 blue-shirt riders) who have speeds `[1, 3, 4, 5]`, and they’re paired as follows: `[1, 4]`, `[5, 3]`, the total speed is `max(1, 4) + max(5, 3) = 4 + 5 = 9`.

---

### 📥 Sample Input
```python
redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True
```

### 📥 Sample Output
```
32
```
