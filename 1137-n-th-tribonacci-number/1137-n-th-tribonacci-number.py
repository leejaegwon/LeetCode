class Solution:
    def tribonacci(self, n: int) -> int:
        Tmap = {}
        Tmap[0] = 0
        Tmap[1] = 1
        Tmap[2] = 1
        for i in range(3,n+1):
            Tmap[i] = Tmap[i-3]+Tmap[i-2]+Tmap[i-1]
        return Tmap[n]