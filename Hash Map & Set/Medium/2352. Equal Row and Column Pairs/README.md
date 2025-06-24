# 🔍 LeetCode 2352: Equal Row and Column Pairs

> **Problem Link**: [LeetCode - Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/)  
> **Level**: Medium  
> **Language**: C++

---

## 🧠 Intuition

We are asked to count how many **row and column pairs** in a square matrix are exactly equal.

Key insights:
- **Rows** are easily accessible.
- **Columns** are not directly accessible as vectors.
- Instead of comparing each row with each column naively (which would be slow), we can:
  - Store all rows in a **hash map** with their frequency.
  - Construct each column vector and check how many times it matches a row.

---

## 🔨 Approach

1. Use a `map<vector<int>, int>` to store the **frequency** of each row vector.
2. For each **column**, construct its corresponding vector by collecting all elements from each row at that column index.
3. Check how many times this column vector appears in the row frequency map.
4. Accumulate the count.
5. Return the total count.

---

## ⏱️ Complexity

| Metric            | Value        |
|-------------------|--------------|
| Time Complexity   | O(n²)        |
| Space Complexity  | O(n²)        |
