class Solution:
    def isPalindrome(self, x: int) -> bool:
        #if x int is less than 0, auto not palindrome and i think single digit numbers
        if x < 0 or (x > 0 and x%10 == 0):   
            return False

        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10
        
        # kinda skipping a step here by adding check - faster to not iterate last section
        if (x == reverse or x == reverse // 10):
            return True 
        else:
            return False
