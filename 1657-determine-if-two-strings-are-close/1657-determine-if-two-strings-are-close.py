class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1map = {}
        word2map = {}
        for w in word1:
            if w in word1map:
                word1map[w] += 1
            else:
                word1map[w] = 1
        for w in word2:
            if w in word2map:
                word2map[w] += 1
            else:
                word2map[w] = 1
        w1mk = [i for i in word1map.keys()]
        w2mk = [i for i in word2map.keys()]
        print(w1mk)
        print(w2mk)
        if sorted(w1mk) != sorted(w2mk):
            return False
        w1mv = [i for i in word1map.values()]
        w2mv = [i for i in word2map.values()]
        print(w1mv)
        print(w2mv)
        if sorted(w1mv) != sorted(w2mv):
            return False
        
        return True