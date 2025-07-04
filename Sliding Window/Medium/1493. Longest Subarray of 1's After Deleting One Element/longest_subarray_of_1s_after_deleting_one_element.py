class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        zeros = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros == 2:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, right - left)

        return ans
