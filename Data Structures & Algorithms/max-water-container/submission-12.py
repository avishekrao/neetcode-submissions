class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        height_list_length = len(heights)
        start_index, stop_index = 0, height_list_length - 1
        while start_index < stop_index:
            width = stop_index - start_index
            height_vol = min(heights[start_index], heights[stop_index])
            if max_water < width * height_vol:
                max_water = width * height_vol
            if heights[start_index] < heights[stop_index]:
                start_index += 1
            else:
                stop_index -= 1
        return max_water