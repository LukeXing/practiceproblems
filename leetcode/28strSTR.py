#faster than 90% of python3, more memory efficient than 97%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        char = 0 

        if needle not in haystack:
            return(-1)
        else:
            needlefound = False
            while not needlefound:

                if haystack[0:len(needle)] == needle:
                    needlefound = True
                else:
                    haystack = haystack[1:len(haystack)]
                    char+=1
                    
            return char
