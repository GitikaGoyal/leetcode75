class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1,set_nums2=set(nums1),set(nums2)
        difference1=list(set_nums1-set_nums2)
        difference2=list(set_nums2-set_nums1)
        return [difference1, difference2]
