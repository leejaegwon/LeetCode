class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = { 
            "I":1, "V":5, "X":10,
            "L":50, "C":100, "D": 500, 
            "M":1000
        }
        sum = 0
        lastword = ""
        for string in s:
            if lastword == "I":
                if string == "V" or string == "X":
                    sum -= 2 * romanMap[lastword]
            elif lastword == "X":
                if string == "L" or string == "C":
                    sum -= 2 * romanMap[lastword]
            elif lastword == "C":
                if string == "D" or string == "M":
                    sum -= 2 * romanMap[lastword]
            sum += romanMap[string]
            lastword = string
        
        return sum
        