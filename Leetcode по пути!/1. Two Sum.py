class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = nums[i]
            diff = target - x
            if diff in nums[i+1:]:
                nums[i] = 'a'
                y = nums.index(diff)
                return [i, y]
                