class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged_nums = nums1 + nums2
        merged_nums.sort()
        
        if len(merged_nums) % 2 == 0:
            median = (merged_nums[int(len(merged_nums)/2)] + merged_nums[int(len(merged_nums)/2)-1])/2
        else:
            median = merged_nums[int(len(merged_nums)/2-.5)]
        
        return median
