class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > remaining:
                    break
                path.append(val)
                dfs(i, remaining - val, path)  # reuse allowed
                path.pop()

        dfs(0, target, [])
        return res
        