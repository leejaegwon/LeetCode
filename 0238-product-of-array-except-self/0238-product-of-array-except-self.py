class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = {}
        n = len(nums)
        left = []
        product = 1
        for i in range(n):
            left.append(product)
            product *= nums[i]
        right = []
        product = 1
        for i in range(n-1,-1,-1):
            right.append(product)
            product *= nums[i]
        ans = []
        for i in range(n):
            ans.append(left[i]*right[n-1-i])
        return ans