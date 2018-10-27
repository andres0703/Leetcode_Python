# Leetcode No.5 longest palindromic substring
# expand around center method
# time O(n^2)
#
class Solution:

    def __init__(self):
        self.lo = 0
        self.maxLen = 0

    def longestPalindromicSubstring(self, str):
        """

        :param str:
        :return: str
        """
        if len(str) < 2 or str is None:
            return str

        for i in range(len(str)):
            self.expandCenter(str, i, i)
            self.expandCenter(str, i, i + 1)
        return str[self.lo: self.lo + self.maxLen]

    def expandCenter(self, str, left, right):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            left -= 1
            right += 1
        if self.maxLen < right - left - 1:
            self.lo = left + 1
            self.maxLen = right - left - 1


if __name__ == "__main__":
    str = "abcdcbooooooabcddcba"
    print(Solution().longestPalindromicSubstring(str))
