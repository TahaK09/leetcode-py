class Solution(object):
    def removeElement(self, nums, val):
       
       count = 0

        # iterate through every element in the list
       for i in nums:
         if i != val: #if it isn't the val, add it to the list
            nums[count] = i
            count += 1 #update count on every iteration
    
       return count

        
