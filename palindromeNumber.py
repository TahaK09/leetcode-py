"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        # breaking the number digits into a list
        a = list(map(int, str(x)))
        n = len(a)
        
        for i in range(n // 2):
            if a[i] != a[n - 1 - i]:
                return False
        return True
