class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        height_list_length = len(heights)
        for start_index, height in enumerate(heights):
            for stop_index in range(height_list_length - 1, start_index, -1):
                width = stop_index - start_index
                if (max_water / width) > height:
                    break
                height_vol = min(height, heights[stop_index])
                if max_water < width * height_vol:
                    max_water = width * height_vol
        return max_water