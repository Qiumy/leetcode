__author__ = 'Minyi'
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.solve(sorted(candidates), target)

    def solve(self, candidates, target):
        if target == 0:
            return [[]]
        ans = []
        for i in range(len(candidates)):
            if i != 0 and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            for r in self.solve(candidates[i + 1:], target - candidates[i]):
                ans.append([candidates[i]] + r)
        return ans
