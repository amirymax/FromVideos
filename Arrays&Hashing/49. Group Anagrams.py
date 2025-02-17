class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            counts = [0]*26

            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            res[tuple(counts)].append(word)
        
        return list(res.values())
