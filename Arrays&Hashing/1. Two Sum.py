class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elems = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in elems:
                return [elems[diff], i]
            elems[nums[i]] = i
        
            
        
