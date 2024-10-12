# Runtime: 51ms
# Beats: 92.07%

# Memory: 18.04MB
# Beats: 8.98%

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for idx, num in enumerate(nums):
            if hash.get(num) is not None:
                return [hash.get(num), idx]
            hash[target-num] = idx