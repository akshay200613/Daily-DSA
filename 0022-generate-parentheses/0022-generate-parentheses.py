class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count, close_count, curr):
            # If the current string has 2*n characters, it's a valid combination
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # We can add '(' if we still have left parentheses remaining
            if open_count < n:
                backtrack(open_count + 1, close_count, curr + "(")

            # We can add ')' only if it won't break validity
            if close_count < open_count:
                backtrack(open_count, close_count + 1, curr + ")")

        backtrack(0, 0, "")
        return res
        