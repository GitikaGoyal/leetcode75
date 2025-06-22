class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict (int)
        for i in range (len(arr)):
            freq[arr[i]] += 1    
        uniqueFreq = set([])
        for i in freq:
            if (freq[i] in uniqueFreq):
                return False
            else:
                uniqueFreq.add(freq[i])

        return True
