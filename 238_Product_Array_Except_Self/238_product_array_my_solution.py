# Runtime: 257ms
# Beats: 91.40%

# Memory: 26.26MB
# Beats: 24.03%

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_product = []
        postfix_product = [None]*len(nums)
        
        total_prefix = 1
        for num in nums:
            total_prefix *= num
            prefix_product.append(total_prefix)
        
        total_postfix = 1
        for idx in range(len(nums)-1, -1, -1):
            total_postfix *= nums[idx]
            postfix_product[idx] = total_postfix

        output = []
        for idx in range(len(nums)):
            prefix = prefix_product[idx-1] if idx > 0 else 1
            postfix = postfix_product[idx+1] if idx < len(nums)-1 else 1
            output.append(prefix*postfix)


        return output