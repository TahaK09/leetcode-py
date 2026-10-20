class Solution(object):
    def lengthOfLastWord(self, s):
        # split the string into a list of words
        a = s.split()

        # get the lenght of the last item in the list
        b = len(a[-1])

        return b