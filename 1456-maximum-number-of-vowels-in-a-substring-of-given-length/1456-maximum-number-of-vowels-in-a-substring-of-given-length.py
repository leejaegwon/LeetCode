class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = 'aeiou'
        curvwls = 0
        for i in range(k):
            if s[i] in vowels:
                curvwls += 1
        maxvwls = curvwls
        for i in range(n-k):
            if s[i] in vowels:
                curvwls -= 1
            if s[i+k] in vowels:
                curvwls += 1
            maxvwls = max(maxvwls,curvwls)
        
        return maxvwls