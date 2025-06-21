# ⚖️ LeetCode 724: Find Pivot Index

> **Problem Link**: [LeetCode - Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)  
> **Level**: Easy  
> **Language**: C++, Python 3  

---

## 🧠 Intuition
We want to find the **pivot index** such that the sum of all elements to the **left** equals the sum of all elements to the **right**. This can be solved using:
- Brute Force (check all indices)
- Prefix-Suffix arrays
- Optimized Two-Variable (most efficient)

---

## 🔨 Approaches

---

### 🪓 1. Brute Force

#### 🔁 Approach:
1. For every index `i` in the array:
   - Compute the **left sum**: sum of elements from index `0` to `i - 1`.
   - Compute the **right sum**: sum of elements from index `i + 1` to `n - 1`.
2. If at any index `i`, `left sum == right sum`, return `i`.
3. If no such index is found, return `-1`.

This approach checks all possible pivot points and compares the sums manually.

#### ⏱️ Complexity

| Metric            | Value   |
|-------------------|---------|
| Time Complexity   | O(n²)   |
| Space Complexity  | O(1)    |

---
### 🪓 2. Prefix-Suffix Arrays

#### 🔁 Approach:
1. Compute prefix sum array:
   - `prefix[i]` is the sum from index `0` to `i`.
2. Compute suffix sum array:
   - `suffix[i]` is the sum from index `i` to the end.
3. For each index `i`:
   - Let `left = prefix[i - 1]` (0 if i == 0).
   - Let `right = suffix[i + 1]` (0 if i == n - 1).
   - If `left == right`, return `i`.
4. If no such index is found, return `-1`.


### ⏱️ Complexity

| Metric            | Value   |
|-------------------|---------|
| Time Complexity   | O(n)    |
| Space Complexity  | O(n)    |

---
### 🪓 3. Two-Variable

#### 🔁 Approach:
1. Calculate the **total sum** of the array and store it in `total`.
2. Initialize `leftSum = 0`.
3. For each index `i` from `0` to `n - 1`:
   - Let `rightSum = total - leftSum - nums[i]`.
   - If `leftSum == rightSum`, return `i` (current index is pivot).
   - Else, add `nums[i]` to `leftSum` and continue.
4. If no such index is found, return `-1`.

This avoids the need for extra space and computes the result in a single pass after calculating the total.

#### ⏱️ Complexity

| Metric            | Value   |
|-------------------|---------|
| Time Complexity   | O(n)   |
| Space Complexity  | O(1)    |
