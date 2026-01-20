class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        used = [False] * n
        pairs = 0

        for i in range(n):
            if used[i]:
                continue
            for j in range(i + 1, n):
                if not used[j] and nums[i] == nums[j]:
                    used[i] = used[j] = True
                    pairs += 1
                    break

        leftover = sum(1 for u in used if not u)
        return [pairs, leftover]