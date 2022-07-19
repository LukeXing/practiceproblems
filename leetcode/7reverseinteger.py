class Solution:
    def reverse(self, x: int) -> int:
        invert = False
        if x < 0:
            x = -x
            invert = True
        
        y = 0 
        while x > 0:
            carry = x % 10
            y = y*10 + carry
            x = (x-carry)/10
            
        if invert:
            y = -y
            
        y = int(y)
        if y > (2**31 -1) or (y < -2**31):
            return 0
        else:
            return y
