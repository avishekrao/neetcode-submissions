class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(2 * len(nums)):
            if i < len(nums):
                new_list.append(nums[i])
            else:
                new_list.append(nums[i - len(nums)])
        return new_list