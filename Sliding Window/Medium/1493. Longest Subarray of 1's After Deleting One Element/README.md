# 🔢 LeetCode 1493: Longest Subarray of 1's After Deleting One Element

> **Problem Link**: [LeetCode - Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)  
> **Level**: Medium  
> **Language**: C++, Python 3  

---

## 🧠 Intuition

To find the **longest contiguous subarray of 1s** after deleting exactly one element, we can think of this as allowing **at most one zero** in our current window of 1s.  
Using a **sliding window**, we track the number of 0s and maximize the length of valid subarrays where at most one zero is present.

---

## 🔀 Approach: Sliding Window

### ✅ Steps:
1. Initialize two pointers `left` and `right`, and a variable `zeros = 0`.
2. Move `right` through the array:
   - If `nums[right] == 0`, increment `zeros`.
3. If `zeros == 2`, the window is invalid (more than one zero):
   - Move `left` forward until the window contains at most one zero.
4. At each valid window, update the maximum length as `right - left`
   - (not `right - left + 1`, because we need to delete **one** element).
5. Return the maximum length recorded.

---

### ⏱️ Complexity

| Metric           | Value   |
|------------------|---------|
| Time Complexity  | O(n)    |
| Space Complexity | O(1)    |
