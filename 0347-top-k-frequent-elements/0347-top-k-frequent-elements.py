class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Frequency map
        freq = Counter(nums)  # value -> count

        n = len(nums)
        # 2. Buckets: index = frequency, value = list of numbers
        buckets = [[] for _ in range(n + 1)]
        for val, count in freq.items():
            buckets[count].append(val)

        # 3. Traverse buckets from high freq to low freq
        res = []
        for c in range(n, 0, -1):
            if buckets[c]:
                for val in buckets[c]:
                    res.append(val)
                    if len(res) == k:
                        return res

        return res