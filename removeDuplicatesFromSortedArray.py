class Solution(object):
    def removeDuplicates(self, nums):
       # i is current elem, k is next elem
       # zip the original list with a sliced version shifted by 1
        for i, k in zip(nums, nums[1:]):
            if i == k:
                nums.pop(i)


