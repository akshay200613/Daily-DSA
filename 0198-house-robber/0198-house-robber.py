class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0  # rob1 = dp[i-2], rob2 = dp[i-1]
        for n in nums:
            newRob = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = newRob
        return rob2
        