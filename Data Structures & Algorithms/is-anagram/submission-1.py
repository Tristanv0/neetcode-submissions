class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sChars = {}
        
        for i in range(len(s)):
            sChars[s[i]] = sChars.get(s[i], 0) + 1
            sChars[t[i]] = sChars.get(t[i], 0) - 1

        return all(v == 0 for v in sChars.values())

        return True