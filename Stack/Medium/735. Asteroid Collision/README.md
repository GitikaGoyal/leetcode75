# ☄️ LeetCode 735: Asteroid Collision

> **Problem Link**: [LeetCode - Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)  
> **Level**: Medium  
> **Language**: C++, Python

---

## 🧠 Intuition

We simulate collisions between asteroids moving in opposite directions.  
A collision only occurs when:
- The current asteroid is moving left (`< 0`)
- The top of the stack is a right-moving asteroid (`> 0`)

This makes a **stack** the perfect structure:
- Push right-moving asteroids onto the stack.
- When a left-moving asteroid comes in, compare it with the top of the stack for potential collisions.

---

## 🔨 Approach

1. Initialize an empty `stack<int>`.
2. Traverse each asteroid `a` in the input list:
   - While the stack is not empty and `a` is negative and the top of the stack is positive:
     - If `abs(a)` > top → pop the top and continue checking.
     - If equal → pop the top and discard `a`.
     - If `abs(a)` < top → discard `a`.
   - If `a` survives all possible collisions, push it onto the stack.
3. Transfer all surviving asteroids from the stack to a result vector (in correct order).

---

## ⏱️ Complexity

| Metric            | Value        |
|-------------------|--------------|
| Time Complexity   | O(n)         |
| Space Complexity  | O(n)         |
