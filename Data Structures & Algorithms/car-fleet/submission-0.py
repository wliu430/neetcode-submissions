class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for p, s in zip(position, speed):

            cars.append((p, s))

        cars.sort(reverse=True)

        fleets = 0

        prevTime = 0

        for p, s in cars:

            curTime = (target - p) / s

            if curTime > prevTime:

                fleets += 1

                prevTime = curTime

        return fleets