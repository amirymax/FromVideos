class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            s = ''.join(sorted(i))
            # print(s)
            ans[s] = ans.get(s,[])+[i]
        return list(ans.values())