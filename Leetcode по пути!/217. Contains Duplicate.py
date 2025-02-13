class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)

        for i in nums:
            counts[i] += 1
            if counts[i] == 2:
                return True
        
        return False

        # O(n)
        # Memory O(n)
