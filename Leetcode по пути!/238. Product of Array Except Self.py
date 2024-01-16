class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        p = 1
        for i in range(1, len(nums)):
            p *= nums[i - 1]
            answer[i] = p
        
        p = 1
        for i in range(len(nums) - 2, -1, -1):
            p *= nums[i + 1]
            answer[i] *= p
        
        return answer
