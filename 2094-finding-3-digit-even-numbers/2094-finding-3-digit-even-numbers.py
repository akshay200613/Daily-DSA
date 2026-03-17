class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        ans = []
        for num in range(100, 1000, 2):
            need = Counter(map(int, str(num)))
            ok = True
            for d, c in need.items():
                if freq[d] < c:
                    ok = False
                    break
            if ok:
                ans.append(num)

        return ans

        