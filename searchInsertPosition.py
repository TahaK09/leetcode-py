class Solution(object):
    def searchInsert(self, nums, target):
        
        a = -1

        for i in range(len(nums)):
            if nums[i] == target:
                a = i
                break
        

        if a == -1:
            if target < nums[0]:
                a = 0
            elif target > nums[-1]:
                a = len(nums)
            else:
                for k in range(len(nums) - 1):
                    if nums[k] < target and nums[k + 1] > target:
                        a = k + 1
                        break


        return a
        
        
