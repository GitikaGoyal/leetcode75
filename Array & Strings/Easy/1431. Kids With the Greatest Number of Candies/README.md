# 🧩 LeetCode 1431: Kids With the Greatest Number of Candies

> **Problem Link**: [LeetCode - Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)  
> **Level**: Easy  
> **Language**: Python 3  

---

## 🧠 Intuition

The problem asks whether each child can have the **greatest number of candies** if given all the `extraCandies`.

Core idea:
- First, determine the current maximum number of candies any child has.
- Then, for each child, check if their candy count plus `extraCandies` is greater than or equal to the maximum.

---

## 🚀 Approach

1. Use Python’s `max()` function to find the maximum number of candies among all children.
2. Iterate through each child’s candy count:
   - Add `extraCandies` to it.
   - Compare the result with the maximum candy count.
3. If the result is greater than or equal to the max, append `True` to the result list; otherwise, append `False`.
4. For cleaner and more efficient code, use a list comprehension.

---

## ⏱️ Complexity

| Metric            | Complexity |
|-------------------|------------|
| Time Complexity   | O(n)       |
| Space Complexity  | O(n)       |

Where `n` is the number of children (length of the `candies` list).  
- One traversal to find max.  
- One traversal to construct the output list.

---

## 🧑‍💻 Code

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [candy + extraCandies >= max_candy for candy in candies]
