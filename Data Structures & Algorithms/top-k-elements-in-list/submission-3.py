class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        sorted_frequencies = dict(sorted
            (frequencies.items(), 
            key = lambda item: item[1], 
            reverse = True))
        return_list = []
        keys_list = list(sorted_frequencies.keys())
        for i in range(k):
            return_list.append(keys_list[i])
        return return_list