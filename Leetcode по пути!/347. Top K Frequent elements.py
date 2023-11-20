class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for i in nums:
            a[i] = a.get(i, 0) + 1
        
        a = dict(sorted(a.items(), key = lambda x: x[1])[::-1])

        ans = []
        keys = list(a.keys())
        for i in range(k):
            ans.append(keys[i])
        
        return ans
