class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        storage = {}
        for i in range(len(min(strs))):
            for s in strs:
                if s[i] != min(strs)[i] or i == len(s):
                    return s[:i]

        return min(strs)


