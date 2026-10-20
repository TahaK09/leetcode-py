class Solution(object):
    def plusOne(self, digits):
        #val, where the final incremented num will be store before final output
     val = 0

     for i in range(len(digits)):
            val += digits[-1 - i] * 10**i
        # or, val = val * 10 + digits[i]
        
     val = val + 1

        #converting the final value after increment into a list
     a = list(map(int, str(val)))

     return a




        