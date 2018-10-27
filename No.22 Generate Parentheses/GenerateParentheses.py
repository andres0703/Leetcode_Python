class Solution:

    def generateParentheses(self, n):
        ans = []

        def backtrack(res, cur, max, open, close):
            if len(cur) == 2 * max:
                res.append(cur)

            if open < max:
                backtrack(res, cur + '(', max, open + 1, close)
            if close < open:
                backtrack(res, cur + ')', max, open, close + 1)

        backtrack(ans, '', n, 0, 0)
        return ans


if __name__ == "__main__":
    print(Solution().generateParentheses(3))
