class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break   
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]

                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
