class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        storage = {}
        ans = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in storage:
                ans.append(storage[difference])
                ans.append(i)
                return ans
            storage[nums[i]] = i

