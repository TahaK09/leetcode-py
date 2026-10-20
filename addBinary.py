class Solution(object):
    def addBinary(self, a, b):
        # a and b strings into a list of integers
        b1 = [int(char) for char in a]
        b2 = [int(char) for char in b]
        carry = 0 
        rl = []  # have to reverse in the end

        i = len(b1) - 1
        j = len(b2) - 1

        while i >= 0 or j >= 0:
            total = carry #total is the sum of one column = two digits + carry that came from prev column
            if i >= 0:
                total += b1[i]
                i -= 1
            if j >= 0:
                total += b2[j]
                j -= 1
            rl.append(total % 2) #leaves us with the remainder of the total that will be appended into the rl
            carry = total // 2 #gives us the dividend, after dividing with 2 we are left with that one number that will be the carry for the number to its left

        #if the carry is 1, then append it to the end
        if carry: 
            rl.append(1)

        # join the list into one single string after reversing it
        res = ''.join(map(str, rl[::-1]))

        return res