# 📞 LeetCode 933: Number of Recent Calls

> **Problem Link**: [LeetCode - Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)  
> **Level**: Easy  
> **Language**: C++, Python

---

## 🧠 Intuition

We want to count how many requests (pings) have been made in the past 3000 milliseconds including the current one.  
This is a classic use case for a **queue** where we only keep track of the relevant time range by removing outdated elements.

---

## 🔨 Approach

1. Maintain a queue `q` to store the timestamps of incoming pings.
2. Each time a new ping at time `t` is received:
   - Push `t` into the queue.
   - Remove all timestamps from the front of the queue that are older than `t - 3000`.
3. The remaining size of the queue represents the number of pings within the last 3000 milliseconds.

---

## ⏱️ Complexity

| Metric            | Value        |
|-------------------|--------------|
| Time Complexity   | O(1) (amortized per operation) |
| Space Complexity  | O(n), where n is the number of pings in the last 3000 ms |
