class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r,i = 0,0,-1
        max_sub = 0

        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif i == -1:
                i = r
                r += 1
            else:
                max_sub = max(max_sub, r-l)
                l = i + 1
                i = -1
                r = l

        return max(max_sub, r-l) - 1
