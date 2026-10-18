class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        store = {}
        for i in range(len(nums)):
            
            if (f'{nums[i]}' in store) == True:
                return True

            store.update({f'{nums[i]}': i})
            
        return False
