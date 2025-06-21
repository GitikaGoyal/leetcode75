// Brute-Force
// T.C.->O(n^2)
// S.C.->O(1)
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            int leftSum = 0, rightSum = 0;
            
            for (int j = 0; j < n; ++j) {
                if (j < i) {
                    leftSum += nums[j];
                } else if (j > i) {
                    rightSum += nums[j];
                }
            }

            if (leftSum == rightSum) {
                return i;
            }
        }

        return -1;
    }
};

// Two-Variable Approach
// T.C.->O(n)
// S.C.->O(1)
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }

        int leftSum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            int rightSum = total - leftSum - nums[i];
            if (leftSum == rightSum) {
                return i;
            }
            leftSum += nums[i];
        }

        return -1;
    }
};

// Prefix-Sum Approach
// T.C.->O(n)
// S.C.->O(n)
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n), suffix(n);
        
        prefix[0] = nums[0];
        for (int i = 1; i < n; ++i) {
            prefix[i] = prefix[i - 1] + nums[i];
        }

        suffix[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffix[i] = suffix[i + 1] + nums[i];
        }

        for (int i = 0; i < n; ++i) {
            int left = (i > 0) ? prefix[i - 1] : 0;
            int right = (i < n - 1) ? suffix[i + 1] : 0;
            if (left == right) {
                return i;
            }
        }

        return -1;
    }
};
