class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        map<vector<int>,int> freq;
        int n=grid.size();
        int count=0;

        for(auto i: grid)
        {
            freq[i]++;
        }

        for(int j=0; j<n; j++)
        {
            vector<int> helper;
            for(int i=0; i<n; i++)
            {
                helper.push_back(grid[i][j]);
            }

            count+=freq[helper];
        }

        return count;
    }
};
