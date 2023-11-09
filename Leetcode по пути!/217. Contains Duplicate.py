class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_array = set(nums)
        return len(set_array) != len(nums)
        