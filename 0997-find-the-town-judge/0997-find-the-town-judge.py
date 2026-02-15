class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1   # a trusts someone
            score[b] += 1   # b is trusted
        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person
        return -1
        