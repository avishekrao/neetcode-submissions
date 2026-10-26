class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_length = len(nums)
        left = 1
        for right in range(1, nums_length):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left