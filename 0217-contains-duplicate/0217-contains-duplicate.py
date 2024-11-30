class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in m:
                return True
            else:
                m[nums[i]] = 0
        return False