class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int curAltitude = 0;
        int highestPoint = 0;
        for (int g:gain)
        {
            curAltitude += g;
            highestPoint = max(highestPoint, curAltitude);
        }
        return highestPoint;
    }
};
