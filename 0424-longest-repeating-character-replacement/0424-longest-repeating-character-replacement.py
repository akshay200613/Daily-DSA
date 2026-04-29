class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            max_freq = max(max_freq, count[idx])

            while (r - l + 1) - max_freq > k:
                left_idx = ord(s[l]) - ord('A')
                count[left_idx] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
        