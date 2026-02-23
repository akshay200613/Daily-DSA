class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_st = {}
        map_tst = {}

        for c1, c2 in zip(s, t):
            if c1 in map_st and map_st[c1] != c2:
                return False
            if c2 in map_tst and map_tst[c2] != c1:
                return False
            map_st[c1] = c2
            map_tst[c2] = c1

        return True
        