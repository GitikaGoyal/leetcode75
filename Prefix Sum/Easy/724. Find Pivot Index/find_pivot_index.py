# Brute-Force
# T.C.->O(n^2)
# S.C.->O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = -1

        for i in range(len(nums)):
            leftSum = 0
            rightSum = 0
            for j in range(len(nums)):
                if (i == j):
                    continue
                if (j < i):
                    leftSum += nums[j]
                elif (j > i):
                    rightSum += nums[j]
            if (leftSum == rightSum):
                index = i
                break
        return index

# Two-Variable solution
# T.C.->O(2n)=>O(n)
# S.C.->O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = 0
        for num in nums:
            rightSum += num
        leftSum = 0
        for i in range(len(nums)):
            rightSum -= nums[i]
            if (leftSum == rightSum):
                return i
            leftSum += nums[i]
        return -1

# Prefix Suffix Sum Solution
# T.C.->O(3n)=>O(n)
# S.C.->O(2n)=>O(n)
