# 🔢 LeetCode 1732: Find the Highest Altitude

> **Problem Link**: [LeetCode - Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/)  
> **Level**: Easy  
> **Language**: C++, Python 3  

---

## 🧠 Intuition

We start at sea level (altitude = 0), and each element in the `gain` array represents a net gain or loss in altitude.  
To find the **highest altitude reached**, we simulate the journey step-by-step and update the maximum altitude reached along the way.

---

## 🔀 Approach: Prefix Sum

### ✅ Steps:
1. Initialize two variables:
   - `curAltitude = 0` — to track current altitude.
   - `highestPoint = 0` — to record the highest point reached.
2. Iterate through each gain value:
   - Add `g` to `curAltitude`.
   - Update `highestPoint = max(highestPoint, curAltitude)`.
3. Return `highestPoint`.

---

### ⏱️ Complexity

| Metric            | Value   |
|-------------------|---------|
| Time Complexity   | O(n)    |
| Space Complexity  | O(1)    |
