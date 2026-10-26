class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [hashmap[difference], index]
            else:
                hashmap[num] = index