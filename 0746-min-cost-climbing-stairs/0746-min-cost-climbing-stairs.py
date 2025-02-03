class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pay = {}
        pay[0] = 0
        pay[1] = 0
        for i in range(2,len(cost)+1):
            pay[i] = min(pay[i-2]+cost[i-2],pay[i-1]+cost[i-1])
        return pay[len(cost)]