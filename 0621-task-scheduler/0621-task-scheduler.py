class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        max_freq = max(counts)
        max_freq_tasks = sum(freq == max_freq for freq in counts)

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + max_freq_tasks
        )