# class Solution(object):
#     def removeDuplicates(self, nums):
#        # i is current elem, k is next elem
#        # zip the original list with a sliced version shifted by 1
#         for i, k in zip(nums, nums[1:]):
#             if i == k:
#                 nums.pop(i)

    # above solution fails many test cases, need to find a better solution.
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        count = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[count-1]:
                nums[count] = nums[i]
                count += 1
        
        return count
            

            
       


