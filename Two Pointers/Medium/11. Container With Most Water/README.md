# 🧩 LeetCode 11: Container With Most Water

> **Problem Link**: [LeetCode - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)  
> **Level**: Medium  
> **Language**: Python 3  

---

## 🧠 Intuition

The task is to find two lines that together with the x-axis form a container that holds the most water.  
Instead of checking all possible pairs (brute-force), we can optimize using a two-pointer approach:
- Start with the widest possible container.
- Always move the pointer pointing to the shorter line to potentially find a taller line that can hold more water.

---

## 🚀 Approach

1. Initialize two pointers:
   - `l` at the start (index 0)
   - `r` at the end (index `len(height) - 1`)
2. While `l < r`:
   - Compute the area: `(r - l) * min(height[l], height[r])`
   - Update the result if this area is greater than the previous maximum.
   - Move the pointer pointing to the shorter height inward:
     - If `height[l] < height[r]`, increment `l`
     - Else, decrement `r`
3. Return the maximum area found.

---

## ⏱️ Complexity

| Metric            | Complexity |
|-------------------|------------|
| Time Complexity   | O(n)       |
| Space Complexity  | O(1)       |

Where `n` is the number of elements in the `height` list.

---

## 🧑‍💻 Code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
