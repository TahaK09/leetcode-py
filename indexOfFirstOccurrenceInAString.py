class Solution(object):
    def strStr(self, haystack, needle):

       
        if needle in haystack:
            a = haystack.find(needle)
        else:
            a = -1

        return a

        