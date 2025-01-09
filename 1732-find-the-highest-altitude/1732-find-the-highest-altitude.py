class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        hval = 0
        maxval = 0
        for g in gain:
            hval += g
            if maxval < hval:
                maxval = hval
        return maxval