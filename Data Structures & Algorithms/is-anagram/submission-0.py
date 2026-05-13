class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}

        for l in s:
            if l in sChars:
                sChars[l] += 1
            else:
                sChars[l] = 1

        for l in t:
            if l not in sChars:
                return False
            elif sChars[l] - 1 < 0:
                return False
            
            sChars[l] -= 1

        for value in sChars.values():
            if value != 0:
                return False

        return True