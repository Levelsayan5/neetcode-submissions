class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maj_element = len(nums)/2
        storage = {}
        
        for i in range(len(nums)):
            if nums.count(nums[i]) > maj_element:
                return nums[i]
                 
