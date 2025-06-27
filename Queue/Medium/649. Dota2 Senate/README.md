# 🏛️ LeetCode 649: Dota2 Senate

> **Problem Link**: [LeetCode - Dota2 Senate](https://leetcode.com/problems/dota2-senate/)  
> **Level**: Medium  
> **Language**: C++, Python

---

## 🧠 Intuition

The problem simulates a voting process between two parties — Radiant (`R`) and Dire (`D`). Each senator can ban an opponent, and the process continues in rounds until one party remains.

The key insight is:
- The order of banning and re-entry (for next round) matters.
- The index of each senator determines priority in each round.

---

## 🔨 Approach

### ✅ Approach I: Brute Force

1. Convert the string to a vector for easy manipulation.
2. Repeatedly:
   - Loop through senators.
   - For each, ban the next senator from the opposite party.
   - Remove banned senators and repeat.
3. Stop when only one party remains.

**Time Complexity**: O(n²)  
**Space Complexity**: O(n)

---

### ✅ Approach II: Greedy using Two Queues

1. Initialize two queues, one for Radiant and one for Dire.
2. Push their indices into their respective queues.
3. In each round:
   - Pop one senator from each queue.
   - The senator with a smaller index bans the other and re-enters the next round by adding `index + n` to their queue.
4. When one queue is empty, the other party wins.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

---

### ✅ Approach III: Greedy using Net Count

1. Use a counter to track net bans:
   - If `cnt > 0`, Radiant is dominant.
   - If `cnt < 0`, Dire is dominant.
2. Traverse through the string:
   - Append surviving senators to the end for the next round.
   - Adjust the `cnt` accordingly.
3. Stop when all senators belong to one party.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

---

## ⏱️ Complexity Summary

| Approach           | Time Complexity | Space Complexity |
|-------------------|------------------|------------------|
| Brute Force        | O(n²)            | O(n)             |
| Greedy (2 Queues)  | O(n)             | O(n)             |
| Greedy (Counter)   | O(n)             | O(n)             |
