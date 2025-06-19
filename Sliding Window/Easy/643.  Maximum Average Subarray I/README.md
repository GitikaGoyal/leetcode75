# 📊 LeetCode 643: Maximum Average Subarray I

> **Problem Link**: [LeetCode - Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)  
> **Level**: Easy  
> **Language**: C++  

---

## 🧠 Intuition

Given an array of `n` integers and an integer `k`, we must find the maximum average value among all contiguous subarrays of length `k`.

Since `k` is fixed, this is an ideal use-case for the **Sliding Window** technique, allowing efficient calculation of each window sum in constant time.

---

## 🔀 Approach: Sliding Window

### ✅ Steps:
1. Compute the sum of the first `k` elements.
2. Initialize `max_avg` with the average of this window.
3. Slide the window one element at a time:
   - Subtract the element that moves out of the window.
   - Add the new element coming into the window.
   - Calculate the new average and update `max_avg` if it's higher.
4. Return the final `max_avg`.

---

### ⏱️ Complexity

| Metric           | Value   |
|------------------|---------|
| Time Complexity  | O(n)    |
| Space Complexity | O(1)    |
