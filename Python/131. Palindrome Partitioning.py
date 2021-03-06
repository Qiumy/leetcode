# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.ans = []
        self.dfs(s, [])
        return Solution.ans

    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    def dfs(self, s, stringlist):
        if len(s) == 0:
            Solution.ans.append(stringlist)
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist + [s[:i]])


s = Solution()
print(s.partition("aaba"))
