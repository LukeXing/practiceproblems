class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        initial_len = len(nums)
        elements_deleted = 0
        elements_removed = 0
        
        for integer in nums:
            if integer == val:
                elements_deleted += 1
            
        elements_removed = elements_deleted
        
        while elements_removed > 0:
            nums.remove(val)
            print(nums)
            elements_removed -= 1

            
        return(initial_len-elements_deleted)
