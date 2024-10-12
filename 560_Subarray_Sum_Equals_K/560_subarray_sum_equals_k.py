# Couldn`t figure this out on my own
# Solution by: `https://www.youtube.com/watch?v=fFVZt-6sgyo
# Runtime: 219ms
# Beats: 90.34%

# Memory: 19.56MB
# Beats: 30.04%

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        current_sum = 0
        prefix_sums = { 0: 1 }

        for num in nums:
            current_sum += num
            diff = current_sum - k
            result += prefix_sums.get(diff, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
        return result