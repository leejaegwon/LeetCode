class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1map = {i:0 for i in nums1}
        nums2map = {i:0 for i in nums2}
        ans1 = []
        ans2 = []
        for i in nums1:
            if i in nums2map or i in ans1:
                continue
            ans1.append(i)
        for i in nums2:
            if i in nums1map or i in ans2:
                continue
            ans2.append(i)
        return [ans1,ans2]
