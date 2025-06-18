# 🔢 LeetCode 1679: Max Number of K-Sum Pairs

> **Problem Link**: [LeetCode - Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/)  
> **Level**: Medium  
> **Language**: Python 3  

---

## 🧠 Intuition

We aim to find the **maximum number of unique pairs** whose sum equals `k`.  
Two efficient strategies are possible:
1. **Two-Pointer on Sorted Array** – greedy pairing by moving inward.
2. **Hash Map** – tracking complement values dynamically.

---

## 🔀 Approach 1: Two-Pointer

### ✅ Steps:
1. Sort the input array.
2. Initialize two pointers:
   - `l` at the start.
   - `r` at the end.
3. While `l < r`:
   - If `nums[l] + nums[r] == k`: count a valid operation and move both inward.
   - If the sum is greater than `k`, decrement `r`.
   - If the sum is less than `k`, increment `l`.
4. Return the operation count.

### ⏱️ Complexity

| Metric            | Complexity   |
|-------------------|--------------|
| Time Complexity   | O(n log n)   |
| Space Complexity  | O(1)         |

---

### 💻 Code

```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        oper_count = 0
        while l < r:
            sum_pair = nums[l] + nums[r]
            if sum_pair == k:
                oper_count += 1
                l += 1
                r -= 1
            elif sum_pair > k:
                r -= 1
            else:
                l += 1
        return oper_count
```
---
## 🔀 Approach 2: Hash-Map

### ✅ Steps:
1. Initialize a dictionary `m` to store complement counts.
2. Iterate over `nums`:
   - If current number `i` exists in `m` and has a positive count, pair found -> Decrease m[i] and increase result counter.
   - Else, increment the count for the needed complement `k - i`.
3. Return the result.

### ⏱️ Complexity

| Metric            | Complexity   |
|-------------------|--------------|
| Time Complexity   | O(n)         |
| Space Complexity  | O(n)         |

---

### 💻 Code

```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = {}
        result = 0
        for i in nums:
            if i in m and m[i] > 0:
                m[i] -= 1
                result += 1
            else:
                m[k - i] = m.get(k - i, 0) + 1
        return result
```
