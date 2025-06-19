class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int ans = 0;
        int zeros = 0;

        for (int left = 0, right = 0; right < nums.size(); right++)
        {
            if (nums[right] == 0)
                zeros++;
            while (zeros == 2)
            {
                if (nums[left] == 0)
                    zeros--;
                left++;
            }
            ans = max(ans, right - left);
        }

        return ans;
    }
};
