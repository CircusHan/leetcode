class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)) :
            for j in range(i+1, len(height)):
                area = ((j-i)*min(height[i], height[j]))
                if area > max_area :
                    max_area = area
        return max_area