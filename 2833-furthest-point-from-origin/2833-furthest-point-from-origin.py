class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        positions = {0}
        for c in moves:
            new_positions = set()
            for pos in positions:
                if c == 'L':
                    new_positions.add(pos - 1)
                elif c == 'R':
                    new_positions.add(pos + 1)
                else:  # '_'
                    new_positions.add(pos - 1)
                    new_positions.add(pos + 1)
            positions = new_positions
        return max(abs(p) for p in positions)