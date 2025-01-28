class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for g in grid: 
            left = 0
            right = len(g) - 1
            while left <= right:
                mid = (left+right) // 2
                if g[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            # print(left)
            # print(len(g[left:]))
            ans += len(g[left:])
        return ans