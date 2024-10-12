# https://www.youtube.com/watch?v=bNvIQI2wAjk
# Runtime: 255ms
# Beats: 93.98%

# Memory: 25.82MB
# Beats: 39.17%

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1]*len(nums)

        prefix = 1
        for idx in range(len(nums)):
            output[idx] = prefix
            prefix *= nums[idx]

        postfix = 1
        for idx in range(len(nums)-1, -1, -1):
            output[idx] *= postfix
            postfix *= nums[idx]
        
        return output