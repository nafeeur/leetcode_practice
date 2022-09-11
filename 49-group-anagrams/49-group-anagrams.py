class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        [anagrams["".join(sorted(list(s)))].append(s) for s in strs]
        return anagrams.values()
            