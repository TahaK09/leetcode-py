class Solution(object):
    def mySqrt(self, x):
       # what i am gonna do is start at 0 and in every iteration square the number.. as it is a non-negative number it is going to be smaller/ lie in a range which is smaller than the number x... we can iterate and if a number squared becomes greater than the input number "x" that means the previous number is the answer (i-1)
       i = 0
       c = 0

       while True:
        s = i * i
        if s > x:
            c = i - 1
            break
        i += 1
    
       return c
        
# another approach is to use binary search, as the square root of a number is always smaller than the number itself, we can use binary search to find the square root of a number. The time complexity of this approach is O(log n) and the space complexity is O(1).
# class Solution(object):
#     def mySqrt(self, x):
#         if x < 2:
#             return x

#         left = 1
#         right = x // 2

#         while left <= right:
#             mid = (left + right) // 2

#             if mid * mid == x:
#                 return mid
#             elif mid * mid < x:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return right

        

        