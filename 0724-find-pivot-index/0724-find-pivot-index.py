class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = []
        left = 0
        rightsum = []
        n = len(nums)
        for i in range(n):
            leftsum.append(left)
            left += nums[i]
        right = left
        for i in range(n):
            right -= nums[i]
            rightsum.append(right)
        for i in range(n):
            if rightsum[i] == leftsum[i]:
                return i
        return -1