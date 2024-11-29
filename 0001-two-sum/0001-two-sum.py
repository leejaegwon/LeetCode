class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        len(nums)
        for i in range(len(nums)):
            a = nums[i]
            searchlist = nums[i+1:]
            for j in range(len(searchlist)):
                b = searchlist[j]
                if a + b == target:
                    return [i,i+1+j]