class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        orderedStrs = ["".join(sorted(string)) for string in strs]
        anagrams = {}

        for i in range(len(orderedStrs)):
            if orderedStrs[i] not in anagrams:
                anagrams[orderedStrs[i]] = [strs[i]]
            else:
                anagrams[orderedStrs[i]].append(strs[i])

        result = []

        for array in anagrams.values():
            result.append(array)

        return result


        