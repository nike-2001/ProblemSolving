# 🏆 Tournament Winner

This Python program determines the winner of a tournament based on a list of competitions and results. Each competition is a match between two teams, and the winning team receives 3 points. The team with the highest total points is declared the tournament winner.


## 🧠 Function Description

### `tournamentWinner(competitions, results)`

- **Parameters:**
  - `competitions`: List of pairs of teams, e.g., `[["A", "B"], ["B", "C"]]`
  - `results`: List of match outcomes. `1` means the first team won, `0` means the second team won.
- **Returns:** The name of the team with the highest score.

## ✅ Example

```python
competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]  # Winners: C#, Python, Python

print(tournamentWinner(competitions, results))  # Output: Python
```
