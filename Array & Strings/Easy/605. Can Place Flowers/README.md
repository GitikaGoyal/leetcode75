# 🌸 LeetCode 605: Can Place Flowers

> **Problem Link**: [LeetCode - Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)  
> **Level**: Easy  
> **Language**: Python 3


---

## 🧠 Problem Intuition

We are given a flowerbed represented as a list of `0`s and `1`s where `0` is an empty plot and `1` is a planted flower. The goal is to determine whether we can plant `n` new flowers such that **no two flowers are adjacent**.

---

## 🚀 Approach 1: Padding & Greedy Placement

### ✅ Idea

- To simplify boundary checks, we **pad the flowerbed** with an extra `0` at the start and end.
- Then, **loop through** the list from index 1 to len-2:
  - If `f[i-1]`, `f[i]`, and `f[i+1]` are all `0`, a flower can be planted at `i`.
  - Update `f[i] = 1` and decrease `n`.
- At the end, if `n <= 0`, return `True`.

### 🧮 Complexity

- **Time:** O(n)  
- **Space:** O(n) — due to the padded copy of the flowerbed

### 💻 Code

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0
```
---

## 🚀 Approach 2: Count Empty Spaces

### ✅ Idea

- Count stretches of `0`s to calculate how many flowers can be placed.
- Start with `empty = 1` if the first element is 0, to simulate a virtual empty plot at the start.
- Iterate over `flowerbed`:
  - If `plot == 0`, increment `empty`.
  - If `plot == 1`, calculate `((empty - 1) // 2)` flowers in the previous gap, subtract from `n`, and reset `empty = 0`.
- After the loop, use `empty // 2` to account for trailing zeros.

### 🧮 Complexity

- **Time:** O(n)  
- **Space:** O(1) — constant space, no modifications or extra lists

### 💻 Code

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 1 if flowerbed[0] == 0 else 0
        for plot in flowerbed:
            if plot == 0:
                empty += 1
            else:
                n -= (empty - 1) // 2
                empty = 0
        n -= empty // 2
        return n <= 0

