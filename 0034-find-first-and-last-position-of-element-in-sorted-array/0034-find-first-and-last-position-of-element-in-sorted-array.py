class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # last: target - 1, first: target + 1 range
        # if last +1 == first return -1,-1
        def search(nums,target,searchLeft):
            left = 0
            right = len(nums) -1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    idx = mid
                    if searchLeft:
                        right = mid -1
                    else:
                        left = mid + 1
        
            return idx
        left = search(nums,target,True)
        right = search(nums,target,False)
        return [left,right]