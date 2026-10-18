class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sep_s = []
        sep_t = []
        for i in s:
            sep_s.append(i)

        for i in t:
            sep_t.append(i)

        x_s = sorted(sep_s)
        x_t = sorted(sep_t)

        if x_s == x_t:
            return True

        else:
            return False