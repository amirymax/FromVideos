class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        count = 1
        max_count = 1
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                count += 1
            
            elif nums[i] == nums[i - 1]:
                continue
            
            else:
                max_count = max(count, max_count)
                count = 1
        
        return max(count, max_count)
