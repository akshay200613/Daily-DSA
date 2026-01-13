class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.next_num(n)
        return n == 1
    
    def next_num(self, n: int) -> int:
        s = 0
        while n > 0:
            d = n % 10
            s += d * d
            n //= 10
        return s
        