class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = []
        b = []
        for i in str(x):
            a.append(i)
        for i in range(len(a)):
            b.append(a.pop())
        b = "".join(b)
        try:
            b = int(b)
            return x == b
        except ValueError:
            return False

        