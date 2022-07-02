class Solution:
    def romanToInt(self, s: str) -> int:
        intval = 0
        
        values_d = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        while len(s) > 1:
            if s[0] == "I":
                if s[1] == "V" or s[1] == "X":
                    intval+=values_d[s[1]]-1 
                    s = s[2:len(s)]
                else:
                    print()
                    intval+=values_d[s[0]]
                    s = s[1:len(s)]
                    
            elif s[0] == "X":
                if s[1] == "L" or s[1] == "C":
                    intval+=values_d[s[1]]-10 
                    s = s[2:len(s)]
                else:
                    intval+=values_d[s[0]]
                    s = s[1:len(s)]
            
            elif s[0] == "C":
                if s[1] == "D" or s[1] == "M":
                    
                    intval+=values_d[s[1]]-100 
                    s = s[2:len(s)]
                else:
                    intval+=values_d[s[0]]
                    s = s[1:len(s)]
            else:
                intval+=values_d[s[0]]
                s = s[1:len(s)]

        if len(s) == 1:
            intval+=values_d[s]

            
        return intval
