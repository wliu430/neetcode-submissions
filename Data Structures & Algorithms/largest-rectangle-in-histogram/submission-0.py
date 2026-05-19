class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []

        for i, h in enumerate(heights + [0]):

            while stack and h < heights[stack[-1]]:

                idx = stack.pop()

                height = heights[idx]

                if stack:

                    width = i - stack[-1] - 1

                else:

                    width = i

                maxArea = max(maxArea, height * width)

            stack.append(i)

        return maxArea