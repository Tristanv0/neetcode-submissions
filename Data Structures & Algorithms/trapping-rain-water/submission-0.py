class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        while left < len(height) - 1:
            if height[left] == 0: 
                left += 1
                continue

            right = left + 1
            for i in range(left + 1, len(height)):
                if height[i] > height[right]:
                    right = i 

                if height[i] >= height[left]:
                    right = i
                    break

            total += self.calcWater(height, left, right)
            left = right
        return total
        

    def calcWater(self, height: List[int], left: int, right: int) -> int:
        total = min(height[left], height[right]) * (right - left - 1)
        
        for i in range(left + 1, right):
            total -= height[i]
        
        return total

