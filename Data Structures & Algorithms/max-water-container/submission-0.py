class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left, right = 0, len(heights) - 1

        while left < right:
            currCap = self.capacity(heights[left], left, heights[right], right)
            maximum = max(maximum, currCap)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maximum

    def capacity(self, left: int,l_idx: int, right: int, r_idx: int) -> int:
        return min(left, right) * (r_idx - l_idx)



