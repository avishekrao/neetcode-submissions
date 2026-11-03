class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = nums.sort()
        result = []
        for index, num in enumerate(nums):
            if num > 0:
                break
            if index > 0 and num == nums[index - 1]:
                continue

            left_pointer, right_pointer = index + 1, len(nums) - 1
            while left_pointer < right_pointer:
                threeSum = num + nums[left_pointer] + nums[right_pointer]
                if threeSum > 0:
                    right_pointer -= 1
                elif threeSum < 0:
                    left_pointer += 1
                else:
                    result.append([num, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1
        
        return result
            