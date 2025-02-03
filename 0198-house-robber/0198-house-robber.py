class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
            
        m = {}
        m[0] = nums[0]
        m[1] = nums[1]
        m[2] = max(nums[2]+nums[0],nums[1])
        for i in range(3,len(nums)):
            m[i] = max(m[i-2]+nums[i],m[i-3]+nums[i])
        return max(m.values())