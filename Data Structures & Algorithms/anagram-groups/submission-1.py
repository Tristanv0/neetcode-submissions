class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        result = []

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]

        for array in anagrams.values():
            result.append(array)

        return result


        