class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        s=0
        t=0
        for i in range(n):
            for j in range(1,n):
                if nums[i]+nums[j]==target and i!=j:
                    s=i
                    t=j
        if s>t:
            return [t,s]
        else:

            return [s,t]
