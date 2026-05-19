class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for p, s in zip(position, speed):

            cars.append((p, s))

        cars.sort(reverse=True)

        stack = []

        for p, s in cars:

            curTime = (target - p) / s

            if not stack or curTime > stack[-1]:

                stack.append(curTime)

        return len(stack)