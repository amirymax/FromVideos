class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)]
        
        for num, count in counts.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # Time: O(n)
        # Memory: O(n)
