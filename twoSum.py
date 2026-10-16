"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        k = 0
        while k < n:
            i = k + 1
            while i < n:
                if nums[k] + nums[i] == target:
                    return [k, i]
                i += 1
            k += 1
        return []