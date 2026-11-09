class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = defaultdict(int)
        output = []

        for i in range(len(nums)):
            dic[nums[i]] += 1

        # Now that frequency of each element in nums have been 
        # counted, we will sort the dictionary into sets of 
        # tuples where the counts (values) is ordered from largest
        # to smallest. From there, we extract only the top k 
        # numbers with the highest frequencies of appearing
        new = sorted(dic.items(), key = lambda x: x[1], reverse = True)[:k]
        # Take the keys from each item and append to a new list
        # to be returned
        for i in new:
            output.append(i[0])
        return output

        
