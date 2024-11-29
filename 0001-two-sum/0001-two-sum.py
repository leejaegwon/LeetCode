class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            findzero = target - nums[i]
            if findzero in numMap and numMap[findzero] != i:
                return [i,numMap[findzero]]
        return []