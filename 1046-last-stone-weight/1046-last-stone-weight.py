class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            y = stones.pop()

            x = stones.pop()

            if y!= x:
                stones.append(y-x)
        return stones[0] if stones else 0
        