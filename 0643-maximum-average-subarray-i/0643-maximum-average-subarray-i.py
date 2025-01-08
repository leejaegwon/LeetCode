class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curval = 0
        for i in range(k):
            curval += nums[i]
        maxval = curval
        for i in range(n-k):
            curval = curval-nums[i]+nums[i+k]
            maxval = max(curval,maxval)

            
        return maxval/k
            
