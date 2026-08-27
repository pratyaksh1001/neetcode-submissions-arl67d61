class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if not position:
            return 0

        cars = sorted(zip(position, speed))

        c = 1

        curr = (target - cars[-1][0]) / cars[-1][1]

        for i in range(len(cars) - 2, -1, -1):

            d = target - cars[i][0]
            t = d / cars[i][1]

            if t <= curr:
                continue

            c += 1
            curr = t

        return c