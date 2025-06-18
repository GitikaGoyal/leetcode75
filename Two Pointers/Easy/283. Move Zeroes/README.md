# 🧩 LeetCode 283: Move Zeroes

> **Problem Link**: [LeetCode - Move Zeroes](https://leetcode.com/problems/move-zeroes/)  
> **Level**: Easy  
> **Language**: Python 3  

---

## 🧠 Intuition

The goal is to move all `0`s in the array to the end while keeping the order of non-zero elements intact.  
We can do this in-place by:
- Keeping a pointer (`l`) to track where the next non-zero should be placed.
- Using another pointer (`r`) to iterate through the array.
- Swapping `nums[l]` and `nums[r]` when a non-zero is found.

---

## 🚀 Approach

1. Initialize `l = 0` to mark the position to place the next non-zero.
2. Iterate with `r` from `0` to `len(nums) - 1`:
   - If `nums[r]` is non-zero:
     - Swap it with `nums[l]`.
     - Increment `l`.
3. This places all non-zero elements at the beginning and moves zeroes to the end.
4. Since swapping only happens when `nums[r]` is non-zero, the relative order is maintained.

---

## ⏱️ Complexity

| Metric            | Complexity |
|-------------------|------------|
| Time Complexity   | O(n)       |
| Space Complexity  | O(1)       |

---

## 🧑‍💻 Code

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
