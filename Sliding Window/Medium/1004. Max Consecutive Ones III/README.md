# 🔢 LeetCode 1004: Max Consecutive Ones III

> **Problem Link**: [LeetCode - Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)  
> **Level**: Medium  
> **Language**: Python 3  

---

## 🧠 Intuition

We want to find the **longest contiguous subarray of 1s** that can be formed by flipping at most `k` zeros.  
This fits perfectly with the **sliding window** approach where we expand the window while keeping the number of 0s within the allowed limit.

---

## 🔀 Approach: Sliding Window

### ✅ Steps:
1. Use two pointers: `left` and `right` to maintain the current window.
2. Count how many zeros are in the current window using `zero_count`.
3. If `zero_count > k`, it means we need to shrink the window from the `left` until we have `≤` k zeros:
   - Move `left` pointer forward and decrement `zero_count` if the left element is 0.
4. Update `max_len` as the maximum window size encountered (`right - left + 1`).
5. Return `max_len` as a result.

---

### ⏱️ Complexity

| Metric           | Value   |
|------------------|---------|
| Time Complexity  | O(n)    |
| Space Complexity | O(1)    |
