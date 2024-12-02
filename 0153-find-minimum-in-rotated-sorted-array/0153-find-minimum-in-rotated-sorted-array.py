class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 기본적으로 ascending
        # 증가하다가 감소한 index를 만날텐데 이것이 진짜 작은거냐?
        n = len(nums)
        dn = nums[0]
        for i in range(1,len(nums)):
            if dn < nums[i]:
                dn = nums[i]
            else:
                return nums[i]
        return nums[0]

        