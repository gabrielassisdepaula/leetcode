# Runtime: 120ms
# Beats: 71.09%

# Memory: 17.74MB
# Beats: 54.68%

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix_sum = []
        total = 0
        for num in nums:
            total += num
            prefix_sum.append(total)
        
        for idx in range(len(prefix_sum)):
            left_sum = prefix_sum[idx-1] if idx != 0 else 0
            right_sum = prefix_sum[-1] - prefix_sum[idx] if idx != len(nums) else 0

            if left_sum == right_sum:
                return idx
            
        return -1         