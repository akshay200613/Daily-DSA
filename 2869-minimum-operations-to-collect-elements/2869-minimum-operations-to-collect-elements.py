class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        ops = 0
        for i in range(len(nums) - 1, -1, -1):
            ops += 1
            x = nums[i]
            if 1 <= x <= k:
                seen.add(x)
            if len(seen) == k:
                return ops
        return ops
        