#Two-Pointer Approach
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        oper_count=0
        while l <r:
            sum_pair=nums[l]+nums[r]
            if sum_pair==k:
                oper_count+=1
                l+=1
                r-=1
            elif sum_pair>k:
                r-=1
            else:
                l+=1
        return oper_count
#T.C.-> O(nlogn)
#S.C.-> O(1)

#OR

#Hash Approach
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m={}
        result=0
        for i in nums:
            if((i in m) and m[i]>0):
                m[i]=m[i]-1
                result+=1
            else:
                if k-i in m:
                    m[k-i]+=1
                else:
                    m[k-i]=1
        return result
#T.C.-> O(n)
#S.C.-> O(n)
