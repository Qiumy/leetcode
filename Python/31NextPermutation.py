#! usr/bin/python #coding=utf-8
__author__ = 'Minyi'
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# 首先，从最尾端开始往前寻找两个相邻的元素，令第一个元素是 i，第二个元素是 ii，且满足 i<ii ；
# 然后，再从最尾端开始往前搜索，找出第一个大于 i 的元素，设其为 j；
# 然后，将 i 和 j 对调，再将 ii 及其后面的所有元素反转。
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not len(nums):
            return

        index = len(nums) - 2

        while index >= 0 and nums[index] >= nums[index + 1]:
            index -= 1

        if index >= 0:
            i = index + 1
            while i < len(nums) and nums[i] > nums[index]:
                i += 1
            nums[i-1], nums[index] = nums[index], nums[i-1]

        left, right = index + 1, len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



