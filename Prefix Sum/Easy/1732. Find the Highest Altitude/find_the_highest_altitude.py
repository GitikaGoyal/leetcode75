class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curAltitude = 0
        highestPoint = 0
        for g in gain:
            curAltitude += g
            highestPoint = max(highestPoint, curAltitude)
        return highestPoint
