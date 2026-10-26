class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums)!= len(nums):
            return True
        else:
            return False
        
        
        
        # for index, num in enumerate(nums):
        #     sliced_arr = nums[index + 1:]
        #     if num in sliced_arr:
        #         return false
        # return true
            