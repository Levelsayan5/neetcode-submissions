class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = defaultdict(int)
        output = []

        for i in range(len(nums)):
            dic[nums[i]] += 1

        new = sorted(dic.items(), key = lambda x: x[1], reverse = True)[:k]
        for i in new:
            output.append(i[0])
        return output

        
