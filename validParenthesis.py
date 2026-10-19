class Solution(object):
    def isValid(self, s):
        vp = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        st = [] #empty list

        #loops over the string s, one character at a time
        for i in s:
            if i in vp: #this line runs when i is an opening bracket
               st.append(vp[i])
            else: #this line runs when s is closing bracket
                if not st or st.pop() != i:
                    return False
            
        return not st #if leftover are preent means invalid

        